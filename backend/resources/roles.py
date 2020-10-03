import json
from functools import wraps
from flask import Response, request
from database.models import Workout, User, Role, Team
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, WorkoutAlreadyExistsError, \
InternalServerError, UpdatingWorkoutError, DeletingWorkoutError, WorkoutNotExistsError, \
UnauthorizedError

def default_exception_handler(function):
    """Handle form exceptions."""
    def wrap(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except TypeError:
            raise SchemaValidationError
        except InvalidQueryError:
            raise SchemaValidationError
        except Exception:
            raise InternalServerError
   
    return wrap

def manager_role_required(function):
    """Allow only user with mangager role."""
    @wraps(function)
    def wrap(*args, **kwargs):
        user = User.objects.get(id=get_jwt_identit())
        if 'manager' not in [role.name for role in user.roles]:
            raise UnauthorizedError
        return function(*args, **kwargs)
   
    return wrap


def coach_role_required(function):
    """Allow only user with coach role."""
    @wraps(function)
    def wrap(*args, **kwargs):
        user = User.objects.get(id=get_jwt_identit())
        if 'coach' not in [role.name for role in user.roles]:
            raise UnauthorizedError

        return function(*args, **kwargs)
   
    return wrap


def check_same_team(source_user, target_user):
    """Check if actor and target are in same team."""

    # If active user is not in team, deny
    if source_user.team is None:
        raise UnauthorizedError
    
    # If users are in team, it must be the same
    if source_user.team != target_user.team:
        raise UnauthorizedError

    return True


def manager_role_required(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        # First, check if user is manager for the team
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        print(user.team)
        if 'manager' in [role.name for role in user.roles]:
            print('user is manager')
        else:
            raise UnauthorizedError
        return function(*args, **kwargs)
   
    return wrap


class TeamApi(Resource):
  @default_exception_handler
  @jwt_required
  def post(self):
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    response_data = json.dumps({'username': user.username,
                                'email': user.email,
                                'roles': [role.name for role in user.roles],
                                'team': user.team.name})
    return Response(response_data, mimetype="application/json", status=200)


class WhoamiApi(Resource):
  @default_exception_handler
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    response_data = json.dumps({'username': user.username,
                                'email': user.email,
                                'roles': [role.name for role in user.roles],
                                'team': user.team.name})
    return Response(response_data, mimetype="application/json", status=200)


class WhoisApi(Resource):
  @default_exception_handler
  @jwt_required
  def get(self):
    body = request.get_json()
    username = body['username']
    user = User.objects.get(username=username)
    response_data = json.dumps({'username': user.username,
                                'email': user.email,
                                'roles': [role.name for role in user.roles],
                                'team': user.team})
    return Response(response_data, mimetype="application/json", status=200)


class ManagerRoleApi(Resource):
  @default_exception_handler
  @jwt_required
  #@manager_role_required
  def post(self):
    active_user = User.objects.get(id=get_jwt_identity())
    body = request.get_json()
    target_username = body['username']
    target_user = User.objects.get(username=target_username)
    if check_same_team(active_user, target_user):
        target_user.add_manager_role()
    return f'Manager role added to {target_username}.', 200


  @default_exception_handler
  @jwt_required
  @manager_role_required
  def delete(self):
    active_user = User.objects.get(id=get_jwt_identity())
    body = request.get_json()
    target_username = body['username']
    target_user = User.objects.get(username=target_username)
    if check_same_team(active_user, target_user):
        target_user.rm_manager_role()
        return f'Manager role removed from {target_username}.', 200


class TeamApi(Resource):
  @default_exception_handler
  @jwt_required
  def post(self):
    '''Create a new team and join it'''
    active_user = User.objects.get(id=get_jwt_identity())
    if active_user.team is not None:
        return f'User must leave team before creating a new team', 412

    body = request.get_json()
    requested_teamname = body['name']

    # Check for name collision
    if Team.objects.get(name=requested_teamname): 
        return f'Teamname {requested_teamname} already exists', 412

    team = Team(**body)
    team.save()

    active_user.team = team
    active_user.save()

    return f'Requested team {requested_teamname} created.', 200


  @default_exception_handler
  @jwt_required
  def put(self):
    '''Delete a team and join it'''
    active_user = User.objects.get(id=get_jwt_identity())
    if active_user.team is not None:
        active_user.team = None
        active_user.save()

    body = request.get_json()
    requested_teamname = body['name']

    # Check for name collision
    if not Team.objects.get(name=requested_teamname): 
        return f'Teamname {requested_teamname} already exists', 412

    team = Team(**body)
    team.save()

    active_user.team = team
    active_user.save()

    return f'Requested team {requested_teamname} created.', 200

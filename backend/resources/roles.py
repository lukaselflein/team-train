import json
from functools import wraps
from flask import Response, request
from database.models import Workout, User, Role
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, WorkoutAlreadyExistsError, \
InternalServerError, UpdatingWorkoutError, DeletingWorkoutError, WorkoutNotExistsError, \
UnauthorizedError


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


def same_team_required(function):
    """Allow only interaction for targets in same team."""
    @wraps(function)
    def wrap(*args, **kwargs):
        user = User.objects.get(id=get_jwt_identit())
        # TODO: Not clear how to implement this.
        # The team info is the target, which is not accessible in the wrapper
        # but only with a lookup on the json body. maybe implement this in the
        # actual function?

        return function(*args, **kwargs)
   
    return wrap


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


class WhoamiApi(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    response_data = json.dumps({'username': user.username,
                                'email': user.email,
                                'roles': [role.name for role in user.roles],
                                'team': user.team})
    return Response(response_data, mimetype="application/json", status=200)


class WhoisApi(Resource):
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
  @jwt_required
  @manager_role_required
  def post(self):

    try:
        body = request.get_json()
        # TODO: check if requested user-id is in manager's team
        username = body['username']
        user = User.objects.get(username=username)
        try:
            manager_role = Role.objects.get(name='manager')
        except:
            manager_role = Role(name='manager')
        manager_role.save()
        user.update(roles=[manager_role])
        return f'Role added.', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingWorkoutError
    except Exception:
        raise InternalServerError


  @jwt_required
  @manager_role_required
  def delete(self):
    # First, check if user is manager for the team
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    print(user.team)
    if 'manager' in [role.name for role in user.roles]:
        print('user is manager')
    else:
        raise UnauthorizedError

    try:
        body = request.get_json()
        # TODO: check if requested user-id is in manager's team
        username = body['username']
        user = User.objects.get(username=username)
        manager_role = Role.objects.get(name='manager')
        print(manager_role)
        user.update(roles=[])
        return f'Role deleted.', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingWorkoutError
    except Exception:
        raise InternalServerError

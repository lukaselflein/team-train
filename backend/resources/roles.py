import json
from flask import Response, request
from database.models import Workout, User, Role
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, WorkoutAlreadyExistsError, \
InternalServerError, UpdatingWorkoutError, DeletingWorkoutError, WorkoutNotExistsError


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
  #@manager_role_required
  def put(self):
    try:
        body = request.get_json()
        # TODO: check if requested user-id is in manager's team
        username = body['username']
        user = User.objects.get(username=username)
        manager_role = Role(name='manager')
        manager_role.save()
        user.update(roles=[manager_role])
        return f'Roles of {username} changed to {user.roles}', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingWorkoutError
    except Exception:
        raise InternalServerError

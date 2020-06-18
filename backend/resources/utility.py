import json
from flask import Response, request
from database.models import Workout, User
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
    response_data = json.dumps({'username': user.username, 'email': user.email,
                                'roles': user.roles, 'team': user.team})
    return Response(response_data, mimetype="application/json", status=200)

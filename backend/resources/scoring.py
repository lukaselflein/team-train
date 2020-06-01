import json
from flask import Response, request
from database.models import Workout, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, WorkoutAlreadyExistsError, \
InternalServerError, UpdatingWorkoutError, DeletingWorkoutError, WorkoutNotExistsError


class ScoringApi(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    body = request.get_json()
    user = User.objects.get(id=user_id)
    response_data = json.dumps({'score': user.score})
    return Response(response_data, mimetype="application/json", status=200)

class ClaimingApi(Resource):
  @jwt_required
  def post(self):
    return
    try:
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        user.score = 100
        user.save()
        return {'workout claimed sucessfully.'}, 200

    except Exception as e:
        raise InternalServerError

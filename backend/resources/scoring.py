import json
import time
from flask import Response, request
from database.models import Workout, User, ScoreLog
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, WorkoutAlreadyExistsError, \
InternalServerError, UpdatingWorkoutError, DeletingWorkoutError, WorkoutNotExistsError


class CurrentScoreApi(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    response_data = json.dumps({'score': user.current_score})
    return Response(response_data, mimetype="application/json", status=200)


class ScoreHistoryApi(Resource):
  @jwt_required
  def get(self):
    user_id = get_jwt_identity()
    user = User.objects.get(id=user_id)
    history = [log.to_dict() for log in user.score_history]
    response_data = json.dumps(history)
    return Response(response_data, mimetype="application/json", status=200)


class ClaimingApi(Resource):
  @jwt_required
  def post(self, id):
    try:
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        # Look up the workout the user just claimed
        workout = Workout.objects.get(id=id)
        # Extract the points assigned to the workout 
        user.current_score += workout.points
        # Write this score into a logfile (date is added automatically)
        log_entry = ScoreLog(points=workout.points, 
                             score=user.current_score, added_by=user_id)
        # Save logfile to db
        log_entry.save()
        # Write the logfile to the user's history
        user.update(push__score_history=log_entry)
        user.save()

        return {'result': f'claimed',
                'workout id': f'{id}',
                'workout points': f'{workout.points}'}, 200

    except Exception as e:
        raise InternalServerError

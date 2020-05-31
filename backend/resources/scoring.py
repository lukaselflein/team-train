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
  def get(self):
    db_workouts = Workout.objects()
    # flatten the default db entries for a readable api response
    workout_dicts = []
    for db_workout in db_workouts:
        pretty_workout = {
          'id': str(db_workout.id),
          'exercises':  [{'name': e.name, 'quantity': e.quantity, 'description': e.description} 
                         for e in db_workout.exercises],
          'time': str(db_workout.date_added),
          'added_by': str(db_workout.added_by.username),
          'description': str(db_workout.description),
          'points': db_workout.points,
          'has_timer': db_workout.has_timer,
          'tags': db_workout.tags
          }
        workout_dicts += [pretty_workout]

    response_data = json.dumps(workout_dicts)
    return Response(response_data, mimetype="application/json", status=200)

  @jwt_required
  def post(self):
    try:
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        workout = Workout(**body, added_by=user)
        workout.save()
        user.update(push__workouts=workout)
        user.save()
        id = workout.id
        return {'id': str(id)}, 200

    except (FieldDoesNotExist, ValidationError):
        raise SchemaValidationError
    except NotUniqueError:
        raise WorkoutAlreadyExistsError
    except Exception as e:
        raise InternalServerError

import json
from flask import Response, request
from database.models import Workout, User
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from mongoengine.errors import FieldDoesNotExist, \
NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from resources.errors import SchemaValidationError, WorkoutAlreadyExistsError, \
InternalServerError, UpdatingWorkoutError, DeletingWorkoutError, WorkoutNotExistsError


class WorkoutsApi(Resource):
  def get(self):
    workouts = Workout.objects()
    # flatten the default db entries for a readable api response
    workout_dicts = [workout.to_dict() for workout in workouts]
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


class WorkoutApi(Resource):
  @jwt_required
  def put(self, id):
    try:
        user_id = get_jwt_identity()
        workout = Workout.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Workout.objects.get(id=id).update(**body)
        return 'Workout changed successfully.', 200
    except InvalidQueryError:
        raise SchemaValidationError
    except DoesNotExist:
        raise UpdatingWorkoutError
    except Exception:
        raise InternalServerError
 
  @jwt_required
  def delete(self, id):
    try:
        user_id = get_jwt_identity()
        # Filter for workouts belonging to authenticated user
        workout = Workout.objects.get(id=id, added_by=user_id)
        workout.delete()
        return '', 200
    except DoesNotExist:
        raise DeletingWorkoutError
    except Exception:
        raise InternalServerError

  def get(self, id):
    try:
        db_workout = Workout.objects.get(id=id)

        # the db object is pretty deep, flatten it to make stuff easier for the fronted
        pretty_workout = {
          'id': str(db_workout.id),
          'exercises':  [{'name': e.name, 'quantity': e.quantity, 'description': e.description} 
                         for e in db_workout.exercises],
          'time': str(db_workout.date_added),
          'added_by': str(db_workout.added_by.username),
          'description': str(db_workout.description),
          'points': db_workout.points,
          'has_timer': db_workout.has_timer,
          'tags': db_workout.tags,
          'name': db_workout.name
          }

        response_data = json.dumps(pretty_workout)
        return Response(response_data, mimetype="application/json", status=200)

    except DoesNotExist:
        raise WorkoutNotExistsError
    except Exception:
        raise InternalServerError


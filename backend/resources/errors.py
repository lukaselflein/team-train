class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class WorkoutAlreadyExistsError(Exception):
    pass

class UpdatingWorkoutError(Exception):
    pass

class DeletingWorkoutError(Exception):
    pass

class WorkoutNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "WorkoutAlreadyExistsError": {
         "message": "Workout with given name already exists",
         "status": 400
     },
     "UpdatingWorkoutError": {
         "message": "Updating workout added by other is forbidden",
         "status": 403
     },
     "DeletingWorkoutError": {
         "message": "Deleting workout added by other is forbidden",
         "status": 403
     },
     "WorkoutNotExistsError": {
         "message": "Workout with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}


from .workouts import WorkoutsApi, WorkoutApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(WorkoutsApi, '/api/workouts')
    api.add_resource(WorkoutApi, '/api/workouts/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

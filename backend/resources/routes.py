from .workouts import WorkoutsApi, WorkoutApi
from .auth import SignupApi, LoginApi
from .scoring import ScoringApi, ClaimingApi

def initialize_routes(api):
    api.add_resource(WorkoutsApi, '/workouts')
    api.add_resource(WorkoutApi, '/workouts/<id>')
    api.add_resource(SignupApi, '/signup')
    api.add_resource(LoginApi, '/login')
    api.add_resource(ClaimingApi, '/claim/<id>')
    api.add_resource(ScoringApi, '/score')

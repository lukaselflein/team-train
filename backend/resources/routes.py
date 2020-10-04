from .workouts import WorkoutsApi, WorkoutApi
from .auth import SignupApi, LoginApi
from .scoring import CurrentScoreApi, ScoreHistoryApi, ClaimingApi
from .roles import UserApi, ManagerRoleApi, WhoisApi, TeamApi

def initialize_routes(api):
    api.add_resource(WorkoutsApi, '/workouts')
    api.add_resource(WorkoutApi, '/workouts/<id>')
    api.add_resource(SignupApi, '/signup')
    api.add_resource(LoginApi, '/login')
    api.add_resource(ClaimingApi, '/claim/<id>')
    api.add_resource(CurrentScoreApi, '/my_score')
    api.add_resource(ScoreHistoryApi, '/my_score_history')
    api.add_resource(UserApi, '/user')
    api.add_resource(ManagerRoleApi, '/manager')
    api.add_resource(WhoisApi, '/whois')
    api.add_resource(TeamApi, '/team')

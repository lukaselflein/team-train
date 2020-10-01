from .workouts import WorkoutsApi, WorkoutApi
from .auth import SignupApi, LoginApi
from .scoring import CurrentScoreApi, ScoreHistoryApi, ClaimingApi
from .roles import WhoamiApi, ManagerRoleApi, WhoisApi

def initialize_routes(api):
    api.add_resource(WorkoutsApi, '/workouts')
    api.add_resource(WorkoutApi, '/workouts/<id>')
    api.add_resource(SignupApi, '/signup')
    api.add_resource(LoginApi, '/login')
    api.add_resource(ClaimingApi, '/claim/<id>')
    api.add_resource(CurrentScoreApi, '/my_score')
    api.add_resource(ScoreHistoryApi, '/my_score_history')
    api.add_resource(WhoamiApi, '/whoami')
    api.add_resource(ManagerRoleApi, '/make_manager')
    api.add_resource(WhoisApi, '/whois')
    #api.add_resource(UserApi, '/user/<id>')

import json
from flask import Response, request
from database.models import Workout, User, Role, Team
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from resources.decorators import default_exception_handler, manager_role_required, coach_role_required, check_same_team


# TODO
# Length restriction on username, teamname, etc

class TeamApi(Resource):
    """Manage teams and their members."""
    @jwt_required
    @default_exception_handler
    def post(self):
        """User creates a new team and join it"""
        active_user = User.objects.get(id=get_jwt_identity())
        if active_user.team is not None:
            return f'User must leave team before creating a new team', 412

        body = request.get_json()
        requested_teamname = body['name']

        # Check for name collision
        try:
            Team.objects.get(name=requested_teamname)
            return f'Teamname {requested_teamname} already exists', 412
        except:
            pass

        team = Team(**body)
        team.save()

        active_user.team = team
        active_user.save()

        return f'Requested team {requested_teamname} created.', 200

    @jwt_required
    @default_exception_handler
    @manager_role_required
    def delete(self):
        '''Manager deletes a team and leaves it'''
        active_user = User.objects.get(id=get_jwt_identity())
        if active_user.team is None:
            return f'User must be in team to delete it.', 400

        requested_teamname = request.get_json()['name']

        # Check if team exists
        if not Team.objects.get(name=requested_teamname): 
            return f'Teamname {requested_teamname} does not exist', 400


        target_team = Team.objects.get(name=requested_teamname)
        target_team.delete()
        active_user.leave_team()

        return f'Requested team {requested_teamname} deleted.', 200


class UserApi(Resource):
   """Modify the user account."""

   @jwt_required
   @default_exception_handler
   def get(self):
      """Info on current user."""
      user_id = get_jwt_identity()
      user = User.objects.get(id=user_id)
      response_data = json.dumps({'username': user.username,
                                  'email': user.email,
                                  'roles': [role.name for role in user.roles],
                                  'team': str(user.team)})
      return Response(response_data, mimetype="application/json", status=200)

   @jwt_required
   @default_exception_handler
   def post(self):
       '''Join a team.'''
       user = User.objects.get(id=get_jwt_identity())
       if user.team is not None:
           return f'User must not be in a team to join a team.', 400

       requested_teamname = request.get_json()['name']
       user.join_team(name=requested_teamname)

       return f'User {user.name} left team.', 200

   @jwt_required
   @default_exception_handler
   def put(self):
       '''Leave a team.'''
       user = User.objects.get(id=get_jwt_identity())
        
       body = request.get_json()
       requested_teamname = body['name']

       if user.team is None:
           return f'User must be in team to leave it.', 400

       user.leave_team()
       return f'User {user.name} left team.', 200

   @jwt_required
   @default_exception_handler
   def delete(self):
       """Delete user account"""
       return f'User {user.name} deleted - NOT IMPLEMENTED', 200


class WhoisApi(Resource):
  """Print info on target user."""
  @jwt_required
  @default_exception_handler
  def get(self):
    body = request.get_json()
    username = body['username']
    user = User.objects.get(username=username)
    response_data = json.dumps({'username': user.username,
                                'email': user.email,
                                'roles': [role.name for role in user.roles],
                                'team': user.team})
    return Response(response_data, mimetype="application/json", status=200)


class ManagerRoleApi(Resource):
  """Team-Manager admin role."""
  @jwt_required
  @default_exception_handler
  #@manager_role_required
  def post(self):
    active_user = User.objects.get(id=get_jwt_identity())
    body = request.get_json()
    target_username = body['username']
    target_user = User.objects.get(username=target_username)
    if check_same_team(active_user, target_user):
        target_user.add_manager_role()
    return f'Manager role added to {target_username}.', 200


  @jwt_required
  @default_exception_handler
  @manager_role_required
  def delete(self):
    active_user = User.objects.get(id=get_jwt_identity())
    body = request.get_json()
    target_username = body['username']
    target_user = User.objects.get(username=target_username)
    if check_same_team(active_user, target_user):
        target_user.rm_manager_role()
        return f'Manager role removed from {target_username}.', 200



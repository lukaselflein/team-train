from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required
import datetime
import json

class Exercise(db.EmbeddedDocument):
    '''An exercise has a name, and a quantity (number of reps/time).'''
    # What kind of exercise?
    name = db.StringField(required=True)
    # How many?
    quantity = db.IntField(required=True)
    # Seconds/Reps
    unit = db.StringField()
    # Free-text details
    description = db.StringField()

    def to_dict(self):
        return {'name': self.name, 
                'quantity': self.quantity, 
                'description': self.description}


class ScoreLog(db.Document):
    '''The history of a user's scores, in the format {time: t, score: 5}'''
    score = db.IntField(required=True)
    points = db.IntField(required=True)
    time = db.DateTimeField(default=datetime.datetime.utcnow)
    workout_id = db.StringField()
    added_by = db.ReferenceField('User')
    name = db.StringField(default='score_log')

    def to_dict(self):
        log = {'time': str(self.time), 'score': self.score, 'points': self.points}
        return log


class Workout(db.Document):
    '''A workout contains exercises and metadata.
    >>> e1 = Exercise(name='Pushup', quantity = 100)
    >>> w = Workout(name='One Punch Workout', points=9000, exercises=[e1]) '''

    exercises = db.ListField(db.EmbeddedDocumentField(Exercise), required=True)
    name = db.StringField(required=True)
    points = db.IntField(required=True)
    added_by = db.ReferenceField('User')
    date_added = db.DateTimeField(default=datetime.datetime.utcnow)
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)
    description = db.StringField()
    has_timer = db.BooleanField(default=False)
    tags = db.ListField(db.StringField())

    def to_dict(self): 
        workout_dict = {
          'id': str(self.id),
          'exercises': [e.to_dict() for e in self.exercises],
          'time': str(self.date_added),
          'added_by': str(self.added_by.username),
          'description': str(self.description),
          'points': self.points,
          'has_timer': self.has_timer,
          'tags': self.tags,
          'name': self.name
          }
        return workout_dict


class Role(db.Document):
    """Abstract role object for controlling user permissions."""
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class RoleContainer(db.Document):
    """Container object for user roles."""
    roles = db.ListField(db.ReferenceField('Role'), default=[])


class Team(db.Document):#, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    # TODO: add reference to all members in team
    members = None
    team_score = None

    def delete(self):
        """Remove team object; kick all members from team."""
        print('Team deletion triggered. Not implemened.')
        # TODO

    def show_score(self):
        """Returns sum of scores of team members."""
        score = 0
        for member in self.members:
            score += member.score
        return score

    def show_member_names(self):
        """Returns list of member-name strings."""
        return [member.name for member in self.members]

    def __str__(self):
        return self.name


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    workouts = db.ListField(db.ReferenceField('Workout', reverse_delete_rule=db.PULL))
    team = db.ReferenceField('Team', default=None)
    current_score = db.IntField(default=0)
    score_history = db.ListField(db.ReferenceField('ScoreLog', reverse_delete_rule=db.PULL))


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def add_manager_role(self):
        """User is now manager, can modify teams"""
        try:
            manager_role = Role.objects.get(name='manager')
        except:
            manager_role = Role(name='manager')
            manager_role.save()

        if manager_role not in self.roles:
            self.roles.append(manager_role)
            self.save()
        else:
            raise RuntimeError('Role already assigned')

    def rm_manager_role(self):
        """User no longer is manager"""
        try:
            manager_role = Role.objects.get(name='manager')
        except:
            manager_role = Role(name='manager')
            manager_role.save()

        if manager_role in self.roles:
            self.update(pull__roles=manager_role)
            self.save()
        else:
            raise RuntimeError('Cannot remove, role not assigned')

    def join_team(self, team_name):
        """Join existing team; Error on missing rights or missing team"""
        try:
            team = Role.objects.get(name=team_name)
        except:
            raise RuntimeError('Team does not exist.')

        if self.team:
            raise RuntimeError('User already in team.')

        self.team = team
        self.save()

    def leave_team(self):
        """Leave current team"""
        if self.team is None:
            raise RuntimeError('User not in team, cannot leave.')

        # TODO: if user is last member of team, delete it
        # if len(self.team.members) == 1:
        #       self.team.delete()
        #       return 'team deleted'

        self.team = None
        self.save()

        # TODO: if user is last member with manager role, transfer role to last active member
        

    def create_team(self, team_name):
        """Create new team and join"""
        # TODO: Check if team exists
        # Error if if does exist
        # Create team otherwise
        # join team
        pass


# Remove all workouts created by user upon deletion of user object
User.register_delete_rule(Workout, 'added_by', db.CASCADE)

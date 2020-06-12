from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
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



class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    workouts = db.ListField(db.ReferenceField('Workout', reverse_delete_rule=db.PULL))
    roles = db.ListField()
    team = db.StringField()
    current_score = db.IntField(default=0)
    score_history = db.ListField(db.ReferenceField('ScoreLog', reverse_delete_rule=db.PULL))


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_team(self, team):
        self.team = team

    def add_role(self, role):
        if role not in self.roles:
            self.roles += [role]


User.register_delete_rule(Workout, 'added_by', db.CASCADE)

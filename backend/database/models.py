from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

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

class Workout(db.Document):
    '''A workout contains exercises and metadata.
    >>> e1 = Exercise(name='Pushup', quantity = 100)
    >>> w = Workout(name='One Punch Workout', points=9000, exercises=[e1]) '''

    exercises = db.ListField(db.EmbeddedDocumentField(Exercise), required=True)
    name = db.StringField(required=True)
    points = db.IntField(required=True)
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    workouts = db.ListField(db.ReferenceField('Workout', reverse_delete_rule=db.PULL))
    roles = db.ListField()
    team = db.StringField()

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

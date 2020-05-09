from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Workout(db.Document):
    name = db.StringField(required=True, unique=True)
    points = db.IntField(required=True)
    exercises = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')


class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    workouts = db.ListField(db.ReferenceField('Workout', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Workout, 'added_by', db.CASCADE)

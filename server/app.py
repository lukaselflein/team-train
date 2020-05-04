import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

ex_max = [{'name': 'Warmup', 'quantity': 1},
          {'name': 'Pullups', 'quantity': 10},
          {'name': 'Pushups', 'quantity': 10},
          {'name': 'Pause', 'quantity': 1},
          {'name': 'Pullups', 'quantity': 10},
          {'name': 'Pushups', 'quantity': 10},
          {'name': 'Pause', 'quantity': 1},
          {'name': 'Pullups', 'quantity': 10},
          {'name': 'Pushups', 'quantity': 10},
        ]
          
ex_sprint = [
          {'name': 'Warmup', 'quantity': 300},
          {'name': 'Medium Speed', 'quantity': 60},
          {'name': 'Slow Speed', 'quantity': 120},
          {'name': 'Maximum Speed', 'quantity': 15},
          {'name': 'Slow Speed', 'quantity': 60},
          {'name': 'Maximum Speed', 'quantity': 15},
          {'name': 'Slow Speed', 'quantity': 60},
          {'name': 'Maximum Speed', 'quantity': 15},
          {'name': 'Slow Speed', 'quantity': 60},
          {'name': 'Cooldown', 'quantity': 300},
          {'name': 'Stretching', 'quantity': 300}
        ]

WORKOUTS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Max Strength',
        'points': 20,
        'exercises': ex_max,
        'unit': 'Repetitions',
        'trainer': 'Bubu',
        'done': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Interval-Sprints',
        'points': 25,
        'exercises': ex_sprint,
        'unit': 'Seconds',
        'trainer': 'Linus',
        'done': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'HIIT-Core',
        'points': 20,
        'exercises': ex_sprint,
        'unit': 'Seconds',
        'trainer': 'Lu',
        'done': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Long run',
        'points': 15,
        'exercises': ex_sprint,
        'unit': 'Seconds',
        'trainer': 'Linus',
        'done': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_workout(workout_id):
    for workout in WORKOUTS:
        if workout['id'] == workout_id:
            WORKOUTS.remove(workout)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/workouts', methods=['GET', 'POST'])
def all_workouts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        WORKOUTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'points': post_data.get('points'),
            'trainer': post_data.get('trainer'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Plan added!'
    else:
        response_object['workouts'] = WORKOUTS
    return jsonify(response_object)


@app.route('/workouts/<workout_id>', methods=['PUT', 'DELETE'])
def single_workout(workout_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_workout(workout_id)
        WORKOUTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'points': post_data.get('points'),
            'trainer': post_data.get('trainer'),
            'done': post_data.get('done')
        })
        response_object['message'] = 'Plan updated!'
    if request.method == 'DELETE':
        remove_workout(workout_id)
        response_object['message'] = 'Plan removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()

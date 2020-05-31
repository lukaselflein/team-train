import json

from tests.BaseCase import BaseCase

class TestWorkoutCreation(BaseCase):

    def test_workout_creation(self):
        # Given
        payload = json.dumps({
            "email": "unit_test_email@test.com",
            "password": "unit_test_password",
            "username": "unit_test_username"
        })

        self.app.post('/signup', 
                      headers={"Content-Type": "application/json"}, 
                      data=payload)

        login_response = self.app.post('/login', 
                                       headers={"Content-Type": "application/json"}, 
                                       data=payload)
        login_token = login_response.json['token']

        workout_payload = {
            "name": "Automated Testing Workout",
            "points": 1234,
            "exercises": [{
                                "name": "Pushups",
                                "quantity": 100
                           },
                           {
                               "name": "Situps",
                               "quantity": 100
                           },
                           {
                               "name": "Squats",
                               "quantity": 100
                           }
                         ],        
        }
        # When
        response = self.app.post('/workouts',
                                 headers={"Content-Type": "application/json", 
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(workout_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

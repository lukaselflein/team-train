import json

from tests.BaseCase import BaseCase

class TestMovieCreation(BaseCase):

    def test_movie_creation(self):
        # Given
        payload = json.dumps({
            "email": "unit_test_email@test.com",
            "password": "unit_test_password"
        })

        self.app.post('/api/auth/signup', 
                      headers={"Content-Type": "application/json"}, 
                      data=payload)

        login_response = self.app.post('/api/auth/login', 
                                       headers={"Content-Type": "application/json"}, 
                                       data=payload)
        login_token = login_response.json['token']

        movie_payload = {
            "name": "Star Wars: The Rise of Skywalker 2",
            "casts": ["Daisy Ridley", "Adam Driver"],
            "genres": ["Fantasy", "Sci-fi"]
        
        }
        # When
        response = self.app.post('/api/movies',
                                 headers={"Content-Type": "application/json", 
                                          "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(movie_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

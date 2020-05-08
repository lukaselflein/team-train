import unittest
import json

from app import app

from tests.BaseCase import BaseCase


class LoginTest(BaseCase):

    def test_successful_login(self):
        # Given
        payload = json.dumps({
            "email": "unit_test_email@test.com",
            "password": "unit_test_password"
        })

        response = self.app.post('/api/auth/signup', 
                                 headers={"Content-Type": "application/json"}, 
                                 data=payload)

        # When
        response = self.app.post('/api/auth/login', 
                                 headers={"Content-Type": "application/json"}, 
                                 data=payload)
        # Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

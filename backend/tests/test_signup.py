import unittest
import json

from app import app

from tests.BaseCase import BaseCase


class SignupTest(BaseCase):

    def test_successful_signup(self):
        # Given
        payload = json.dumps({
            "email": "unit_test_email@test.com",
            "password": "unit_test_password"
        })

        # When
        response = self.app.post('/signup', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

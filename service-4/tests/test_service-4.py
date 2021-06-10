from flask import url_for
from flask_testing import TestCase

from app import app, Hint

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_get_hint(TestBase):
    def test_get_hint(self):
        expected_region = "Europe"
        response = self.client.post(url_for('Hint', json=[51,0]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_region)
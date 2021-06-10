from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_get_hint(TestBase):
    def test_get_hint(self):
        response = self.client.post(url_for('Hint'), json={'x':51, 'y':0})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Europe", response.data.decode("utf-8"))
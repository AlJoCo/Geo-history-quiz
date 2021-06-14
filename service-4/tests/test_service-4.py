from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_get_hint(TestBase):
    def test_get_hint(self):
        response = self.client.post(url_for('Hint'), json={'x':90, 'y':140})
        self.assertIn("Orbit", response.data.decode("utf-8"))

        response = self.client.post(url_for('Hint'), json={'x':35, 'y':140})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Asia & Oceania", response.data.decode("utf-8"))

        response = self.client.post(url_for('Hint'), json={'x':80, 'y':140})
        self.assertIn("The Arctic", response.data.decode("utf-8"))

        response = self.client.post(url_for('Hint'), json={'x':-65, 'y':140})
        self.assertIn("Antarctica", response.data.decode("utf-8"))

        response = self.client.post(url_for('Hint'), json={'x':51, 'y':0})
        self.assertIn("Europe", response.data.decode("utf-8"))

        response = self.client.post(url_for('Hint'), json={'x':40, 'y':-140})
        self.assertIn("The Americas", response.data.decode("utf-8"))

        response = self.client.post(url_for('Hint'), json={'x':32, 'y':0})
        self.assertIn("Africa & Middle East", response.data.decode("utf-8"))
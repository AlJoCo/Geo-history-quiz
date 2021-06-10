from flask import Flask, url_for
from flask_testing import TestCase

from app import app, z

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_get_coords(TestBase):
    def test_get_coords(self):
        response = self.client.get(url_for('coords'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json,z)
from flask import url_for
from flask_testing import TestCase

from app import app, Date

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_get_date(TestBase):
    def test_get_date(self):
        response = self.client.get(url_for('Date'))
        self.assertEqual(response.status_code, 200)        
        self.assertTrue(response.json >=-2000 and response.json <= 2000)
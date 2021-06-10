from flask import url_for
from flask_testing import TestCase

from service-3.app import app, date

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_get_date(TestBase):
    def test_get_date(self):
        response = self.client.get(url_for('date'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.json,date)
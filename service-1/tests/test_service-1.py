from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_Home():
        with requests_mock.Mocker() as mocker:
            mocker.get('http://service-2:5000/get_coords', json=[51,0])
            mocker.get('http://service-3:5000/get_date', json=2000)
            mocker.post('http://service-4:5000/get_hint', test='Europe')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'You are at co-ordinates: 51,0 in the year 2000.', response.data)
            self.assertIn(b"(Hint: it's in Europe!)", response.data)
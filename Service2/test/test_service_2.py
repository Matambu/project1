from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestName(TestBase):
    def test_cal_kestis(self):
        with patch('random.choices') as r:
            r.return_value = 0
            response = self.client.get(url_for('name'))
            self.assertIn(b'Cal Kestis', response.data)

class TestName(TestBase):
    def test_ahsoka_tano(self):
        with patch('random.choices') as r:
            r.return_value = 1
            response = self.client.get(url_for('name'))
            self.assertIn(b'Ahsoka Tano', response.data)

    def test_shaak_Ti(self):
        with patch('random.choices') as r:
            r.return_value = 2
            response = self.client.get(url_for('name'))
            self.assertIn(b'Shaak-Ti', response.data)


    def test_grandinquisitor(self):
        with patch('random.choices') as r:
            r.return_value = 4
            response = self.client.get(url_for('name'))
            self.assertIn(b'Grand Inquisitor', response.data)
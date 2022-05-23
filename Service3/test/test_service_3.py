from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app



class TestBase(TestCase):
    def create_app(self):
        return app

class TestPlanet(TestBase):
    def test_coruscant(self):
        with patch('random.choices') as r:
            r.return_value = 0
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Coruscant', response.data)

class TestPlanet(TestBase):
    def test_kashyyyk(self):
        with patch('random.choices') as r:
            r.return_value = 1
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Kashyyyk', response.data)

    def test_shilli(self):
        with patch('random.choices') as r:
            r.return_value = 2
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Shilli', response.data)


    def test_kamino(self):
        with patch('random.choices') as r:
            r.return_value = 3
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Kamino', response.data)

    def test_ryloth(self):
        with patch('random.choices') as r:
            r.return_value = 4
            response = self.client.get(url_for('planet'))
            self.assertIn(b'Ryloth', response.data)

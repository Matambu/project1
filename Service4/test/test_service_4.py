from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDatabank(TestBase):
    def databank_10(self):
        response = self.client.post(url_for('databank'), data = 'Cal Kestis, Coruscant')
        self.assertIn(b'Cal Kestis Coruscant', response.data)

    def databank_1(self):
        response = self.client.post(url_for('databank'), data = 'Ahsoka Tano, Shilli')
        self.assertIn(b'Ahsoka Tano Shilli', response.data)

    def databank_2(self):
        response = self.client.post(url_for('databank'), data = 'Obi-Wan Kenobi, Kashyyyk')
        self.assertIn(b'Kashyyyk Obi-Wan', response.data)

    def databank_3(self):
        response = self.client.post(url_for('databank'), data = 'Grand Inquisitor, Kamino')
        self.assertIn(b'Grand Inquisitor Kamino', response.data)

    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Kylo Ren, Ryloth')
        self.assertIn(b'Kylo Ren Ryloth', response.data)

    def databank_5(self):
        response = self.client.post(url_for('databank'), data = 'Galen Marek ,Tatooine')
        self.assertIn(b'Galen Marek Tatooine', response.data)


    def databank_6(self):
        response = self.client.post(url_for('databank'), data = 'Darth Bane, Naboo')
        self.assertIn(b'Darth Bane Naboo', response.data)
    
    def databank_7(self):
        response = self.client.post(url_for('databank'), data = 'Bail Organa, Bespin')
        self.assertIn(b'Bail Organa Bespin', response.data)
    
    def databank_8(self):
        response = self.client.post(url_for('databank'), data = 'R2-D2, Dagobah')
        self.assertIn(b'R2-D2 Dagobah', response.data)
    
    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shaak-Ti , Hoth')
        self.assertIn(b'Shaak-Ti Hoth', response.data)

    
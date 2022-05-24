from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestDatabank(TestBase):
    def databank_1(self):
        response = self.client.post(url_for('databank'), data = 'Cal Kestis, Coruscant')
        self.assertIn(b'Cal Kestis Coruscant', response.data)

    def databank_2(self):
        response = self.client.post(url_for('databank'), data = 'Cal Kestis, Tatooine')
        self.assertIn(b'Cal Kestis Tatooine', response.data)
    
    def databank_3(self):
        response = self.client.post(url_for('databank'), data = 'Cal Kestis, Kamino')
        self.assertIn(b'Cal Kestis Kamino', response.data)
    
    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Cal Kestis, Ryloth')
        self.assertIn(b'Cal Kestis Ryloth', response.data)
    
    def databank_5(self):
        response = self.client.post(url_for('databank'), data = 'Cal Kestis, Shilli')
        self.assertIn(b'Cal Kestis Shilli', response.data)

    def databank_6(self):
        response = self.client.post(url_for('databank'), data = 'Ahsoka Tano, Shilli')
        self.assertIn(b'Ahsoka Tano Shilli', response.data)
    
    def databank_6(self):
        response = self.client.post(url_for('databank'), data = 'Ahsoka Tano, Tatooine')
        self.assertIn(b'Ahsoka Tano Tatooine', response.data)
    
    def databank_6(self):
        response = self.client.post(url_for('databank'), data = 'Ahsoka Tano, Coruscant')
        self.assertIn(b'Ahsoka Tano Coruscant', response.data)

    def databank_6(self):
        response = self.client.post(url_for('databank'), data = 'Ahsoka Tano, Kamino')
        self.assertIn(b'Ahsoka Tano Kamino', response.data)

    def databank_6(self):
        response = self.client.post(url_for('databank'), data = 'Ahsoka Tano, Kashyyyk')
        self.assertIn(b'Ahsoka Tano Kashyyyk', response.data)

    def databank_8(self):
        response = self.client.post(url_for('databank'), data = 'Grand Inquisitor, Kamino')
        self.assertIn(b'Grand Inquisitor Kamino', response.data)
    
    def databank_8(self):
        response = self.client.post(url_for('databank'), data = 'Grand Inquisitor, Tatooine')
        self.assertIn(b'Grand Inquisitor Tatooine', response.data)

    def databank_8(self):
        response = self.client.post(url_for('databank'), data = 'Grand Inquisitor, Coruscant')
        self.assertIn(b'Grand Inquisitor Coruscant', response.data)

    def databank_8(self):
        response = self.client.post(url_for('databank'), data = 'Grand Inquisitor, Ryloth')
        self.assertIn(b'Grand Inquisitor Ryloth', response.data)

    def databank_8(self):
        response = self.client.post(url_for('databank'), data = 'Grand Inquisitor, Shilli')
        self.assertIn(b'Grand Inquisitor Shilli', response.data)

    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Kylo Ren, Ryloth')
        self.assertIn(b'Kylo Ren Ryloth', response.data)
    
    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Kylo Ren, Shilli')
        self.assertIn(b'Kylo Ren Shilli', response.data)

    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Kylo Ren, Tatooine')
        self.assertIn(b'Kylo Ren Tatooine', response.data)
    
    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Kylo Ren, Coruscant')
        self.assertIn(b'Kylo Ren Coruscant', response.data)
    
    def databank_4(self):
        response = self.client.post(url_for('databank'), data = 'Kylo Ren, Kamino')
        self.assertIn(b'Kylo Ren Ryloth', response.data)


    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shaak-Ti , Tatooine')
        self.assertIn(b'Shaak-Ti Tatooine', response.data)
    
    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shaak-Ti , Coruscant')
        self.assertIn(b'Shaak-Ti Coruscant', response.data)
    
    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shaak-Ti , Kamino')
        self.assertIn(b'Shaak-Ti Kamino', response.data)
    
    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shaak-Ti , Ryloth')
        self.assertIn(b'Shaak-Ti Ryloth', response.data)

    def databank_9(self):
        response = self.client.post(url_for('databank'), data = 'Shaak-Ti , Shilli')
        self.assertIn(b'Shaak-Ti Shilli', response.data)
    

    
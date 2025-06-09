import unittest
from app import app

class SaludoApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_saludo_default(self):
        response = self.app.get('/saludo')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['mensaje'], 'hola  desde la API de Python')

    def test_saludo_con_cadena(self):
        response = self.app.get('/saludo?cadena=Platzi')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['mensaje'], 'hola Platzi desde la API de Python')

if __name__ == '__main__':
    unittest.main()
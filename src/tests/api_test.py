
from main import app
import sys
import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient
sys.path.append('..')

client = TestClient(app)


class TestApi(unittest.TestCase):

    def test_get_sensors(self):
        response = client.get("/sensors")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_get_sensors_ha(self):
        response = client.get("/sensors/ha")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_get_automations(self):
        response = client.get("/automations")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])


if __name__ == '__main__':
    unittest.main()

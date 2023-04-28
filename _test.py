import unittest
from database import DatabaseConnector

class TestDatabaseConnection(unittest.TestCase):

    def test_getSensors(self):
        databaseConnector = DatabaseConnector("test.db")
        sensors = databaseConnector.getSensors()

        self.assertEqual(len(sensors),2)        
        self.assertEqual(sensors[0].id,1)
        self.assertEqual(sensors[0].haSensorId,"test-sensor-1")

if __name__ == '__main__':
    unittest.main()
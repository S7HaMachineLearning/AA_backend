import unittest
from database import DatabaseConnector

class TestDatabaseConnection(unittest.TestCase):

    def test_getSensors(self):
        databaseConnector = DatabaseConnector("tests/test.db")
        sensors = databaseConnector.get_sensors()

        self.assertEqual(len(sensors), 2)
        self.assertEqual(sensors[0].id, 1)
        self.assertEqual(sensors[0].haSensorId, "test-sensor-1")

    def test_getAutomations(self):
        databaseConnector = DatabaseConnector("tests/test.db")
        automations = databaseConnector.get_automations()

        self.assertEqual(len(automations), 2)
        self.assertEqual(automations[0].id, 1)
        self.assertEqual(automations[0].value, "test-automation-1")
        


if __name__ == '__main__':
    unittest.main()

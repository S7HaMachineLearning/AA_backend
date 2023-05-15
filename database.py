"""Database service"""
from datetime import datetime
import sqlite3
import models


class DatabaseConnector:
    """Database connector class"""
    database_name = ""

    def __init__(self, database_name):
        self.database_name = database_name

    # Get sensor data from database
    def get_sensors(self) -> list[models.Sensor]:
        """Get list of all sensors from database."""
        try:

            # Get all sensors
            rows = self.execute_fetch_all(
                "SELECT * FROM sensors WHERE deleted = 0")

            # Create return list
            ret = []
            for row in rows:
                print(row)
                sensor = models.Sensor(
                    id=row[0],
                    haSensorId=row[1],
                    type=row[2],
                    createdOn=row[3],
                    updatedOn=row[4],
                    deleted=row[5],
                    friendlyName=row[6]
                )
                print(sensor)
                ret.append(sensor)

            return ret
        except sqlite3.Error as err:
            print(err)
            return []

    def add_sensor(self, sensor: models.NewSensor) -> int:
        """Add sensor to database"""
        newId = 0
        try:
            # Add sensor to database
            newId = self.execute_insert("INSERT INTO sensors (haSensorId, friendlyName, type, createdOn, updatedOn)" +
                                        " VALUES (?, ?, ?, ?, ?);",
                                        (
                                            sensor.haSensorId,
                                            sensor.friendlyName,
                                            sensor.type,
                                            datetime.now(),
                                            datetime.now(),
                                        )
                                        )
        except sqlite3.Error as err:
            print(err)
        return newId

    # Open local database and get data

    def execute_fetch_all(self, query: str):
        """Execute query and return all rows."""
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        result = cursor.execute(query)
        rows = result.fetchall()
        connection.close()
        return rows

    def execute_insert(self, query: str, params):
        """Execute query and insert row."""
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()

        # Get last inserted row id
        result = cursor.execute("select last_insert_rowid()")
        new_id = result.fetchone()[0]

        connection.close()
        return int(new_id)

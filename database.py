"""Database service"""
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
            rows = self.execute_fetch_all("SELECT * FROM sensors WHERE deleted = 0")

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
                    deleted=row[5]
                )
                print(sensor)
                ret.append(sensor)

            return ret
        except sqlite3.Error as err:
            print(err)
            return []

    # Open local database and get data
    def execute_fetch_all(self, query: str):
        """Execute query and return all rows."""
        con = sqlite3.connect(self.database_name)
        cur = con.cursor()
        res = cur.execute(query)
        rows = res.fetchall()
        con.close()
        return rows

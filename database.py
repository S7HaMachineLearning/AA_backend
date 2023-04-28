import sqlite3
import models


class DatabaseConnector:
    databaseName = ""

    def __init__(self, databaseName):
        self.databaseName = databaseName

    # Get sensor data from database
    def getSensors(self) -> list[models.Sensor]:
        try:

            # Get all sensors
            rows = self.__executeFetchall("SELECT * FROM sensors WHERE deleted = 0")

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
        except Exception as e:
            print(e)
            return []

    # Open local database and get data
    def __executeFetchall(self, query: str):
        con = sqlite3.connect(self.databaseName)
        cur = con.cursor()
        res = cur.execute(query)
        rows = res.fetchall()
        con.close()
        return rows

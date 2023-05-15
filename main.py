"""Main file for the API. Contains all endpoints and the main function."""
from json import JSONDecodeError
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import DatabaseConnector
import models
from ha_api import HomeAssistantApi

# Create database connector for local DB
databaseConnector = DatabaseConnector("database.db")
haApi = HomeAssistantApi()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## API ENDPOINTS ##

@app.get("/sensors", response_model=list[models.Sensor])
def getShit() -> list[models.Sensor]:
    objects = databaseConnector.get_sensors()
    return objects


@app.get("/sensors/ha", response_model=list[models.HaSensor])
def get_ha_sensors() -> list[models.HaSensor]:
    """Get list of all sensors from Home Assistant."""
    # Get sensor from HA
    sensors = haApi.get_states()
    return sensors

@app.post("/sensors")
async def main(request: Request):
    """Add sensor to database."""
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'
    elif content_type == 'application/json':
        try:
            json = await request.json()
            # Parse to NewSensor
            sensor = models.NewSensor(
                haSensorId=json['haSensorId'],
                friendlyName=json['friendlyName'],
                type=json['type']
            )
            newId = databaseConnector.add_sensor(sensor)
            return newId
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'
    
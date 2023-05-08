"""Main file for the API. Contains all endpoints and the main function."""
from fastapi import FastAPI
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

@app.get("/sensors")
def get_sensors() -> dict[str, dict[int, models.Sensor]]:
    """Get list of all sensors from database."""

    # Get sensor from database
    sensors = databaseConnector.get_sensors()

    # Create Return list
    ret = dict[int, models.Sensor]()
    for index, item in enumerate(sensors):
        ret[index] = item

    return {"sensors": ret}


@app.get("/sensors/ha")
def get_ha_sensors() :
    """Get list of all sensors from Home Assistant."""

    # Get sensor from HA
    sensors = haApi.get_states()

    return {"sensors": sensors}

@app.post("/sensors")
def add_sensor(sensor: models.Sensor):
    """Add sensor to database."""

    # Add sensor to database
    sensor = databaseConnector.add_sensor(sensor)

    print(sensor)
    return {"sensor": sensor}

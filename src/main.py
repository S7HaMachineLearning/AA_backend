"""Main file for the API. Contains all endpoints and the main function."""
from json import JSONDecodeError
from fastapi import FastAPI, HTTPException, Request
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
def get_sensors() -> list[models.Sensor]:
    """Get list of all sensors from database."""
    objects = databaseConnector.get_sensors()
    return objects


@app.get("/sensors/ha", response_model=list[models.HaSensor])
def get_ha_sensors() -> list[models.HaSensor]:
    """Get list of all sensors from Home Assistant."""
    # Get sensor from HA
    sensors = haApi.get_states()
    return sensors


@app.post("/sensors")
async def post_sensor(request: Request):
    """Add sensor to database."""
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'

    if content_type == 'application/json':
        try:
            json = await request.json()
            # Parse to NewSensor
            sensor = models.NewSensor(
                haSensorId=json['haSensorId'],
                friendlyName=json['friendlyName'],
                type=json['type']
            )

            # Check if HaSensor exists
            if databaseConnector.check_ha_sensor(sensor.haSensorId):
                return databaseConnector.add_sensor(sensor)

            raise HTTPException(
                status_code=409, detail="Sensor with same haSensorId already exists")
        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'


@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: int):
    """Delete sensor from database."""
    return databaseConnector.delete_sensor(sensor_id)


@app.get("/automations", response_model=list[models.Automation])
def get_automations() -> list[models.Automation]:
    """Get list of all automation's from database."""
    objects = databaseConnector.get_automations()
    return objects


@app.post("/automations")
async def post_automation(request: Request):
    """Add automation to database."""
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'

    if content_type == 'application/json':
        try:
            json = await request.json()

            #Parse to NewAutomation
            automation = models.NewAutomation(
                value=json['value']
            )

            # Check if HaSensor exists
            return databaseConnector.add_automation(automation)

        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'

@app.patch("/automations/{automation_id}")
async def patch_automation_status(request: Request, automation_id: int):
    """Update automation in database."""
    content_type = request.headers.get('Content-Type')
    if content_type is None:
        return 'No Content-Type provided.'

    if content_type == 'application/json':
        try:
            json = await request.json()

            #Parse to NewAutomation
            update = models.UpdateAutomation(
                status=json['status']
            )

            # Check if HaSensor exists
            return databaseConnector.update_automation(automation_id,update)

        except JSONDecodeError:
            return 'Invalid JSON data.'
    else:
        return 'Content-Type not supported.'
    
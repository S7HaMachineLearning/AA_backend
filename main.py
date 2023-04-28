from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import DatabaseConnector
import models

# Create database connector for local DB
databaseConnector = DatabaseConnector("database.db")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins= [ "*" ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



## API ENDPOINTS ##

# Get list of all sensors from database
@app.get("/sensors")
def getSensors() -> dict[str, dict[int, models.Sensor]]:
    
    # Get sensor from database
    sensors = databaseConnector.getSensors()

    # Create Return list
    ret =  dict[int, models.Sensor]()
    for index, item in enumerate(sensors):
        ret[index] = item

    return {"sensors": ret}

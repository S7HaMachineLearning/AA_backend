from enum import Enum
from pydantic import BaseModel

class SensorType(Enum):
    TEMPERATURE = 1
    HUMIDITY = 2

class Sensor(BaseModel):
    id: int
    haSensorId: str
    type: SensorType	
    createdOn : int
    updatedOn : int
    deleted: int

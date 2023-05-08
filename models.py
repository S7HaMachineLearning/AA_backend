"""Models for the application."""

from enum import Enum
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class SensorType(Enum):  # pylint: disable=too-few-public-methods
    """Enum for sensor types."""
    TEMPERATURE = 1
    HUMIDITY = 2


class Sensor(BaseModel):  # pylint: disable=too-few-public-methods
    """Sensor model."""
    id: int
    haSensorId: str
    type: SensorType
    createdOn: str
    updatedOn: str
    deleted: int


class HaSensor(BaseModel):  # pylint: disable=too-few-public-methods
    """Home assistant sensor model."""
    entity_id: str
    friendly_name: str
    state: str

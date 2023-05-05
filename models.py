"""Models for the application."""

from enum import Enum
from pydantic import BaseModel # pylint: disable=no-name-in-module


class SensorType(Enum): # pylint: disable=too-few-public-methods
    """Enum for sensor types."""
    TEMPERATURE = 1
    HUMIDITY = 2


class Sensor(BaseModel): # pylint: disable=too-few-public-methods
    """Sensor model."""
    id: int
    haSensorId: str
    type: SensorType
    createdOn: int
    updatedOn: int
    deleted: int

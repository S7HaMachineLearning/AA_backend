"""Models for the application."""

from enum import Enum
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class SensorType(Enum):  # pylint: disable=too-few-public-methods
    """Enum for sensor types."""
    TEMPERATURE = 1
    HUMIDITY = 2


class FeedbackType(Enum):  # pylint: disable=too-few-public-methods
    """Enum for feedback types."""
    NEW = 0
    ACCEPTED = 1
    DECLINED_GOOD = 2
    DECLINED_BAD = 3


class Sensor(BaseModel):  # pylint: disable=too-few-public-methods
    """Sensor model."""
    id: int
    friendlyName: str
    haSensorId: str
    type: SensorType
    createdOn: str
    updatedOn: str
    deleted: int


class NewSensor(BaseModel):  # pylint: disable=too-few-public-methods
    """New sensor model."""
    friendlyName: str
    haSensorId: str
    type: int


class HaSensor(BaseModel):  # pylint: disable=too-few-public-methods
    """Home assistant sensor model."""
    entityId: str
    friendlyName: str
    state: str


class Automation(BaseModel):  # pylint: disable=too-few-public-methods
    """Automation model."""
    id: int
    value: str
    status: FeedbackType
    createdOn: str
    updatedOn: str
    deleted: int


class NewAutomation(BaseModel):  # pylint: disable=too-few-public-methods
    """New automation model."""
    value: str

class UpdateAutomation(BaseModel):  # pylint: disable=too-few-public-methods
    """Update automation model."""
    status: int

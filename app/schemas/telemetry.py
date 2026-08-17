from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TelemetryIn(BaseModel):
    vehicle_id: str
    timestamp: datetime
    lat: float
    long: float
    alt = Optional[float] = None
    speed = Optional[float] = None
    course = Optional[float] = None
    sats = Optional[float] = None
    hdop = Optional[float] = None
    igntion = bool = False
    aspa_active = bool = False
    battery_voltage = Optional[float] = None
    battery_current_ma = Optional[float] = None
    alert = Optional[str] = None


class TelemetryOut(BaseModel):
    vehicle_id: str
    timestamp: datetime
    lat: float
    long: float
    alt = Optional[float] = None
    speed = Optional[float] = None
    course = Optional[float] = None
    sats = Optional[float] = None
    hdop = Optional[float] = None
    igntion = bool = False
    aspa_active = bool = False
    battery_voltage = Optional[float] = None
    battery_current_ma = Optional[float] = None
    alert = Optional[str] = None

    class Config:
        from_attributes = True

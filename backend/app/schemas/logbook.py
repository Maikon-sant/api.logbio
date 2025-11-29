from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import date

BioLevel = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]

class LogbookCreate(BaseModel):
    ship_id: int
    date: date
    biofouling_level: BioLevel = Field(..., description="LOW|MEDIUM|HIGH|CRITICAL")
    image_url: Optional[str] = None
    idle_days: int
    fuel_consumption: float
    velocity: float
    water_temp: float
    salinity: float

class LogbookOut(LogbookCreate):
    id: int
    class Config:
        from_attributes = True

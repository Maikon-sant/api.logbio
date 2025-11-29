from pydantic import BaseModel
from typing import Optional
from datetime import date

class ShipBase(BaseModel):
    name: str
    type: str
    last_cleaning_date: Optional[date] = None
    coating_type: Optional[str] = None

class ShipCreate(ShipBase):
    pass

class ShipOut(ShipBase):
    id: int
    class Config:
        from_attributes = True

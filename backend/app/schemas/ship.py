from pydantic import BaseModel
from typing import List, Optional

class ShipBase(BaseModel):
    name: str
    imo: str
    ship_class: Optional[str] = None

class ShipCreate(ShipBase):
    pass

class Ship(ShipBase):
    id: int

    class Config:
        from_attributes = True

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LogbookBase(BaseModel):
    ship_id: int
    description: str
    date: Optional[datetime] = None

class LogbookCreate(LogbookBase):
    pass

class Logbook(LogbookBase):
    id: int
    date: datetime

    class Config:
        from_attributes = True

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LogbookBase(BaseModel):
    ship_id: int
    session_id: Optional[str] = None
    event_name: str
    start_date: datetime
    end_date: Optional[datetime] = None
    duration: Optional[float] = 0.0
    distance: Optional[float] = 0.0
    
    aft_draft: Optional[float] = 0.0
    fwd_draft: Optional[float] = 0.0
    mid_draft: Optional[float] = 0.0
    trim: Optional[float] = 0.0
    displacement: Optional[float] = 0.0
    
    beaufort_scale: Optional[str] = None
    sea_condition: Optional[str] = None
    beaufort_scale_desc: Optional[str] = None
    sea_condition_desc: Optional[str] = None
    
    speed: Optional[float] = 0.0
    speed_gps: Optional[float] = 0.0
    port: Optional[str] = None
    
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class LogbookCreate(LogbookBase):
    pass

class Logbook(LogbookBase):
    id: int

    class Config:
        from_attributes = True

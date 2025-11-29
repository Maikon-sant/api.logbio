from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Logbook(Base):
    __tablename__ = "logbooks"

    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, ForeignKey("ships.id"))
    
    session_id = Column(String, index=True)
    event_name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    duration = Column(Float)
    distance = Column(Float)
    
    aft_draft = Column(Float)
    fwd_draft = Column(Float)
    mid_draft = Column(Float)
    trim = Column(Float)
    displacement = Column(Float)
    
    beaufort_scale = Column(String)
    sea_condition = Column(String)
    beaufort_scale_desc = Column(String)
    sea_condition_desc = Column(String)
    
    speed = Column(Float)
    speed_gps = Column(Float)
    port = Column(String)
    
    latitude = Column(Float)
    longitude = Column(Float)
    
    # Relacionamento com Ship
    ship = relationship("Ship", back_populates="logbooks")

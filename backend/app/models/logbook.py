from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Logbook(Base):
    __tablename__ = "logbooks"

    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, ForeignKey("ships.id"))
    date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    description = Column(String)
    
    # Relacionamento com Ship
    ship = relationship("Ship", back_populates="logbooks")

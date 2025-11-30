from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    imo = Column(String, unique=True, index=True)
    
    # Relacionamento com Logbook
    logbooks = relationship("Logbook", back_populates="ship")

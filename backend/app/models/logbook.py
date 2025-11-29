from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from ..database import Base

class Logbook(Base):
    __tablename__ = "logbooks"
    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, ForeignKey("ships.id"), nullable=False)
    date = Column(Date, nullable=False)
    biofouling_level = Column(String, nullable=False)
    image_url = Column(String, nullable=True)
    idle_days = Column(Integer, nullable=False)
    fuel_consumption = Column(Float, nullable=False)
    velocity = Column(Float, nullable=False)
    water_temp = Column(Float, nullable=False)
    salinity = Column(Float, nullable=False)

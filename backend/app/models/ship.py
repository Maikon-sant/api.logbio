from sqlalchemy import Column, Integer, String, Date
from ..database import Base

class Ship(Base):
    __tablename__ = "ships"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    last_cleaning_date = Column(Date, nullable=True)
    coating_type = Column(String, nullable=True)

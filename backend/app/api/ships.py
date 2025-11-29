from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db, Base, engine
from ..models.ship import Ship
from ..schemas.ship import ShipOut

# Garante criação de tabelas
Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/ships", response_model=list[ShipOut])
def list_ships(db: Session = Depends(get_db)):
    return db.query(Ship).all()

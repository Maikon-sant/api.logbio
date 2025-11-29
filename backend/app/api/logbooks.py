from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db, Base, engine
from ..models.logbook import Logbook
from ..models.ship import Ship
from ..schemas.logbook import LogbookCreate

# Garante criação de tabelas
Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/logbooks")
def create_logbook(payload: LogbookCreate, db: Session = Depends(get_db)):
    # valida ship
    ship = db.query(Ship).filter(Ship.id == payload.ship_id).first()
    if not ship:
        raise HTTPException(status_code=400, detail="ship_id inválido")

    log = Logbook(**payload.dict())
    db.add(log)
    db.commit()
    db.refresh(log)
    return {"id": log.id}

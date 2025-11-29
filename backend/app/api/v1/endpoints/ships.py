from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api import deps
from app.models import ship as models
from app.schemas import ship as schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Ship])
def read_ships(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve ships.
    """
    ships = db.query(models.Ship).offset(skip).limit(limit).all()
    return ships

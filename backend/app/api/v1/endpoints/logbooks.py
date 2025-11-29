from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models import logbook as models
from app.schemas import logbook as schemas

router = APIRouter()

@router.post(
    "/",
    response_model=schemas.Logbook,
    summary="Criar registro de diário de bordo",
    description="Adiciona um novo registro manual ao diário de bordo de um navio específico.",
    response_description="O registro criado com ID e timestamp."
)
def create_logbook(
    logbook: schemas.LogbookCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Create a new logbook entry.
    """
    db_logbook = models.Logbook(
        ship_id=logbook.ship_id,
        description=logbook.description,
        date=logbook.date
    )
    db.add(db_logbook)
    db.commit()
    db.refresh(db_logbook)
    return db_logbook


@router.get("/", response_model=List[schemas.Logbook])
def read_logbooks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve logbooks.
    """
    logbooks = db.query(models.Logbook).offset(skip).limit(limit).all()
    return logbooks

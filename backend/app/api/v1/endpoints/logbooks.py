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
        session_id=logbook.session_id,
        event_name=logbook.event_name,
        start_date=logbook.start_date,
        end_date=logbook.end_date,
        duration=logbook.duration,
        distance=logbook.distance,
        aft_draft=logbook.aft_draft,
        fwd_draft=logbook.fwd_draft,
        mid_draft=logbook.mid_draft,
        trim=logbook.trim,
        displacement=logbook.displacement,
        beaufort_scale=logbook.beaufort_scale,
        sea_condition=logbook.sea_condition,
        beaufort_scale_desc=logbook.beaufort_scale_desc,
        sea_condition_desc=logbook.sea_condition_desc,
        speed=logbook.speed,
        speed_gps=logbook.speed_gps,
        port=logbook.port,
        latitude=logbook.latitude,
        longitude=logbook.longitude
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

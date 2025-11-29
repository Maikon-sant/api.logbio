"""
Endpoints relacionados à frota.
"""
from fastapi import APIRouter, HTTPException
from app.schemas.schemas import FleetOverview
from app.services.fleet_service import get_fleet_overview

router = APIRouter()


@router.get("/overview", response_model=FleetOverview)
async def get_fleet_overview():
    """
    Retorna a visão geral da frota com KPIs e histórico de performance.
    """
    try:
        return get_fleet_overview()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados da frota: {str(e)}")


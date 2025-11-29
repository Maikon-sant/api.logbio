"""
Endpoints relacionados à frota.
"""
from fastapi import APIRouter, HTTPException
from app.schemas.fleet import FleetOverview
from app.services.fleet_service import get_fleet_overview

router = APIRouter()


@router.get(
    "/overview",
    response_model=FleetOverview,
    summary="Obter visão geral da frota",
    description="Retorna dados agregados da frota, incluindo total de navios, eficiência média, KPIs principais e histórico de performance.",
    response_description="Objeto contendo estatísticas e dados históricos da frota."
)
async def read_fleet_overview():
    """
    Retorna a visão geral da frota com KPIs e histórico de performance.
    """
    try:
        return get_fleet_overview()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar dados da frota: {str(e)}")


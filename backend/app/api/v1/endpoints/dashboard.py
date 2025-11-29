"""
Endpoints relacionados ao dashboard de analytics.
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.schemas.schemas import DashboardMetrics, CriticalShip
from app.services.calculations import aggregate_fleet_metrics
from app.services.data_service import get_recent_logbooks

router = APIRouter()

# Preço padrão do combustível (em reais por tonelada)
# Em produção, isso viria de uma configuração ou API externa
DEFAULT_FUEL_PRICE = 3500.0  # R$ 3.500 por tonelada


@router.get("", response_model=DashboardMetrics)
async def get_dashboard_analytics(
    days: Optional[int] = Query(
        default=30,
        ge=1,
        le=365,
        description="Número de dias para analisar logbooks recentes"
    ),
    fuel_price: Optional[float] = Query(
        default=None,
        ge=0,
        description="Preço do combustível por tonelada (opcional, usa padrão se não fornecido)"
    )
):
    """
    Retorna métricas agregadas do dashboard baseadas em análises de logbooks.
    
    Este endpoint:
    - Busca logbooks recentes dos navios
    - Calcula riscos de bioincrustação usando heurísticas
    - Identifica navios críticos (risco >= 70)
    - Calcula desperdício de combustível e economia potencial
    - Retorna métricas consolidadas da frota
    """
    try:
        # Usar preço padrão se não fornecido
        fuel_price_per_ton = fuel_price if fuel_price is not None else DEFAULT_FUEL_PRICE
        
        # Buscar logbooks recentes
        logbooks = get_recent_logbooks(days=days)
        
        # Processar dados e agregar métricas
        metrics = aggregate_fleet_metrics(
            logbooks=logbooks,
            fuel_price=fuel_price_per_ton
        )
        
        # Converter para o schema Pydantic
        return DashboardMetrics(
            fleet_average_risk=metrics["fleet_average_risk"],
            critical_ships=[
                CriticalShip(**ship) for ship in metrics["critical_ships"]
            ],
            total_extra_fuel_tons=metrics["total_extra_fuel_tons"],
            total_savings_money=metrics["total_savings_money"],
            total_ships=metrics["total_ships"],
            risk_level=metrics["risk_level"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar analytics do dashboard: {str(e)}"
        )


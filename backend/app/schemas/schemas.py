"""
Schemas Pydantic para validação de dados de entrada e saída da API.
"""
from typing import List, Literal, Union
from pydantic import BaseModel


class KPIData(BaseModel):
    """Schema para dados de KPI."""
    id: str
    title: str
    value: Union[str, float]
    unit: str
    trend: Literal['up', 'down', 'neutral']
    trendValue: str
    status: Literal['success', 'warning', 'error', 'info']


class TimeSeriesPoint(BaseModel):
    """Schema para pontos de série temporal."""
    date: str  # ISO 8601 YYYY-MM-DD
    value: float
    type: Literal['historical', 'prediction']


class FleetOverview(BaseModel):
    """Schema para visão geral da frota."""
    totalShips: int
    activeShips: int
    averageEfficiency: float
    kpis: List[KPIData]
    performanceHistory: List[TimeSeriesPoint]


class PredictionParams(BaseModel):
    """Schema para parâmetros de previsão."""
    shipId: str
    routeId: str
    speed: float
    days: int


class PredictionResult(BaseModel):
    """Schema para resultado de previsão."""
    fuelConsumption: float
    biofoulingRisk: float
    maintenanceDate: str  # ISO 8601 YYYY-MM-DD
    chartData: List[TimeSeriesPoint]


class CriticalShip(BaseModel):
    """Schema para navio com risco crítico."""
    id: int
    name: str
    risk: int
    level: str


class DashboardMetrics(BaseModel):
    """Schema para métricas agregadas do dashboard."""
    fleet_average_risk: int
    critical_ships: List[CriticalShip]
    total_extra_fuel_tons: float
    total_savings_money: float
    total_ships: int
    risk_level: str


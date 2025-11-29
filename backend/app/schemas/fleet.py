from typing import List, Literal, Union
from pydantic import BaseModel
from app.schemas.common import TimeSeriesPoint

class KPIData(BaseModel):
    """Schema para dados de KPI."""
    id: str
    title: str
    value: Union[str, float]
    unit: str
    trend: Literal['up', 'down', 'neutral']
    trendValue: str
    status: Literal['success', 'warning', 'error', 'info']

class FleetOverview(BaseModel):
    """Schema para visão geral da frota."""
    totalShips: int
    activeShips: int
    averageEfficiency: float
    kpis: List[KPIData]
    performanceHistory: List[TimeSeriesPoint]

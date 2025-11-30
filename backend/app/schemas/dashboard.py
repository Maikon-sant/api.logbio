from typing import List
from pydantic import BaseModel

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

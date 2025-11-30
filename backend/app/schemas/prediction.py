from typing import List
from pydantic import BaseModel
from app.schemas.common import TimeSeriesPoint

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

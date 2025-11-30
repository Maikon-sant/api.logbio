from typing import Literal
from pydantic import BaseModel

class TimeSeriesPoint(BaseModel):
    """Schema para pontos de série temporal."""
    date: str  # ISO 8601 YYYY-MM-DD
    value: float
    type: Literal['historical', 'prediction']

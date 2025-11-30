"""
Roteador principal da API v1.
"""
from fastapi import APIRouter
from app.api.v1.endpoints import fleet, predictions, logbooks, ships, dashboard

api_router = APIRouter()

api_router.include_router(fleet.router, prefix="/fleet", tags=["fleet"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(logbooks.router, prefix="/logbooks", tags=["logbooks"])
api_router.include_router(ships.router, prefix="/ships", tags=["ships"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])


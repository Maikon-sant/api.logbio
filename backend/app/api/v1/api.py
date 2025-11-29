"""
Roteador principal da API v1.
"""
from fastapi import APIRouter
from app.api.v1.endpoints import fleet, predictions

api_router = APIRouter()

api_router.include_router(fleet.router, prefix="/fleet", tags=["fleet"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])


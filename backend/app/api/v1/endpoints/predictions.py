"""
Endpoints relacionados a previsões e insights.
"""
from fastapi import APIRouter, HTTPException
from app.schemas.schemas import PredictionParams, PredictionResult
from app.services.prediction_service import generate_prediction as generate_prediction_service

router = APIRouter()


@router.post(
    "/generate",
    response_model=PredictionResult,
    summary="Gerar previsão de bioincrustação",
    description="Calcula o risco de bioincrustação e o consumo estimado de combustível com base nos parâmetros da rota e do navio.",
    response_description="Resultados da previsão incluindo consumo, risco e gráficos."
)
async def generate_prediction(params: PredictionParams):
    """
    Gera previsões de consumo de combustível e risco de bioincrustação.
    """
    try:
        # Validações básicas
        if params.days <= 0:
            raise HTTPException(status_code=400, detail="O número de dias deve ser maior que zero")
        if params.speed <= 0:
            raise HTTPException(status_code=400, detail="A velocidade deve ser maior que zero")
        if params.speed > 30:
            raise HTTPException(status_code=400, detail="A velocidade não pode ser maior que 30 nós")
        
        return generate_prediction_service(params)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar previsão: {str(e)}")


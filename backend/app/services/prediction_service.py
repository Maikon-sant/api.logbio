"""
Serviço para lógica de negócio relacionada a previsões e insights.
"""
from datetime import datetime, timedelta
from typing import List
from app.schemas.schemas import PredictionParams, PredictionResult, TimeSeriesPoint


def generate_prediction(params: PredictionParams) -> PredictionResult:
    """
    Gera previsões de consumo de combustível e risco de bioincrustação.
    Em produção, isso usaria modelos de ML reais.
    """
    # Cálculos mockados baseados nos parâmetros
    # Fórmula simplificada: consumo = speed * days * factor
    base_consumption_per_day = 250.0  # toneladas por dia
    speed_factor = params.speed / 15.0  # Normalizado para 15 nós
    fuel_consumption = base_consumption_per_day * params.days * speed_factor
    
    # Risco de bioincrustação baseado em dias e velocidade
    # Velocidades menores aumentam o risco
    base_risk = 20.0
    days_factor = params.days * 0.8
    speed_risk_factor = max(0, (15 - params.speed) * 2)
    biofouling_risk = min(100, base_risk + days_factor + speed_risk_factor)
    
    # Data de manutenção sugerida (30 dias a partir de hoje)
    maintenance_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    
    # Gerar dados do gráfico para os próximos N dias
    chart_data: List[TimeSeriesPoint] = []
    today = datetime.now()
    
    for i in range(params.days):
        date = today + timedelta(days=i)
        # Simular eficiência decrescente ao longo do tempo (efeito da bioincrustação)
        base_efficiency = 87.5
        efficiency_decrease = (i * biofouling_risk) / (params.days * 100)
        value = max(70, base_efficiency - efficiency_decrease)
        
        chart_data.append(
            TimeSeriesPoint(
                date=date.strftime("%Y-%m-%d"),
                value=round(value, 1),
                type="prediction"
            )
        )
    
    return PredictionResult(
        fuelConsumption=round(fuel_consumption, 2),
        biofoulingRisk=round(biofouling_risk, 1),
        maintenanceDate=maintenance_date,
        chartData=chart_data
    )


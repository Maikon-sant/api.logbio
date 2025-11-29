"""
Serviço para lógica de negócio relacionada à frota.
"""
from datetime import datetime, timedelta
from typing import List
from app.schemas.fleet import FleetOverview, KPIData
from app.schemas.common import TimeSeriesPoint


def get_fleet_overview() -> FleetOverview:
    """
    Retorna a visão geral da frota com dados mockados.
    Em produção, isso viria de um banco de dados.
    """
    # Gerar histórico de performance dos últimos 30 dias
    performance_history: List[TimeSeriesPoint] = []
    today = datetime.now()
    
    for i in range(30, 0, -1):
        date = today - timedelta(days=i)
        # Simular valores históricos variando entre 80 e 90
        base_value = 85.5
        variation = (i % 7) * 0.5  # Variação semanal
        value = base_value + variation
        
        performance_history.append(
            TimeSeriesPoint(
                date=date.strftime("%Y-%m-%d"),
                value=round(value, 1),
                type="historical"
            )
        )
    
    # KPIs mockados
    kpis: List[KPIData] = [
        KPIData(
            id="1",
            title="Eficiência Média",
            value=87.5,
            unit="%",
            trend="up",
            trendValue="+2.1%",
            status="success"
        ),
        KPIData(
            id="2",
            title="Risco de Bioincrustação",
            value="Baixo",
            unit="",
            trend="neutral",
            trendValue="Estável",
            status="info"
        ),
        KPIData(
            id="3",
            title="Consumo de Combustível",
            value=1250.5,
            unit="ton",
            trend="down",
            trendValue="-5.2%",
            status="success"
        ),
        KPIData(
            id="4",
            title="Navios em Manutenção",
            value=3,
            unit="",
            trend="down",
            trendValue="-1",
            status="warning"
        ),
    ]
    
    return FleetOverview(
        totalShips=45,
        activeShips=42,
        averageEfficiency=87.5,
        kpis=kpis,
        performanceHistory=performance_history
    )


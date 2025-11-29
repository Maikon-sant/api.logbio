"""
Serviço para busca de dados (logbooks, navios, etc).

Em produção, este serviço faria consultas ao banco de dados.
Atualmente retorna dados mockados para desenvolvimento.
"""
from typing import List, Dict, Any


def get_recent_logbooks(days: int = 30) -> List[Dict[str, Any]]:
    """
    Busca logbooks recentes dos navios da frota.
    
    Args:
        days: Número de dias para buscar logbooks (padrão: 30)
    
    Returns:
        Lista de logbooks, cada um contendo dados de um navio
    """
    # Dados mockados simulando logbooks reais
    # Em produção, isso viria de uma consulta ao banco de dados
    
    mock_logbooks = [
        {
            "ship_id": 1,
            "ship_name": "Lobov 486",
            "idle_days": 15.5,
            "water_temp": 28.5,
            "salinity": 36.2,
            "avg_fuel_consumption": 85.5,
            "optimized_consumption": 72.0,
            "last_maintenance_date": "2023-09-15"
        },
        {
            "ship_id": 2,
            "ship_name": "Marítima Express",
            "idle_days": 8.0,
            "water_temp": 22.0,
            "salinity": 34.5,
            "avg_fuel_consumption": 92.3,
            "optimized_consumption": 88.0,
            "last_maintenance_date": "2023-10-01"
        },
        {
            "ship_id": 3,
            "ship_name": "Ocean Voyager",
            "idle_days": 22.0,
            "water_temp": 26.8,
            "salinity": 35.8,
            "avg_fuel_consumption": 78.2,
            "optimized_consumption": 65.5,
            "last_maintenance_date": "2023-08-20"
        },
        {
            "ship_id": 4,
            "ship_name": "Atlantic Star",
            "idle_days": 5.5,
            "water_temp": 19.5,
            "salinity": 33.0,
            "avg_fuel_consumption": 88.7,
            "optimized_consumption": 85.0,
            "last_maintenance_date": "2023-10-10"
        },
        {
            "ship_id": 5,
            "ship_name": "Pacific Carrier",
            "idle_days": 12.0,
            "water_temp": 24.2,
            "salinity": 35.0,
            "avg_fuel_consumption": 95.1,
            "optimized_consumption": 90.0,
            "last_maintenance_date": "2023-09-25"
        },
        {
            "ship_id": 6,
            "ship_name": "Mediterranean Sea",
            "idle_days": 3.0,
            "water_temp": 18.0,
            "salinity": 38.5,
            "avg_fuel_consumption": 82.4,
            "optimized_consumption": 80.0,
            "last_maintenance_date": "2023-10-15"
        },
        {
            "ship_id": 7,
            "ship_name": "Cargo Master",
            "idle_days": 18.5,
            "water_temp": 27.5,
            "salinity": 36.5,
            "avg_fuel_consumption": 100.2,
            "optimized_consumption": 82.0,
            "last_maintenance_date": "2023-07-10"
        },
        {
            "ship_id": 8,
            "ship_name": "Trade Wind",
            "idle_days": 10.0,
            "water_temp": 23.5,
            "salinity": 34.8,
            "avg_fuel_consumption": 87.8,
            "optimized_consumption": 84.0,
            "last_maintenance_date": "2023-09-30"
        }
    ]
    
    # Filtrar logbooks que estão dentro do período especificado
    # (simulação - em produção seria uma query SQL com filtro de data)
    return mock_logbooks


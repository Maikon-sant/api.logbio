from typing import Dict, List, Any


def calculate_fouling_risk(
    idle_days: float,
    water_temp: float,
    salinity: float
) -> Dict[str, Any]:
    """
    Calculate the biofouling risk for a ship based on environmental factors.

    This function uses a heuristic model to estimate the risk of biofouling
    (marine organism accumulation on hull) based on idle time and water conditions.

    Args:
        idle_days: Number of days the ship has been stationary. Higher idle time
            increases risk as organisms have more time to attach (5 risk points per day).
        water_temp: Water temperature in Celsius. Warmer waters (>20°C) accelerate
            biological growth, with temperatures above 25°C adding 15 risk points.
        salinity: Water salinity in parts per thousand (ppt). Higher salinity (>35 ppt)
            favors certain fouling species, adding 5 risk points.

    Returns:
        Dict containing:
            - risk (int): Numeric risk score from 0 to 100
            - level (str): Risk category - "baixo" (<30), "moderado" (30-69), or "crítico" (>=70)
    """
    # Risk base
    risk = 20
    
    # Fator de dias parado (aumenta significativamente o risco)
    risk += idle_days * 5
    
    # Fator de temperatura da água (temperaturas maiores aceleram crescimento)
    if water_temp > 25:
        risk += 15
    elif water_temp > 20:
        risk += 5
    
    # Fator de salinidade (águas mais salgadas favorecem algumas espécies)
    if salinity > 35:
        risk += 5
    
    # Clamp entre 0 e 100
    risk = max(0, min(100, int(risk)))
    
    # Categorização
    if risk < 30:
        level = "baixo"
    elif risk < 70:
        level = "moderado"
    else:
        level = "crítico"
    
    return {
        "risk": risk,
        "level": level
    }


def calculate_cleaning_roi(
    avg_fuel_consumption: float,
    optimized_consumption: float,
    fuel_price_per_ton: float,
    days: float
) -> Dict[str, float]:
    """
    Calculate the Return on Investment (ROI) for hull cleaning operations.

    This function estimates fuel savings achieved by maintaining a clean hull,
    comparing actual consumption against optimized (clean hull) consumption rates.

    Args:
        avg_fuel_consumption: Current average fuel consumption in tons per day
            (typically higher due to fouling drag).
        optimized_consumption: Expected fuel consumption in tons per day with
            a clean hull (baseline/optimal value).
        fuel_price_per_ton: Current fuel price in currency units per ton.
        days: Number of days to calculate savings over.

    Returns:
        Dict containing:
            - extra_fuel_tons (float): Total excess fuel consumed due to fouling,
              rounded to 2 decimal places.
            - savings_money (float): Potential monetary savings from cleaning,
              rounded to 2 decimal places.
    """
    # Cálculo do consumo extra por dia
    extra_per_day = avg_fuel_consumption - optimized_consumption
    
    # Total de toneladas extras no período
    extra_tons = extra_per_day * days
    
    # Economia monetária
    savings_money = extra_tons * fuel_price_per_ton
    # Validação para evitar valores negativos
    if avg_fuel_consumption < optimized_consumption:
        # Não há economia, retorna zero
        extra_tons = 0.0
        savings_money = 0.0
    else:
        # Cálculo do consumo extra por dia
        extra_per_day = avg_fuel_consumption - optimized_consumption
        # Total de toneladas extras no período
        extra_tons = extra_per_day * days
        # Economia monetária
        savings_money = extra_tons * fuel_price_per_ton
    
    return {
        "extra_fuel_tons": round(extra_tons, 2),
        "savings_money": round(savings_money, 2)
    }


def aggregate_fleet_metrics(
    logbooks: List[Dict[str, Any]],
    fuel_price: float
) -> Dict[str, Any]:
    """
    Aggregate biofouling risk and ROI metrics across an entire fleet.

    This function processes multiple ship logbooks to calculate fleet-wide
    statistics, identify critical vessels, and estimate total potential savings.

    Args:
        logbooks: List of logbook dictionaries, each containing:
            - idle_days (float): Days the ship was stationary
            - water_temp (float): Water temperature in Celsius
            - salinity (float): Water salinity in ppt
            - ship_id: Unique identifier for the ship
            - ship_name (str, optional): Human-readable ship name
            - avg_fuel_consumption (float, optional): Current fuel consumption
            - optimized_consumption (float, optional): Optimal fuel consumption
        fuel_price: Fuel price in currency units per ton for ROI calculations.

    Returns:
        Dict containing:
            - fleet_average_risk (int): Mean risk score across all ships (0-100)
            - critical_ships (list): Ships with risk >= 70, sorted by risk descending,
              each containing id, name, risk, and level
            - total_extra_fuel_tons (float): Sum of excess fuel across fleet
            - total_savings_money (float): Total potential savings from cleaning
            - total_ships (int): Number of ships processed
            - risk_level (str): Fleet risk category - "baixo", "moderado", or "crítico"
    """
    if not logbooks:
        return {
            "fleet_average_risk": 0,
            "critical_ships": [],
            "total_extra_fuel_tons": 0.0,
            "total_savings_money": 0.0,
            "total_ships": 0,
            "risk_level": "baixo"
        }
    
    # Listas para armazenar cálculos
    risks = []
    critical_ships = []
    total_extra_fuel = 0.0
    
    # Processar cada logbook
    for logbook in logbooks:
        # Calcular risco de bioincrustação
        fouling_result = calculate_fouling_risk(
            idle_days=logbook.get("idle_days", 0),
            water_temp=logbook.get("water_temp", 20),
            salinity=logbook.get("salinity", 35)
        )
        
        risk = fouling_result["risk"]
        risks.append(risk)
        
        # Identificar navios críticos (risco >= 70)
        if risk >= 70:
            critical_ships.append({
                "id": logbook.get("ship_id"),
                "name": logbook.get("ship_name", "N/A"),
                "risk": risk,
                "level": fouling_result["level"]
            })
        
        # Calcular ROI de limpeza se houver dados de consumo
        avg_consumption = logbook.get("avg_fuel_consumption")
        optimized_consumption = logbook.get("optimized_consumption")
        
        if avg_consumption and optimized_consumption:
            # Usar período padrão de 30 dias para cálculo
            roi_result = calculate_cleaning_roi(
                avg_fuel_consumption=avg_consumption,
                optimized_consumption=optimized_consumption,
                fuel_price_per_ton=fuel_price,
                days=30
            )
            
            total_extra_fuel += roi_result["extra_fuel_tons"]
    
    # Calcular média de risco
    fleet_average_risk = int(sum(risks) / len(risks)) if risks else 0
    
    # Calcular economia total
    total_savings_money = total_extra_fuel * fuel_price
    
    # Ordenar navios críticos por risco (maior primeiro)
    critical_ships.sort(key=lambda x: x["risk"], reverse=True)
    
    return {
        "fleet_average_risk": fleet_average_risk,
        "critical_ships": critical_ships,
        "total_extra_fuel_tons": round(total_extra_fuel, 2),
        "total_savings_money": round(total_savings_money, 2),
        "total_ships": len(logbooks),
        "risk_level": (
            "crítico" if fleet_average_risk >= 70
            else "moderado" if fleet_average_risk >= 30
            else "baixo"
        )
    }


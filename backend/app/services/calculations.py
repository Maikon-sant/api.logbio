from typing import Dict, List, Any


def calculate_fouling_risk(
    idle_days: float,
    water_temp: float,
    salinity: float
) -> Dict[str, Any]:

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

    if not logbooks:
        return {
            "fleet_average_risk": 0,
            "critical_ships": [],
            "total_extra_fuel_tons": 0.0,
            "total_savings_money": 0.0,
            "total_ships": 0
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


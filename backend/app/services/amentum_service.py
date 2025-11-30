import requests
import math
from datetime import datetime, timezone
import os
from typing import Optional, Dict, Any

# Constantes padrão (podem ser movidas para config se necessário)
DEFAULT_LAT = -25.55
DEFAULT_LON = -48.30

def get_ocean_data(
    variable: str,
    lat: float = DEFAULT_LAT,
    lon: float = DEFAULT_LON,
    api_key: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Busca dados oceanográficos da API Amentum.
    
    Args:
        variable: Variável a ser buscada (ex: 'thetao', 'so', 'uo', 'vo', 'zos')
        lat: Latitude
        lon: Longitude
        api_key: Chave da API (opcional, busca de env var se não fornecido)
        
    Returns:
        Dicionário com dados da resposta ou None em caso de erro.
    """
    if not api_key:
        api_key = os.getenv("AMENTUM_API_KEY")
        
    if not api_key:
        print("Warning: AMENTUM_API_KEY not found.")
        return None

    url = "https://ocean.amentum.io/nemo/phys"
    
    now = datetime.now(timezone.utc)
    
    params = {
        "latitude": lat,
        "longitude": lon,
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "depth": 0,
        "variable": variable
    }

    headers = {
        "Accept": "application/json",
        "API-Key": api_key
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching {variable}: Status {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception fetching {variable}: {str(e)}")
        return None

def calculate_current_speed_direction(u_data: Dict, v_data: Dict) -> Dict[str, float]:
    """
    Calcula velocidade e direção da corrente baseada nos componentes U e V.
    """
    if not u_data or not v_data:
        return {"speed": 0.0, "direction": 0.0}
        
    u_val = u_data.get("value", 0)
    v_val = v_data.get("value", 0)
    
    speed = math.sqrt(u_val*u_val + v_val*v_val)
    direction = math.degrees(math.atan2(v_val, u_val))
    
    return {
        "speed": speed,
        "direction": direction
    }

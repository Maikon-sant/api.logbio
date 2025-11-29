# Exemplos de Uso da API

Este documento contém exemplos de como usar os endpoints da API LogBio486.

## 1. Visão Geral da Frota

### Requisição

```bash
curl -X GET "http://localhost:8000/api/v1/fleet/overview" \
  -H "Content-Type: application/json"
```

### Resposta

```json
{
  "totalShips": 45,
  "activeShips": 42,
  "averageEfficiency": 87.5,
  "kpis": [
    {
      "id": "1",
      "title": "Eficiência Média",
      "value": 87.5,
      "unit": "%",
      "trend": "up",
      "trendValue": "+2.1%",
      "status": "success"
    },
    {
      "id": "2",
      "title": "Risco de Bioincrustação",
      "value": "Baixo",
      "unit": "",
      "trend": "neutral",
      "trendValue": "Estável",
      "status": "info"
    }
  ],
  "performanceHistory": [
    {
      "date": "2023-10-01",
      "value": 85.5,
      "type": "historical"
    }
  ]
}
```

## 2. Gerar Previsão

### Requisição

```bash
curl -X POST "http://localhost:8000/api/v1/predictions/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "shipId": "SHIP-123",
    "routeId": "ROUTE-RJ-SP",
    "speed": 14.5,
    "days": 15
  }'
```

### Resposta

```json
{
  "fuelConsumption": 4350.0,
  "biofoulingRisk": 32.5,
  "maintenanceDate": "2023-12-15",
  "chartData": [
    {
      "date": "2023-11-01",
      "value": 84.2,
      "type": "prediction"
    }
  ]
}
```

## 3. Health Check

### Requisição

```bash
curl -X GET "http://localhost:8000/health"
```

### Resposta

```json
{
  "status": "healthy"
}
```

## Testando com Python

```python
import requests

# Base URL
BASE_URL = "http://localhost:8000/api/v1"

# 1. Obter visão geral da frota
response = requests.get(f"{BASE_URL}/fleet/overview")
print(response.json())

# 2. Gerar previsão
prediction_data = {
    "shipId": "SHIP-123",
    "routeId": "ROUTE-RJ-SP",
    "speed": 14.5,
    "days": 15
}
response = requests.post(
    f"{BASE_URL}/predictions/generate",
    json=prediction_data
)
print(response.json())
```

## Testando com JavaScript/Fetch

```javascript
const API_URL = 'http://localhost:8000/api/v1';

// 1. Obter visão geral da frota
async function getFleetOverview() {
  const response = await fetch(`${API_URL}/fleet/overview`);
  const data = await response.json();
  console.log(data);
  return data;
}

// 2. Gerar previsão
async function generatePrediction(params) {
  const response = await fetch(`${API_URL}/predictions/generate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(params),
  });
  const data = await response.json();
  console.log(data);
  return data;
}

// Uso
getFleetOverview();

generatePrediction({
  shipId: 'SHIP-123',
  routeId: 'ROUTE-RJ-SP',
  speed: 14.5,
  days: 15
});
```


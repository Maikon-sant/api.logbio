# Guia de Integração Frontend - LogBio486 API

Este documento fornece as diretrizes e especificações para integrar o frontend da aplicação LogBio486 com o backend FastAPI.

## Visão Geral

A API fornece serviços para gestão de frota, previsões de bioincrustação e registros de diário de bordo. A comunicação é feita via HTTP/JSON.

- **Base URL (Local)**: `http://localhost:8000/api/v1`
- **Documentação Interativa (Swagger UI)**: `http://localhost:8000/docs`
- **Especificação OpenAPI (JSON)**: `http://localhost:8000/openapi.json`

## Configuração de CORS

O backend está configurado para aceitar requisições das seguintes origens (localhost):
- `http://localhost:8080`
- `http://127.0.0.1:8080`
- `http://localhost:5173` (Vite Default)
- `http://127.0.0.1:5173`

Se o seu frontend estiver rodando em outra porta, solicite a adição na whitelist de CORS.

## Autenticação

Atualmente, a API **não requer autenticação** (aberta para desenvolvimento). Futuramente, será implementado OAuth2 com tokens JWT.

## Endpoints Principais

### 1. Visão Geral da Frota

Retorna um dashboard consolidado com KPIs e histórico.

- **Método**: `GET`
- **Rota**: `/fleet/overview`
- **Exemplo de Requisição**:
  ```javascript
  const response = await fetch('http://localhost:8000/api/v1/fleet/overview');
  const data = await response.json();
  ```
- **Resposta de Sucesso (200 OK)**:
  ```json
  {
    "totalShips": 15,
    "activeShips": 12,
    "averageEfficiency": 85.5,
    "kpis": [
      {
        "id": "fuel-savings",
        "title": "Economia de Combustível",
        "value": "1.2M",
        "unit": "USD",
        "trend": "up",
        "trendValue": "+12%",
        "status": "success"
      }
    ],
    "performanceHistory": [...]
  }
  ```

### 2. Gerar Previsão

Calcula riscos e consumo baseados em parâmetros de simulação.

- **Método**: `POST`
- **Rota**: `/predictions/generate`
- **Body (JSON)**:
  ```json
  {
    "shipId": "ship-123",
    "routeId": "route-456",
    "speed": 14.5,
    "days": 30
  }
  ```
- **Exemplo de Requisição**:
  ```javascript
  const response = await fetch('http://localhost:8000/api/v1/predictions/generate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      shipId: "ship-001",
      routeId: "route-A",
      speed: 12.0,
      days: 45
    })
  });
  ```
- **Resposta de Sucesso (200 OK)**:
  ```json
  {
    "fuelConsumption": 450.5,
    "biofoulingRisk": 0.75,
    "maintenanceDate": "2024-06-15",
    "chartData": [...]
  }
  ```

### 3. Criar Registro de Diário de Bordo

Registra um evento manual ou observação para um navio.

- **Método**: `POST`
- **Rota**: `/logbooks/`
- **Body (JSON)**:
  ```json
  {
    "ship_id": 1,
    "description": "Limpeza do casco realizada no porto de Santos.",
    "date": "2023-10-27T10:00:00"
  }
  ```
  *Nota: `date` é opcional. Se omitido, pode ser nulo ou tratado pelo backend.*

- **Resposta de Sucesso (200 OK)**:
  ```json
  {
    "id": 42,
    "ship_id": 1,
    "description": "Limpeza do casco realizada no porto de Santos.",
    "date": "2023-10-27T10:00:00"
  }
  ```

## Tratamento de Erros

A API retorna códigos de status HTTP padrão:

- `400 Bad Request`: Parâmetros inválidos (ex: velocidade negativa).
- `422 Unprocessable Entity`: Erro de validação de schema (campos faltando ou tipo errado).
- `500 Internal Server Error`: Erro inesperado no servidor.

O corpo do erro geralmente segue o formato:
```json
{
  "detail": "Mensagem descritiva do erro"
}
```

## Tipos e Interfaces (Sugestão TypeScript)

Recomenda-se criar interfaces TypeScript baseadas nos schemas da API para garantir tipagem forte no frontend.

```typescript
interface PredictionParams {
  shipId: string;
  routeId: string;
  speed: number;
  days: number;
}

interface FleetOverview {
  totalShips: number;
  activeShips: number;
  // ...
}
```

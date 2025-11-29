# LogBio486 API - Backend FastAPI

API backend para a plataforma LogBio486, desenvolvida com FastAPI.

## Estrutura do Projeto

```
backend/
├── app/
│   ├── main.py            # Ponto de entrada (FastAPI app)
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/ # Rotas (fleet.py, predictions.py)
│   │       └── api.py     # Roteador principal
│   ├── core/
│   │   └── config.py      # Configurações (env vars)
│   ├── models/            # Modelos de banco de dados (SQLAlchemy/Pydantic)
│   ├── schemas/           # Schemas Pydantic (Request/Response)
│   └── services/          # Lógica de negócio (ML, cálculos)
├── requirements.txt
└── README.md
```

## Instalação

1. **Criar ambiente virtual (recomendado):**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

2. **Instalar dependências:**

```bash
pip install -r requirements.txt
```

3. **Configurar variáveis de ambiente:**

Copie o arquivo `.env.example` para `.env` e ajuste as configurações:

```bash
cp .env.example .env
```

## Executando a API

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em:
- **API**: http://localhost:8000
- **Documentação interativa (Swagger)**: http://localhost:8000/docs
- **Documentação alternativa (ReDoc)**: http://localhost:8000/redoc

## Endpoints Disponíveis

### 1. Visão Geral da Frota

- **Método**: `GET`
- **Rota**: `/api/v1/fleet/overview`
- **Descrição**: Retorna dados consolidados da frota, KPIs e histórico de performance

**Exemplo de resposta:**
```json
{
  "totalShips": 45,
  "activeShips": 42,
  "averageEfficiency": 87.5,
  "kpis": [...],
  "performanceHistory": [...]
}
```

### 2. Gerar Previsão

- **Método**: `POST`
- **Rota**: `/api/v1/predictions/generate`
- **Descrição**: Gera previsões de consumo de combustível e risco de bioincrustação

**Exemplo de requisição:**
```json
{
  "shipId": "SHIP-123",
  "routeId": "ROUTE-RJ-SP",
  "speed": 14.5,
  "days": 15
}
```

**Exemplo de resposta:**
```json
{
  "fuelConsumption": 4350.0,
  "biofoulingRisk": 32.5,
  "maintenanceDate": "2023-12-15",
  "chartData": [...]
}
```

## Configuração de CORS

A API está configurada para aceitar requisições das seguintes origens:
- `http://localhost:8080`
- `http://127.0.0.1:8080`
- `http://localhost:5173` (Vite default)
- `http://127.0.0.1:5173`

Para adicionar novas origens, edite o arquivo `.env` ou `app/core/config.py`.

## Desenvolvimento

### Estrutura de Código

- **Schemas** (`app/schemas/`): Modelos Pydantic para validação de dados
- **Services** (`app/services/`): Lógica de negócio e cálculos
- **Endpoints** (`app/api/v1/endpoints/`): Rotas da API
- **Config** (`app/core/config.py`): Configurações centralizadas

### Adicionando Novos Endpoints

1. Crie o schema em `app/schemas/schemas.py`
2. Implemente a lógica em `app/services/`
3. Crie o endpoint em `app/api/v1/endpoints/`
4. Registre a rota em `app/api/v1/api.py`

## Próximos Passos

- [ ] Implementar autenticação (JWT)
- [ ] Conectar com banco de dados (PostgreSQL)
- [ ] Implementar modelos de ML reais
- [ ] Adicionar testes unitários e de integração
- [ ] Configurar logging estruturado
- [ ] Implementar cache (Redis)

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI de alta performance


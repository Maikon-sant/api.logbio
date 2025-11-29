# Guia de Integração do Frontend

Este documento descreve como configurar o frontend para se comunicar com a API backend FastAPI.

## 1. Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto frontend (ou na pasta onde está o `vite.config.js`/`package.json`) com o seguinte conteúdo:

```env
VITE_API_URL=http://localhost:8000/api/v1
```

**Importante**: No Vite, as variáveis de ambiente devem começar com `VITE_` para serem expostas ao código do frontend.

## 2. Atualização do Serviço de API

Substitua os dados mockados no arquivo `src/services/api.ts` (ou similar) por chamadas reais à API.

### Exemplo de Implementação

```typescript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1';

// Tipos (ajuste conforme necessário)
interface FleetOverview {
  totalShips: number;
  activeShips: number;
  averageEfficiency: number;
  kpis: KPIData[];
  performanceHistory: TimeSeriesPoint[];
}

interface PredictionParams {
  shipId: string;
  routeId: string;
  speed: number;
  days: number;
}

interface PredictionResult {
  fuelConsumption: number;
  biofoulingRisk: number;
  maintenanceDate: string;
  chartData: TimeSeriesPoint[];
}

// Função para obter visão geral da frota
export const getFleetOverview = async (): Promise<FleetOverview> => {
  try {
    const response = await fetch(`${API_URL}/fleet/overview`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        // Adicione aqui o token de autenticação quando implementado
        // 'Authorization': `Bearer ${token}`
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Erro ao buscar dados da frota:', error);
    throw error;
  }
};

// Função para gerar previsão
export const generateInsight = async (
  params: PredictionParams
): Promise<PredictionResult> => {
  try {
    const response = await fetch(`${API_URL}/predictions/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // Adicione aqui o token de autenticação quando implementado
        // 'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(params),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(
        errorData.detail || `HTTP error! status: ${response.status}`
      );
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Erro ao gerar previsão:', error);
    throw error;
  }
};
```

## 3. Tratamento de Erros

Implemente tratamento de erros adequado:

```typescript
try {
  const data = await getFleetOverview();
  // Processar dados
} catch (error) {
  if (error instanceof Error) {
    // Mostrar mensagem de erro ao usuário
    console.error('Erro:', error.message);
  }
  // Fallback para dados mockados ou estado de erro
}
```

## 4. Testando a Conexão

### Verificar se a API está rodando

1. Inicie o backend:
   ```bash
   cd backend
   python run.py
   # ou
   uvicorn app.main:app --reload
   ```

2. Teste o endpoint de health check:
   ```bash
   curl http://localhost:8000/health
   ```

3. Teste o endpoint da frota:
   ```bash
   curl http://localhost:8000/api/v1/fleet/overview
   ```

### Verificar CORS

Se você receber erros de CORS no navegador, verifique:

1. Se a URL do frontend está na lista de origens permitidas em `backend/app/core/config.py`
2. Se o backend está rodando na porta correta (8000)
3. Se o frontend está usando a URL correta da API

## 5. Desenvolvimento

### Modo de Desenvolvimento

Durante o desenvolvimento, você pode:

1. **Usar dados mockados como fallback**: Se a API não estiver disponível, use dados mockados
2. **Logging**: Adicione logs para debug das requisições
3. **Timeouts**: Configure timeouts para evitar requisições travadas

```typescript
const fetchWithTimeout = async (
  url: string,
  options: RequestInit,
  timeout = 10000
): Promise<Response> => {
  const controller = new AbortController();
  const id = setTimeout(() => controller.abort(), timeout);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
    });
    clearTimeout(id);
    return response;
  } catch (error) {
    clearTimeout(id);
    throw error;
  }
};
```

## 6. Próximos Passos

- [ ] Implementar autenticação (quando o backend suportar)
- [ ] Adicionar cache de requisições
- [ ] Implementar retry logic para requisições falhadas
- [ ] Adicionar loading states
- [ ] Implementar polling para dados em tempo real (se necessário)


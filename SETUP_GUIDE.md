# Guia de Configuração - LogBio486 API

Este guia fornece instruções passo a passo para configurar e executar o backend FastAPI.

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Instalação Rápida

### 1. Navegar para o diretório do backend

```bash
cd backend
```

### 2. Criar ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (opcional)

Crie um arquivo `.env` na pasta `backend/` com:

```env
API_V1_STR=/api/v1
PROJECT_NAME=LogBio486 API
VERSION=1.0.0
BACKEND_CORS_ORIGINS=http://localhost:8080,http://127.0.0.1:8080,http://localhost:5173,http://127.0.0.1:5173
SECRET_KEY=your-secret-key-here-change-in-production
```

**Nota**: Se não criar o arquivo `.env`, os valores padrão serão usados.

### 5. Executar a aplicação

**Opção 1 - Usando o script run.py:**
```bash
python run.py
```

**Opção 2 - Usando uvicorn diretamente:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## ✅ Verificar se está funcionando

1. Acesse http://localhost:8000 no navegador
2. Acesse a documentação interativa: http://localhost:8000/docs
3. Teste o health check: http://localhost:8000/health

## 📡 Endpoints Disponíveis

### Base URL
```
http://localhost:8000/api/v1
```

### Endpoints

1. **GET /api/v1/fleet/overview**
   - Retorna visão geral da frota

2. **POST /api/v1/predictions/generate**
   - Gera previsões de consumo e bioincrustação
   - Body: `{ "shipId": "string", "routeId": "string", "speed": number, "days": number }`

3. **GET /health**
   - Health check da API

4. **GET /**
   - Informações da API

## 🔧 Estrutura do Projeto

```
backend/
├── app/
│   ├── main.py                 # Aplicação FastAPI
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/      # Rotas da API
│   │       └── api.py          # Roteador principal
│   ├── core/
│   │   └── config.py           # Configurações
│   ├── schemas/                # Schemas Pydantic
│   ├── services/               # Lógica de negócio
│   └── models/                 # Modelos de banco (futuro)
├── requirements.txt            # Dependências
├── run.py                      # Script de execução
└── README.md                   # Documentação
```

## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'fastapi'"
**Solução**: Certifique-se de que o ambiente virtual está ativado e execute `pip install -r requirements.txt`

### Erro de CORS no frontend
**Solução**: Verifique se a URL do frontend está em `BACKEND_CORS_ORIGINS` no arquivo de configuração

### Porta 8000 já em uso
**Solução**: Altere a porta no comando uvicorn:
```bash
uvicorn app.main:app --reload --port 8001
```

## 📚 Documentação Adicional

- `README.md` - Documentação completa da API
- `EXAMPLES.md` - Exemplos de uso dos endpoints
- `FRONTEND_INTEGRATION.md` - Guia de integração com o frontend

## 🔐 Segurança (Futuro)

Atualmente, a API não requer autenticação. Para produção, será necessário:

1. Implementar autenticação JWT
2. Adicionar validação de tokens nos endpoints
3. Configurar HTTPS
4. Adicionar rate limiting
5. Validar e sanitizar todas as entradas

## 📝 Próximos Passos

1. Conectar com banco de dados (PostgreSQL)
2. Implementar autenticação
3. Adicionar testes
4. Implementar modelos de ML reais
5. Configurar logging estruturado
6. Adicionar monitoramento


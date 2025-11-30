# 🚢 LogBio API - Backend

Bem-vindo ao repositório do backend do **LogBio**, uma solução avançada para monitoramento e predição de bioincrustação e eficiência energética em frotas navais. Este projeto foi construído com foco em performance, escalabilidade e manutenibilidade.

## 🎯 Objetivo do Projeto

Fornecer uma API robusta e eficiente para:
- Gerenciar dados da frota e navios.
- Registrar e consultar diários de bordo (Logbooks).
- Gerar insights e predições sobre consumo de combustível e riscos de bioincrustação.
- Integrar com dados oceanográficos externos (Amentum Ocean API).
- Alimentar dashboards interativos no frontend.

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza uma stack moderna e de alta performance:

- **Linguagem**: [Python 3.8+](https://www.python.org/)
- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) - Moderno, rápido (alta performance) e fácil de usar.
- **Servidor ASGI**: [Uvicorn](https://www.uvicorn.org/) - Servidor de aplicação web assíncrono.
- **Validação de Dados**: [Pydantic](https://docs.pydantic.dev/) - Validação de dados robusta e tipagem forte.
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) - Mapeamento objeto-relacional para interação com banco de dados.
- **Gerenciamento de Dependências**: `pip` e `requirements.txt`.
- **Variáveis de Ambiente**: `python-dotenv`.

## 🏗️ Arquitetura e Estrutura

O projeto segue uma arquitetura modular e limpa, facilitando a manutenção e a adição de novas funcionalidades.

```
api.logbio/
├── amentumOcean.py         # Integração com API externa (Amentum Ocean)
├── backend/
│   ├── app/
│   │   ├── api/            # Camada de API (Rotas e Endpoints)
│   │   │   └── v1/endpoints/ # dashboard, fleet, logbooks, predictions, ships
│   │   ├── core/           # Configurações centrais (CORS, segurança)
│   │   ├── models/         # Modelos de banco de dados (SQLAlchemy)
│   │   ├── schemas/        # Schemas de validação e serialização (Pydantic)
│   │   ├── services/       # Lógica de negócio e regras da aplicação
│   │   └── main.py         # Ponto de entrada da aplicação
│   ├── requirements.txt    # Lista de dependências
│   └── run.py              # Script facilitador de execução
├── .env                    # Variáveis de ambiente (não versionado)
└── README.md               # Este arquivo
```

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.8+ instalado.
- Git instalado.

### Passo a Passo

1. **Clone o repositório** (se ainda não o fez).

2. **Configure o ambiente**:
   ```bash
   # Crie o arquivo .env na raiz com sua chave da API Amentum (se necessário)
   echo "AMENTUM_API_KEY=sua_chave_aqui" > .env
   ```

3. **Instale as dependências**:
   ```bash
   cd backend
   # Crie um ambiente virtual (recomendado)
   python -m venv venv
   # Ative o ambiente (Windows)
   ..\venv\Scripts\activate
   # Instale os pacotes
   pip install -r requirements.txt
   ```

4. **Execute a API**:
   ```bash
   # Dentro da pasta backend
   python run.py
   ```
   A API estará rodando em `http://localhost:8000`.

## 📡 Endpoints Principais

A API é organizada em recursos RESTful. Consulte a documentação interativa em `/docs` para detalhes completos.

- **Dashboard** (`/api/v1/dashboard`): Dados agregados para visão geral.
- **Fleet** (`/api/v1/fleet`): Visão geral e métricas da frota.
- **Ships** (`/api/v1/ships`): Gerenciamento de navios individuais.
- **Logbooks** (`/api/v1/logbooks`): Registros de diário de bordo.
- **Predictions** (`/api/v1/predictions`): Geração de insights de IA/ML.

## 🆚 Diferenciais (Para Comparação)

Se você está comparando este backend com outras soluções, considere os seguintes pontos fortes:

1.  **Performance Assíncrona**: Graças ao FastAPI e Uvicorn, este backend pode lidar com muitas requisições simultâneas de forma muito mais eficiente que frameworks tradicionais síncronos (como Flask ou Django padrão).
2.  **Documentação Automática**: A documentação Swagger/OpenAPI é gerada automaticamente e está sempre atualizada com o código. Acesse `http://localhost:8000/docs` para testar.
3.  **Tipagem Forte e Validação**: O uso de Pydantic garante que os dados de entrada e saída estejam sempre corretos, reduzindo bugs drasticamente e melhorando a experiência de desenvolvimento do frontend (IntelliSense).
4.  **Arquitetura Escalável**: A separação clara entre Rotas, Schemas, Models e Services permite que o projeto cresça sem virar uma "bagunça". É fácil adicionar novos módulos sem quebrar os existentes.
5.  **Pronto para Integração**: Já possui configuração de CORS e estrutura para integração fácil com frontends modernos (React, Vue, etc.), como detalhado em `FRONTEND_INTEGRATION.md`.

## 📚 Documentação Adicional

- [Guia de Configuração Detalhado](SETUP_GUIDE.md)
- [Guia de Integração Frontend](FRONTEND_INTEGRATION.md)

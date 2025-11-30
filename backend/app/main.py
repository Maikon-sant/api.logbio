"""
Ponto de entrada da aplicação FastAPI.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router

tags_metadata = [
    {
        "name": "fleet",
        "description": "Operações relacionadas à gestão e visualização da frota de navios.",
    },
    {
        "name": "predictions",
        "description": "Geração de insights e previsões de bioincrustação e consumo.",
    },
    {
        "name": "logbooks",
        "description": "Gerenciamento de diários de bordo e registros manuais.",
    },
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API para a plataforma LogBio486 - Gestão de Frota e Previsões de Bioincrustação",
    openapi_tags=tags_metadata,
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas da API
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    """Endpoint raiz da API."""
    return {
        "message": "LogBio486 API",
        "version": settings.VERSION,
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
async def health_check():
    """Endpoint de health check."""
    return {"status": "ok"}


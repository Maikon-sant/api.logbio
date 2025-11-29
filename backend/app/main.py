from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.ships import router as ships_router
from .api.logbooks import router as logbooks_router

app = FastAPI(title="Hackathon Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(ships_router, prefix="/api", tags=["ships"])
app.include_router(logbooks_router, prefix="/api", tags=["logbooks"])

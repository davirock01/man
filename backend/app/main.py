"""
Fleet Maintenance System - Main Application
FastAPI Backend
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1 import auth
from app.db.base import Base
from sqlalchemy import create_engine
# Importar modelos para que se registren en Base.metadata
from app.models import Usuario, Vehiculo

# Inicializar base de datos
def init_db():
    """Inicializar base de datos PostgreSQL"""
    try:
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Warning: Could not initialize database: {e}")

# Solo inicializar si no estamos en modo de testing
if os.getenv("TESTING") != "true":
    init_db()

app = FastAPI(
    title="Fleet Maintenance System API",
    description="Sistema de mantenimiento para flotas vehiculares del sector petrolero",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:19006", "*"],  # Frontend y Mobile
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "fleet-maintenance-api",
        "version": "1.0.0",
        "database": "postgresql"
    }

@app.get("/")
def root():
    return {
        "message": "Fleet Maintenance System API",
        "docs": "/api/docs",
        "health": "/health",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


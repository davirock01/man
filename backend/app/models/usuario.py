"""
Modelo Usuario para autenticación y RBAC
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    nombre = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False, index=True)  # CONDUCTOR, COORDINADOR, TECNICO, ADMIN
    estado = Column(String(50), default="ACTIVO")
    telefono = Column(String(50))
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


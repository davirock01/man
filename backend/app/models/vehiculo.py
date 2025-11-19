"""
Modelo Vehículo
"""
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from datetime import datetime
from app.db.base import Base


class Vehiculo(Base):
    __tablename__ = "vehiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(50), unique=True, nullable=False, index=True)
    vin = Column(String(100), unique=True)
    marca = Column(String(100))
    modelo = Column(String(100))
    anio = Column(Integer)
    tipo = Column(String(50), nullable=False, index=True)  # PICKUP, TURBO
    estado_operativo = Column(String(50), default="OPERATIVO")
    odometro_actual = Column(Integer, default=0)
    odometro_ultimo_pm = Column(Integer, default=0)
    gps_device_id = Column(String(100))
    gps_lat = Column(Numeric(10, 8))
    gps_lng = Column(Numeric(11, 8))
    gps_ultima_actualizacion = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class AlertaPredictiva(Base):
    __tablename__ = "alertas_predictivas"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    tipo = Column(String(100), nullable=False)  # PM_PROXIMA, PATRON_RECURRENTE, RIESGO_FALLA
    mensaje = Column(Text, nullable=False)
    criticidad = Column(String(50), default='MEDIA')  # BAJA, MEDIA, ALTA
    estado = Column(String(50), default='PENDIENTE', index=True)  # PENDIENTE, REVISADA, RESUELTA
    metadata_json = Column(JSONB)
    creado_en = Column(TIMESTAMP, default=datetime.utcnow)
    revisada_en = Column(TIMESTAMP)
    resuelta_en = Column(TIMESTAMP)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="alertas_predictivas")


class AlertaReactiva(Base):
    __tablename__ = "alertas_reactivas"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    origen = Column(String(100), nullable=False)  # DVIR_CRITICO, REPORTE_CONDUCTOR, SISTEMA
    mensaje = Column(Text, nullable=False)
    criticidad = Column(String(50), default='ALTA')
    estado = Column(String(50), default='PENDIENTE', index=True)
    metadata_json = Column(JSONB)
    creado_en = Column(TIMESTAMP, default=datetime.utcnow)
    revisada_en = Column(TIMESTAMP)
    resuelta_en = Column(TIMESTAMP)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="alertas_reactivas")


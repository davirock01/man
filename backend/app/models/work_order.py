from sqlalchemy import Column, String, Integer, Date, TIMESTAMP, ForeignKey, DECIMAL, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class OrdenWork(Base):
    __tablename__ = "ordenes_work"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    tipo = Column(String(50), nullable=False)  # PM_PREVENTIVO, CORRECTIVO, DIAGNOSTICO
    prioridad = Column(String(50), default='MEDIA', index=True)  # BAJA, MEDIA, ALTA, URGENTE
    estado = Column(String(50), default='PENDIENTE', index=True)  # PENDIENTE, ASIGNADA, EN_PROGRESO, PAUSADA, COMPLETADA, CANCELADA
    descripcion = Column(Text)
    fecha_programada = Column(Date)
    fecha_asignacion = Column(TIMESTAMP)
    fecha_inicio = Column(TIMESTAMP)
    fecha_fin = Column(TIMESTAMP)
    duracion_estimada_min = Column(Integer)
    duracion_real_min = Column(Integer)
    tecnico_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), index=True)
    coordinador_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))
    contexto_json = Column(JSONB)
    origen_alerta_id = Column(UUID(as_uuid=True))
    costo_estimado = Column(DECIMAL(10, 2))
    costo_real = Column(DECIMAL(10, 2))
    validada_conductor = Column(Boolean, default=False)
    validada_conductor_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="ordenes_work")
    tecnico = relationship("Usuario", foreign_keys=[tecnico_id], back_populates="ordenes_tecnico")
    coordinador = relationship("Usuario", foreign_keys=[coordinador_id], back_populates="ordenes_coordinador")
    items = relationship("OrdenWorkItem", back_populates="orden", cascade="all, delete-orphan")
    logs = relationship("OrdenWorkLog", back_populates="orden", cascade="all, delete-orphan")
    repuestos = relationship("RepuestoUsado", back_populates="orden")
    metricas = relationship("MetricaEjecucion", back_populates="orden", uselist=False)


class OrdenWorkItem(Base):
    __tablename__ = "ordenes_work_items"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ot_id = Column(UUID(as_uuid=True), ForeignKey("ordenes_work.id", ondelete="CASCADE"), nullable=False, index=True)
    tarea = Column(Text, nullable=False)
    estado = Column(String(50), default='PENDIENTE')
    tiempo_estimado_min = Column(Integer)
    tiempo_real_min = Column(Integer)
    notas = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    # Relationships
    orden = relationship("OrdenWork", back_populates="items")


class OrdenWorkLog(Base):
    __tablename__ = "ordenes_work_logs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ot_id = Column(UUID(as_uuid=True), ForeignKey("ordenes_work.id", ondelete="CASCADE"), nullable=False, index=True)
    evento = Column(String(100), nullable=False)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))
    timestamp = Column(TIMESTAMP, default=datetime.utcnow, index=True)
    payload_json = Column(JSONB)
    
    # Relationships
    orden = relationship("OrdenWork", back_populates="logs")


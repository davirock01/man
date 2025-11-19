from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, DECIMAL, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class InventarioTaller(Base):
    __tablename__ = "inventario_taller"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sku = Column(String(100), unique=True, nullable=False, index=True)
    descripcion = Column(Text, nullable=False)
    categoria = Column(String(100))
    stock_actual = Column(Integer, default=0)
    stock_minimo = Column(Integer, default=0)
    costo_unitario = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)


class RepuestoUsado(Base):
    __tablename__ = "repuestos_usados"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ot_id = Column(UUID(as_uuid=True), ForeignKey("ordenes_work.id"), nullable=False, index=True)
    sku = Column(String(100), nullable=False)
    cantidad = Column(Integer, nullable=False)
    costo_unitario = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    # Relationships
    orden = relationship("OrdenWork", back_populates="repuestos")


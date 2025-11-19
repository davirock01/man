from sqlalchemy import Column, String, Integer, Date, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class SeveridadUso(Base):
    __tablename__ = "severidad_uso"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    fecha = Column(Date, nullable=False)
    tipo_uso = Column(String(50), default='NORMAL')  # NORMAL, SEVERO
    eventos_frenazos = Column(Integer, default=0)
    eventos_exceso_vel = Column(Integer, default=0)
    km_recorridos = Column(Integer, default=0)
    metricas_json = Column(JSONB)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    __table_args__ = (
        UniqueConstraint('vehiculo_id', 'fecha', name='uq_severidad_vehiculo_fecha'),
    )
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="severidad_uso")


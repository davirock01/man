from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey, DECIMAL, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class MetricaEjecucion(Base):
    __tablename__ = "metricas_ejecucion"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ot_id = Column(UUID(as_uuid=True), ForeignKey("ordenes_work.id"), nullable=False, index=True)
    desviacion_tiempo_pct = Column(DECIMAL(5, 2))
    desviacion_costo_pct = Column(DECIMAL(5, 2))
    complejidad_final = Column(Integer)  # 1-10
    defecto_predicho_confirmado = Column(Boolean)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    # Relationships
    orden = relationship("OrdenWork", back_populates="metricas")


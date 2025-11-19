from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class PatronRecurrente(Base):
    __tablename__ = "patrones_recurrentes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    componente = Column(String(255), nullable=False)
    tipo_defecto = Column(String(255))
    veces_30d = Column(Integer, nullable=False)
    criticidad = Column(String(50))
    primera_ocurrencia = Column(TIMESTAMP)
    ultima_ocurrencia = Column(TIMESTAMP)
    estado = Column(String(50), default='ACTIVO')
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="patrones_recurrentes")


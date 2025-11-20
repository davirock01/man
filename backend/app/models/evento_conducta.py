from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, DECIMAL
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class EventoConducta(Base):
    __tablename__ = "eventos_conducta"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    conductor_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
    tipo_evento = Column(String(100), nullable=False, index=True)  # FRENAZO, EXCESO_VELOCIDAD, ACELERACION_BRUSCA
    severidad = Column(Integer, default=1)  # 1-10
    timestamp = Column(TIMESTAMP, default=datetime.utcnow, nullable=False, index=True)
    gps_lat = Column(DECIMAL(10, 8))
    gps_lng = Column(DECIMAL(11, 8))
    datos_extra = Column(JSONB)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="eventos_conducta")


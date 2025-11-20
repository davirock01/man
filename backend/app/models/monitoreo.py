from sqlalchemy import Column, String, Date, TIMESTAMP, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class MonitoreoVehiculo(Base):
    __tablename__ = "monitoreo_vehiculos"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    fecha_registro = Column(TIMESTAMP, default=datetime.utcnow)
    comentario = Column(Text)
    fecha_revision_programada = Column(Date)
    estado = Column(String(50), default='ACTIVO')
    revisado_por = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))
    revisado_at = Column(TIMESTAMP)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="monitoreos")


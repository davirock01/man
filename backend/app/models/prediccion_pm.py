from sqlalchemy import Column, Integer, Date, TIMESTAMP, ForeignKey, DECIMAL
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from app.core.database import Base


class PrediccionPM(Base):
    __tablename__ = "predicciones_pm"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_id = Column(UUID(as_uuid=True), ForeignKey("vehiculos.id"), nullable=False, index=True)
    km_actual = Column(Integer, nullable=False)
    km_proximo_pm = Column(Integer, nullable=False)
    fecha_proximo_pm = Column(Date)
    dias_hasta_pm = Column(Integer)
    prob_falla = Column(DECIMAL(5, 2))
    umbral_configurado = Column(DECIMAL(5, 2))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    vehiculo = relationship("Vehiculo", back_populates="predicciones_pm")


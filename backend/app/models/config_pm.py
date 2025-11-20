from sqlalchemy import Column, String, Integer, TIMESTAMP, DECIMAL
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
from datetime import datetime
from app.core.database import Base


class ConfigPM(Base):
    __tablename__ = "config_pm"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    vehiculo_tipo = Column(String(50), nullable=False, index=True)
    politica_km = Column(Integer, nullable=False)
    politica_dias = Column(Integer, nullable=False)
    umbral_alerta_pct = Column(DECIMAL(5, 2), default=0.90)
    items_checklist = Column(JSONB)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)


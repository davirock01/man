from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from uuid import UUID


class AlertaPredictivaResponse(BaseModel):
    id: UUID
    vehiculo_id: UUID
    tipo: str
    mensaje: str
    criticidad: str
    estado: str
    metadata_json: Optional[Dict[str, Any]]
    creado_en: datetime
    revisada_en: Optional[datetime]
    resuelta_en: Optional[datetime]
    
    class Config:
        from_attributes = True


class AlertaReactivaResponse(BaseModel):
    id: UUID
    vehiculo_id: UUID
    origen: str
    mensaje: str
    criticidad: str
    estado: str
    metadata_json: Optional[Dict[str, Any]]
    creado_en: datetime
    revisada_en: Optional[datetime]
    resuelta_en: Optional[datetime]
    
    class Config:
        from_attributes = True


class PatronRecurrenteResponse(BaseModel):
    id: UUID
    vehiculo_id: UUID
    componente: str
    tipo_defecto: Optional[str]
    veces_30d: int
    criticidad: Optional[str]
    primera_ocurrencia: Optional[datetime]
    ultima_ocurrencia: Optional[datetime]
    estado: str
    created_at: datetime
    
    class Config:
        from_attributes = True


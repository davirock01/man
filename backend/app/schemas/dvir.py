from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class DVIRItemCreate(BaseModel):
    componente: str
    categoria: Optional[str] = None
    estado_item: str  # OK, ALERTA, CRITICO
    comentario: Optional[str] = None
    foto_url: Optional[str] = None


class DVIRItemResponse(DVIRItemCreate):
    id: int
    dvir_id: int
    creado_en: datetime
    
    class Config:
        from_attributes = True


class DVIRCreate(BaseModel):
    vehiculo_id: int
    odometro: float = Field(..., gt=0, description="Odómetro debe ser mayor a 0")
    gps_lat: Optional[float] = None
    gps_lng: Optional[float] = None
    firma_url: Optional[str] = None
    firma_nombre: Optional[str] = None
    items: List[DVIRItemCreate]
    comentarios: Optional[str] = None
    modo_offline_flag: bool = False


class DVIRResponse(BaseModel):
    id: int
    vehiculo_id: int
    conductor_id: int
    timestamp: datetime
    odometro: float
    gps_lat: Optional[float] = None
    gps_lng: Optional[float] = None
    estado_resumen: str
    firma_url: Optional[str] = None
    firma_nombre: Optional[str] = None
    modo_offline_flag: bool
    sincronizado_en: Optional[datetime] = None
    revisado: bool
    revisado_por_id: Optional[int] = None
    revisado_en: Optional[datetime] = None
    comentarios: Optional[str] = None
    creado_en: datetime
    items: List[DVIRItemResponse] = []
    
    class Config:
        from_attributes = True


class DefectoReporteCreate(BaseModel):
    vehiculo_id: int
    componente: str
    severidad: str  # LEVE, MODERADO, SEVERO
    descripcion: str
    gps_lat: Optional[float] = None
    gps_lng: Optional[float] = None
    foto_url: Optional[str] = None


class JornadaFinRequest(BaseModel):
    vehiculo_id: int
    odometro_final: float
    comentarios: Optional[str] = None


class EventoConductaCreate(BaseModel):
    vehiculo_id: int
    tipo_evento: str
    severidad: str
    gps_lat: Optional[float] = None
    gps_lng: Optional[float] = None
    velocidad: Optional[float] = None
    datos_extra_json: Optional[dict] = None


class SyncRequest(BaseModel):
    operaciones: List[dict]  # List of sync operations



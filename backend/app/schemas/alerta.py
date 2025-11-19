from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AlertaPredictiv

aResponse(BaseModel):
    id: int
    vehiculo_id: int
    tipo: str
    mensaje: str
    criticidad: str
    estado: str
    datos_json: Optional[dict] = None
    prediccion_pm_id: Optional[int] = None
    creado_en: datetime
    atendida_en: Optional[datetime] = None
    atendida_por_id: Optional[int] = None
    
    class Config:
        from_attributes = True


class AlertaReactivaResponse(BaseModel):
    id: int
    vehiculo_id: int
    origen: str
    mensaje: str
    componente_afectado: Optional[str] = None
    criticidad: str
    estado: str
    origen_dvir_id: Optional[int] = None
    creado_en: datetime
    atendida_en: Optional[datetime] = None
    atendida_por_id: Optional[int] = None
    ot_generada_id: Optional[int] = None
    
    class Config:
        from_attributes = True


class PatronRecurrenteResponse(BaseModel):
    id: int
    vehiculo_id: int
    componente: str
    tipo_defecto: str
    veces_30d: int
    fecha_primera_ocurrencia: Optional[datetime] = None
    fecha_ultima_ocurrencia: Optional[datetime] = None
    criticidad: str
    estado: str
    detalles_json: Optional[dict] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True



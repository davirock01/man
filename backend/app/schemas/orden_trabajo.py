from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class OrdenTrabajoItemCreate(BaseModel):
    tarea: str
    componente: Optional[str] = None
    tiempo_estimado_min: Optional[int] = None


class OrdenTrabajoItemResponse(BaseModel):
    id: int
    ot_id: int
    tarea: str
    componente: Optional[str] = None
    estado: str
    tiempo_estimado_min: Optional[int] = None
    tiempo_real_min: Optional[int] = None
    notas: Optional[str] = None
    foto_url: Optional[str] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True


class OrdenTrabajoCreate(BaseModel):
    vehiculo_id: int
    tipo: str  # PM_PREVENTIVO, CORRECTIVO, DIAGNOSTICO, EMERGENCIA
    prioridad: str = "MEDIA"  # BAJA, MEDIA, ALTA, URGENTE
    descripcion: str
    fecha_programada: Optional[datetime] = None
    tecnico_id: Optional[int] = None
    items: List[OrdenTrabajoItemCreate] = []
    origen_alerta_id: Optional[int] = None
    origen_tipo: Optional[str] = None


class OrdenTrabajoUpdate(BaseModel):
    estado: Optional[str] = None
    tecnico_id: Optional[int] = None
    prioridad: Optional[str] = None
    fecha_programada: Optional[datetime] = None
    observaciones: Optional[str] = None


class OrdenTrabajoResponse(BaseModel):
    id: int
    vehiculo_id: int
    tipo: str
    prioridad: str
    estado: str
    tecnico_id: Optional[int] = None
    coordinador_id: int
    fecha_creacion: datetime
    fecha_asignacion: Optional[datetime] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    fecha_programada: Optional[datetime] = None
    duracion_estimada_min: Optional[int] = None
    costo_estimado: Optional[float] = None
    descripcion: str
    observaciones: Optional[str] = None
    contexto_json: Optional[dict] = None
    creado_en: datetime
    items: List[OrdenTrabajoItemResponse] = []
    
    class Config:
        from_attributes = True


class RepuestoUsadoCreate(BaseModel):
    sku: str
    cantidad: int
    costo_unitario: float


class RepuestoUsadoResponse(BaseModel):
    id: int
    ot_id: int
    sku: str
    cantidad: int
    costo_unitario: float
    costo_total: float
    usado_en: datetime
    
    class Config:
        from_attributes = True


class DefectoInesperadoCreate(BaseModel):
    descripcion: str
    componente: str
    foto_url: Optional[str] = None
    requiere_autorizacion: bool = True



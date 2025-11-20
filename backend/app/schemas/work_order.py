from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime, date
from uuid import UUID
from decimal import Decimal


class OrdenWorkItemCreate(BaseModel):
    tarea: str
    tiempo_estimado_min: Optional[int] = None


class OrdenWorkItemResponse(BaseModel):
    id: UUID
    ot_id: UUID
    tarea: str
    estado: str
    tiempo_estimado_min: Optional[int]
    tiempo_real_min: Optional[int]
    notas: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class OrdenWorkCreate(BaseModel):
    vehiculo_id: UUID
    tipo: str  # PM_PREVENTIVO, CORRECTIVO, DIAGNOSTICO
    prioridad: str = "MEDIA"
    descripcion: Optional[str] = None
    fecha_programada: Optional[date] = None
    tecnico_id: Optional[UUID] = None
    duracion_estimada_min: Optional[int] = None
    costo_estimado: Optional[Decimal] = None
    items: List[OrdenWorkItemCreate] = []


class OrdenWorkUpdate(BaseModel):
    estado: Optional[str] = None
    tecnico_id: Optional[UUID] = None
    fecha_programada: Optional[date] = None
    descripcion: Optional[str] = None
    prioridad: Optional[str] = None


class OrdenWorkResponse(BaseModel):
    id: UUID
    vehiculo_id: UUID
    tipo: str
    prioridad: str
    estado: str
    descripcion: Optional[str]
    fecha_programada: Optional[date]
    fecha_asignacion: Optional[datetime]
    fecha_inicio: Optional[datetime]
    fecha_fin: Optional[datetime]
    duracion_estimada_min: Optional[int]
    duracion_real_min: Optional[int]
    tecnico_id: Optional[UUID]
    coordinador_id: Optional[UUID]
    contexto_json: Optional[Dict[str, Any]]
    costo_estimado: Optional[Decimal]
    costo_real: Optional[Decimal]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class RepuestoUsadoCreate(BaseModel):
    sku: str
    cantidad: int
    costo_unitario: Optional[Decimal] = None


class DefectoInesperadoRequest(BaseModel):
    descripcion: str
    foto_url: Optional[str] = None
    componente: Optional[str] = None


class CompletarOTRequest(BaseModel):
    notas_finales: Optional[str] = None
    fotos: List[str] = []


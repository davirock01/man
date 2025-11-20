from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ChecklistItemCreate(BaseModel):
    componente: str
    categoria: Optional[str] = None
    orden: int = 0
    obligatorio: bool = True
    requiere_foto_si_alerta: bool = True
    descripcion: Optional[str] = None
    instrucciones: Optional[str] = None


class ChecklistItemResponse(BaseModel):
    id: int
    checklist_id: int
    componente: str
    categoria: Optional[str] = None
    orden: int
    obligatorio: bool
    requiere_foto_si_alerta: bool
    descripcion: Optional[str] = None
    instrucciones: Optional[str] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True


class ChecklistCreate(BaseModel):
    nombre: str
    vehiculo_tipo: str
    descripcion: Optional[str] = None
    items: List[ChecklistItemCreate]


class ChecklistUpdate(BaseModel):
    nombre: Optional[str] = None
    activo: Optional[bool] = None
    descripcion: Optional[str] = None


class ChecklistResponse(BaseModel):
    id: int
    nombre: str
    vehiculo_tipo: str
    activo: bool
    version: Optional[str] = None
    descripcion: Optional[str] = None
    creado_en: datetime
    creado_por_id: Optional[int] = None
    items: List[ChecklistItemResponse] = []
    
    class Config:
        from_attributes = True



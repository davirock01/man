from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID
from decimal import Decimal


class ConfigPMCreate(BaseModel):
    vehiculo_tipo: str
    politica_km: int
    politica_dias: int
    umbral_alerta_pct: Decimal = 0.90
    items_checklist: Optional[List[Dict[str, Any]]] = None


class ConfigPMUpdate(BaseModel):
    politica_km: Optional[int] = None
    politica_dias: Optional[int] = None
    umbral_alerta_pct: Optional[Decimal] = None
    items_checklist: Optional[List[Dict[str, Any]]] = None


class ConfigPMResponse(BaseModel):
    id: UUID
    vehiculo_tipo: str
    politica_km: int
    politica_dias: int
    umbral_alerta_pct: Decimal
    items_checklist: Optional[List[Dict[str, Any]]]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


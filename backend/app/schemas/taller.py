from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InventarioTallerResponse(BaseModel):
    id: int
    sku: str
    descripcion: str
    categoria: Optional[str] = None
    stock_actual: int
    stock_minimo: int
    stock_maximo: Optional[int] = None
    costo_unitario: float
    moneda: str
    proveedor: Optional[str] = None
    ubicacion: Optional[str] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True



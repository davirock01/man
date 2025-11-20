from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VehiculoBase(BaseModel):
    placa: str
    vehiculo_tipo: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    año: Optional[int] = None
    vin: Optional[str] = None


class VehiculoCreate(VehiculoBase):
    pass


class VehiculoUpdate(BaseModel):
    placa: Optional[str] = None
    vehiculo_tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    año: Optional[int] = None
    estado_operativo: Optional[str] = None
    conductor_asignado_id: Optional[int] = None
    notas: Optional[str] = None


class VehiculoResponse(VehiculoBase):
    id: int
    estado_operativo: str
    odometro_actual: float
    conductor_asignado_id: Optional[int] = None
    ultima_lat: Optional[float] = None
    ultima_lng: Optional[float] = None
    ultima_actualizacion_gps: Optional[datetime] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True


class ConfigPMBase(BaseModel):
    vehiculo_tipo: str
    politica_km: float
    politica_tiempo: int
    umbral_km_alerta: float = 0.9
    umbral_tiempo_alerta: float = 0.9


class ConfigPMCreate(ConfigPMBase):
    pass


class ConfigPMUpdate(BaseModel):
    politica_km: Optional[float] = None
    politica_tiempo: Optional[int] = None
    umbral_km_alerta: Optional[float] = None
    umbral_tiempo_alerta: Optional[float] = None
    descripcion: Optional[str] = None


class ConfigPMResponse(ConfigPMBase):
    id: int
    descripcion: Optional[str] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True



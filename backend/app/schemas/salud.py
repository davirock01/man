from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class SaludVehiculoResponse(BaseModel):
    vehiculo_id: int
    score_salud: float
    fecha_calculo: datetime
    detalle_json: Optional[Dict[str, Any]] = None
    clasificacion: Optional[str] = None
    creado_en: datetime
    
    class Config:
        from_attributes = True


class PrediccionPMResponse(BaseModel):
    id: int
    vehiculo_id: int
    km_actual: float
    fecha_actual: datetime
    km_ultimo_pm: float
    fecha_ultimo_pm: Optional[datetime] = None
    km_proximo_pm: float
    fecha_proximo_pm: Optional[datetime] = None
    prob_falla: Optional[float] = None
    umbral_km_configurado: Optional[float] = None
    umbral_tiempo_configurado: Optional[int] = None
    alerta_generada: str
    creado_en: datetime
    
    class Config:
        from_attributes = True



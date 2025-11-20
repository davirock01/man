from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class SaludVehiculo(Base):
    __tablename__ = "salud_vehiculo"
    
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), primary_key=True, index=True)
    
    # Score de salud (0-100)
    score_salud = Column(Float, nullable=False, default=100.0)
    
    # Fecha de último cálculo
    fecha_calculo = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    
    # Detalle del cálculo (JSON)
    detalle_json = Column(JSON)  # {dvir_score, eventos_score, ot_score, pm_compliance, etc}
    
    # Clasificación
    clasificacion = Column(String(50))  # EXCELENTE, BUENO, REGULAR, MALO, CRITICO
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<SaludVehiculo {self.vehiculo_id} - Score {self.score_salud}>"


class PrediccionPM(Base):
    __tablename__ = "predicciones_pm"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Estado actual
    km_actual = Column(Float, nullable=False)
    fecha_actual = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    
    # Último PM realizado
    km_ultimo_pm = Column(Float, default=0.0)
    fecha_ultimo_pm = Column(DateTime(timezone=True))
    
    # Próximo PM predicho
    km_proximo_pm = Column(Float, nullable=False)
    fecha_proximo_pm = Column(DateTime(timezone=True))
    
    # Probabilidad de falla antes del PM
    prob_falla = Column(Float)  # 0-1
    
    # Umbrales configurados
    umbral_km_configurado = Column(Float)
    umbral_tiempo_configurado = Column(Integer)  # días
    
    # Flags de alerta
    alerta_generada = Column(String(50), default="NO")  # NO, ADVERTENCIA, URGENTE
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<PrediccionPM Vehiculo {self.vehiculo_id} - Próximo PM {self.km_proximo_pm} km>"



from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class SyncQueue(Base):
    __tablename__ = "sync_queue"
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    
    # Tipo de operación
    operacion = Column(String(100), nullable=False, index=True)  # CREATE_DVIR, UPDATE_OT, REPORT_DEFECTO, etc.
    entidad_tipo = Column(String(100), nullable=False)  # DVIR, OT, EVENTO, etc.
    
    # Payload
    payload_json = Column(JSON, nullable=False)
    
    # Estado de sincronización
    estado = Column(String(50), nullable=False, default="PENDIENTE", index=True)  
    # Estados: PENDIENTE, PROCESANDO, COMPLETADA, FALLIDA, CONFLICTO
    
    # Identificador temporal del cliente
    client_temp_id = Column(String(100), index=True)
    
    # ID de la entidad creada en servidor
    entidad_server_id = Column(Integer)
    
    # Intento de procesamiento
    intentos = Column(Integer, default=0)
    ultimo_intento = Column(DateTime(timezone=True))
    error_mensaje = Column(Text)
    
    # Timestamps
    creado_en = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    procesado_en = Column(DateTime(timezone=True))
    
    def __repr__(self):
        return f"<SyncQueue {self.operacion} - {self.estado}>"


class HistoricoPredicciones(Base):
    __tablename__ = "historico_predicciones"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    prediccion_id = Column(Integer, ForeignKey("predicciones_pm.id"))
    
    # Predicción realizada
    km_predicho = Column(Float)
    fecha_predicha = Column(DateTime(timezone=True))
    prob_falla_predicha = Column(Float)
    
    # Realidad (qué sucedió realmente)
    se_confirmo_bool = Column(Boolean)
    km_real = Column(Float)
    fecha_real = Column(DateTime(timezone=True))
    
    # Error de predicción
    error_km_pct = Column(Float)
    error_tiempo_dias = Column(Integer)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __repr__(self):
        return f"<HistoricoPredicciones Vehiculo {self.vehiculo_id}>"



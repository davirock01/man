from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from app.core.database import Base


class AlertaPredictiva(Base):
    __tablename__ = "alertas_predictivas"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Tipo de alerta
    tipo = Column(String(100), nullable=False, index=True)  # PM_PROXIMA, PM_VENCIDA, PATRON_DETECTADO, etc.
    mensaje = Column(Text, nullable=False)
    
    # Criticidad
    criticidad = Column(String(50), nullable=False, index=True)  # BAJA, MEDIA, ALTA, CRITICA
    
    # Estado
    estado = Column(String(50), nullable=False, default="ACTIVA", index=True)  # ACTIVA, ATENDIDA, CERRADA, DESCARTADA
    
    # Datos adicionales
    datos_json = Column(JSON)
    
    # Asociación a predicción
    prediccion_pm_id = Column(Integer, ForeignKey("predicciones_pm.id"))
    
    # Seguimiento
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
    atendida_en = Column(DateTime(timezone=True))
    atendida_por_id = Column(Integer, ForeignKey("usuarios.id"))
    cerrada_en = Column(DateTime(timezone=True))
    
    def __repr__(self):
        return f"<AlertaPredictiva {self.tipo} - {self.criticidad}>"


class AlertaReactiva(Base):
    __tablename__ = "alertas_reactivas"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Origen de la alerta
    origen = Column(String(100), nullable=False, index=True)  # DVIR, DEFECTO_RUTA, CONDUCTOR, SISTEMA
    origen_dvir_id = Column(Integer, ForeignKey("dvirs.id"))
    origen_evento_id = Column(Integer)
    
    # Detalle de la alerta
    mensaje = Column(Text, nullable=False)
    componente_afectado = Column(String(200))
    
    # Criticidad
    criticidad = Column(String(50), nullable=False, index=True)  # BAJA, MEDIA, ALTA, CRITICA
    
    # Estado
    estado = Column(String(50), nullable=False, default="ACTIVA", index=True)  # ACTIVA, ATENDIDA, CERRADA, DESCARTADA
    
    # Seguimiento
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
    atendida_en = Column(DateTime(timezone=True))
    atendida_por_id = Column(Integer, ForeignKey("usuarios.id"))
    cerrada_en = Column(DateTime(timezone=True))
    
    # Orden de trabajo generada
    ot_generada_id = Column(Integer, ForeignKey("ordenes_work.id"))
    
    def __repr__(self):
        return f"<AlertaReactiva {self.origen} - {self.criticidad}>"


class PatronRecurrente(Base):
    __tablename__ = "patrones_recurrentes"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Patrón detectado
    componente = Column(String(200), nullable=False)
    tipo_defecto = Column(String(200), nullable=False)
    
    # Conteo
    veces_30d = Column(Integer, nullable=False)  # Número de veces en últimos 30 días
    fecha_primera_ocurrencia = Column(DateTime(timezone=True))
    fecha_ultima_ocurrencia = Column(DateTime(timezone=True))
    
    # Criticidad acumulada
    criticidad = Column(String(50), nullable=False)  # BAJA, MEDIA, ALTA, CRITICA
    
    # Estado
    estado = Column(String(50), nullable=False, default="ACTIVO", index=True)  # ACTIVO, RESUELTO, DESCARTADO
    
    # Detalles
    detalles_json = Column(JSON)  # Array de DVIR IDs y fechas
    
    # Seguimiento
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)
    resuelto_en = Column(DateTime(timezone=True))
    resuelto_por_id = Column(Integer, ForeignKey("usuarios.id"))
    
    def __repr__(self):
        return f"<PatronRecurrente {self.componente} - {self.tipo_defecto} ({self.veces_30d}x)>"


class MonitoreoVehiculo(Base):
    __tablename__ = "monitoreo_vehiculos"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Registro de monitoreo
    fecha_registro = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    comentario = Column(Text, nullable=False)
    
    # Próxima revisión
    fecha_revision_programada = Column(DateTime(timezone=True))
    
    # Estado
    estado = Column(String(50), nullable=False, default="PENDIENTE")  # PENDIENTE, REVISADO, ESCALADO
    
    # Seguimiento
    registrado_por_id = Column(Integer, ForeignKey("usuarios.id"))
    revisado_por_id = Column(Integer, ForeignKey("usuarios.id"))
    revisado_en = Column(DateTime(timezone=True))
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<MonitoreoVehiculo {self.vehiculo_id} - {self.estado}>"



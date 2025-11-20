from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class OrdenTrabajo(Base):
    __tablename__ = "ordenes_work"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Tipo de OT
    tipo = Column(String(50), nullable=False, index=True)  # PM_PREVENTIVO, CORRECTIVO, DIAGNOSTICO, EMERGENCIA
    
    # Prioridad
    prioridad = Column(String(50), nullable=False, default="MEDIA")  # BAJA, MEDIA, ALTA, URGENTE
    
    # Estado
    estado = Column(String(50), nullable=False, default="PENDIENTE", index=True)  
    # Estados: PENDIENTE, ASIGNADA, EN_PROGRESO, PAUSADA, PAUSADA_FALTA_REPUESTOS, COMPLETADA, PARCIAL, CANCELADA
    
    # Asignación
    tecnico_id = Column(Integer, ForeignKey("usuarios.id"), index=True)
    coordinador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    
    # Fechas
    fecha_creacion = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    fecha_asignacion = Column(DateTime(timezone=True))
    fecha_inicio = Column(DateTime(timezone=True))
    fecha_fin = Column(DateTime(timezone=True))
    fecha_programada = Column(DateTime(timezone=True))
    
    # Contexto histórico (JSON)
    contexto_json = Column(JSON)  # Historial, sugerencias, repuestos probables, etc.
    
    # Origen de la OT
    origen_alerta_id = Column(Integer)  # ID de alerta que generó la OT
    origen_tipo = Column(String(50))  # ALERTA_PREDICTIVA, ALERTA_REACTIVA, MANUAL, PROGRAMADA
    
    # Estimaciones
    duracion_estimada_min = Column(Integer)  # minutos
    costo_estimado = Column(Float)
    
    # Descripción
    descripcion = Column(Text, nullable=False)
    observaciones = Column(Text)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    items = relationship("OrdenTrabajoItem", back_populates="orden", cascade="all, delete-orphan")
    logs = relationship("OrdenTrabajoLog", back_populates="orden", cascade="all, delete-orphan")
    repuestos = relationship("RepuestoUsado", back_populates="orden", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<OrdenTrabajo {self.id} - {self.tipo} - {self.estado}>"


class OrdenTrabajoItem(Base):
    __tablename__ = "ordenes_work_items"
    
    id = Column(Integer, primary_key=True, index=True)
    ot_id = Column(Integer, ForeignKey("ordenes_work.id"), nullable=False, index=True)
    
    # Tarea
    tarea = Column(String(500), nullable=False)
    componente = Column(String(200))
    
    # Estado de la tarea
    estado = Column(String(50), nullable=False, default="PENDIENTE")  # PENDIENTE, EN_PROGRESO, COMPLETADA, OMITIDA
    
    # Tiempos
    tiempo_estimado_min = Column(Integer)
    tiempo_real_min = Column(Integer)
    
    # Detalles
    notas = Column(Text)
    foto_url = Column(String(500))
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    orden = relationship("OrdenTrabajo", back_populates="items")
    
    def __repr__(self):
        return f"<OrdenTrabajoItem {self.tarea} - {self.estado}>"


class OrdenTrabajoLog(Base):
    __tablename__ = "ordenes_work_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    ot_id = Column(Integer, ForeignKey("ordenes_work.id"), nullable=False, index=True)
    
    # Evento registrado
    evento = Column(String(200), nullable=False)  # CREADA, ASIGNADA, INICIADA, PAUSADA, REANUDADA, COMPLETADA, etc.
    
    # Usuario que generó el evento
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    
    # Timestamp
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    
    # Payload adicional
    payload_json = Column(JSON)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    orden = relationship("OrdenTrabajo", back_populates="logs")
    
    def __repr__(self):
        return f"<OrdenTrabajoLog {self.evento} - OT {self.ot_id}>"


class MetricasEjecucion(Base):
    __tablename__ = "metricas_ejecucion"
    
    id = Column(Integer, primary_key=True, index=True)
    ot_id = Column(Integer, ForeignKey("ordenes_work.id"), unique=True, nullable=False, index=True)
    
    # Desviaciones
    desviacion_tiempo_pct = Column(Float)  # Porcentaje de desviación respecto a estimado
    desviacion_costo_pct = Column(Float)
    
    # Tiempos reales
    tiempo_total_min = Column(Integer)
    tiempo_efectivo_min = Column(Integer)
    tiempo_pausas_min = Column(Integer)
    
    # Costos reales
    costo_total = Column(Float)
    costo_mano_obra = Column(Float)
    costo_repuestos = Column(Float)
    
    # Complejidad
    complejidad_final = Column(String(50))  # BAJA, MEDIA, ALTA
    
    # Predicción vs Realidad
    defecto_predicho_confirmado_bool = Column(Boolean)
    causa_raiz = Column(String(500))
    
    # Calidad
    reinspecciones_count = Column(Integer, default=0)
    defectos_nuevos_encontrados = Column(Integer, default=0)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<MetricasEjecucion OT {self.ot_id}>"



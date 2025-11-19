from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class DVIR(Base):
    __tablename__ = "dvirs"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    conductor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    
    # Datos del DVIR
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    odometro = Column(Float, nullable=False)
    
    # GPS
    gps_lat = Column(Float)
    gps_lng = Column(Float)
    
    # Estado resumen del DVIR
    estado_resumen = Column(String(50), nullable=False)  # OK, ALERTA, CRITICO
    
    # Firma digital
    firma_url = Column(String(500))
    firma_nombre = Column(String(200))
    
    # Modo offline
    modo_offline_flag = Column(Boolean, default=False)
    sincronizado_en = Column(DateTime(timezone=True))
    
    # Estado de revisión
    revisado = Column(Boolean, default=False)
    revisado_por_id = Column(Integer, ForeignKey("usuarios.id"))
    revisado_en = Column(DateTime(timezone=True))
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    comentarios = Column(Text)
    
    # Relationships
    items = relationship("DVIRItem", back_populates="dvir", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<DVIR {self.id} - Vehiculo {self.vehiculo_id} - {self.estado_resumen}>"


class DVIRItem(Base):
    __tablename__ = "dvir_items"
    
    id = Column(Integer, primary_key=True, index=True)
    dvir_id = Column(Integer, ForeignKey("dvirs.id"), nullable=False, index=True)
    
    # Componente inspeccionado
    componente = Column(String(200), nullable=False)  # Motor, Frenos, Luces, etc.
    categoria = Column(String(100))  # Mecánico, Eléctrico, Carrocería, etc.
    
    # Estado del item
    estado_item = Column(String(50), nullable=False)  # OK, ALERTA, CRITICO
    
    # Detalles
    comentario = Column(Text)
    foto_url = Column(String(500))
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    dvir = relationship("DVIR", back_populates="items")
    
    def __repr__(self):
        return f"<DVIRItem {self.componente} - {self.estado_item}>"


class EventoConducta(Base):
    __tablename__ = "eventos_conducta"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    conductor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False, index=True)
    
    # Tipo de evento
    tipo_evento = Column(String(100), nullable=False, index=True)  # FRENAZO_BRUSCO, EXCESO_VELOCIDAD, ACELERACION_BRUSCA, GIRO_BRUSCO
    severidad = Column(String(50), nullable=False)  # LEVE, MODERADO, SEVERO
    
    # Datos del evento
    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    gps_lat = Column(Float)
    gps_lng = Column(Float)
    velocidad = Column(Float)  # km/h
    
    # Datos adicionales (JSON)
    datos_extra_json = Column(JSON)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __repr__(self):
        return f"<EventoConducta {self.tipo_evento} - {self.severidad}>"


class SeveridadUso(Base):
    __tablename__ = "severidad_uso"
    
    id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("vehiculos.id"), nullable=False, index=True)
    
    # Fecha de cálculo
    fecha = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), index=True)
    
    # Tipo de uso
    tipo_uso = Column(String(50), nullable=False)  # NORMAL, MODERADO, SEVERO
    
    # Métricas calculadas
    metricas_json = Column(JSON)  # {frenazos_count, excesos_velocidad, km_recorridos, etc}
    score_severidad = Column(Float)  # 0-100
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __repr__(self):
        return f"<SeveridadUso Vehiculo {self.vehiculo_id} - {self.tipo_uso}>"



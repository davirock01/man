from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Checklist(Base):
    __tablename__ = "checklists"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False)
    vehiculo_tipo = Column(String(50), nullable=False, index=True)  # PICKUP, TURBO, etc.
    
    # Configuración
    activo = Column(Boolean, default=True)
    version = Column(String(20))
    
    # Descripción
    descripcion = Column(Text)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    creado_por_id = Column(Integer, ForeignKey("usuarios.id"))
    
    # Relationships
    items = relationship("ChecklistItem", back_populates="checklist", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Checklist {self.nombre} - {self.vehiculo_tipo}>"


class ChecklistItem(Base):
    __tablename__ = "checklist_items"
    
    id = Column(Integer, primary_key=True, index=True)
    checklist_id = Column(Integer, ForeignKey("checklists.id"), nullable=False, index=True)
    
    # Item
    componente = Column(String(200), nullable=False)
    categoria = Column(String(100))  # SEGURIDAD, MECANICO, ELECTRICO, DOCUMENTACION, etc.
    orden = Column(Integer, nullable=False, default=0)  # Orden de presentación
    
    # Configuración
    obligatorio = Column(Boolean, default=True)
    requiere_foto_si_alerta = Column(Boolean, default=True)
    
    # Descripción
    descripcion = Column(Text)
    instrucciones = Column(Text)
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    checklist = relationship("Checklist", back_populates="items")
    
    def __repr__(self):
        return f"<ChecklistItem {self.componente}>"



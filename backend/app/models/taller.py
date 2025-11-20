from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class InventarioTaller(Base):
    __tablename__ = "inventario_taller"
    
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(100), unique=True, nullable=False, index=True)
    descripcion = Column(String(500), nullable=False)
    categoria = Column(String(100), index=True)  # FILTROS, ACEITES, FRENOS, ELECTRICO, etc.
    
    # Stock
    stock_actual = Column(Integer, nullable=False, default=0)
    stock_minimo = Column(Integer, nullable=False, default=0)
    stock_maximo = Column(Integer)
    
    # Costos
    costo_unitario = Column(Float, nullable=False)
    moneda = Column(String(10), default="USD")
    
    # Proveedor
    proveedor = Column(String(200))
    codigo_proveedor = Column(String(100))
    
    # Ubicación en taller
    ubicacion = Column(String(100))
    
    # Metadata
    creado_en = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    actualizado_en = Column(DateTime(timezone=True), onupdate=func.now())
    notas = Column(Text)
    
    def __repr__(self):
        return f"<InventarioTaller {self.sku} - {self.descripcion}>"


class RepuestoUsado(Base):
    __tablename__ = "repuestos_usados"
    
    id = Column(Integer, primary_key=True, index=True)
    ot_id = Column(Integer, ForeignKey("ordenes_work.id"), nullable=False, index=True)
    sku = Column(String(100), ForeignKey("inventario_taller.sku"), nullable=False, index=True)
    
    # Cantidad usada
    cantidad = Column(Integer, nullable=False)
    
    # Costo al momento del uso
    costo_unitario = Column(Float, nullable=False)
    costo_total = Column(Float, nullable=False)
    
    # Metadata
    usado_en = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    registrado_por_id = Column(Integer, ForeignKey("usuarios.id"))
    
    # Relationships
    orden = relationship("OrdenTrabajo", back_populates="repuestos")
    
    def __repr__(self):
        return f"<RepuestoUsado {self.sku} x{self.cantidad} - OT {self.ot_id}>"



"""
Importar todos los modelos para que SQLAlchemy los registre
"""
from app.models.usuario import Usuario
from app.models.vehiculo import Vehiculo

# Exportar modelos principales
__all__ = [
    "Usuario",
    "Vehiculo",
]

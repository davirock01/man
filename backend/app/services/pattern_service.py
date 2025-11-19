from sqlalchemy.orm import Session
from sqlalchemy import func
from uuid import UUID
from typing import List
from datetime import datetime, timedelta

from app.models.patron_recurrente import PatronRecurrente
from app.models.dvir import DVIR, DVIRItem


class PatternDetectionService:
    def __init__(self, db: Session):
        self.db = db
    
    def scan_recurrent_defects(self, vehiculo_id: UUID, dias: int = 30) -> List[PatronRecurrente]:
        """Scan for recurrent defects in the last N days."""
        fecha_limite = datetime.utcnow() - timedelta(days=dias)
        
        # Get DVIRs from last N days
        dvirs = self.db.query(DVIR).filter(
            DVIR.vehiculo_id == vehiculo_id,
            DVIR.timestamp >= fecha_limite
        ).all()
        
        # Count defects by component and severity
        defectos_por_componente = {}
        
        for dvir in dvirs:
            for item in dvir.items:
                if item.estado_item in ["ALERTA", "CRITICO"]:
                    key = (item.componente, item.estado_item)
                    
                    if key not in defectos_por_componente:
                        defectos_por_componente[key] = {
                            "count": 0,
                            "first_occurrence": dvir.timestamp,
                            "last_occurrence": dvir.timestamp
                        }
                    
                    defectos_por_componente[key]["count"] += 1
                    defectos_por_componente[key]["last_occurrence"] = max(
                        defectos_por_componente[key]["last_occurrence"],
                        dvir.timestamp
                    )
        
        # Create patterns for components with 3+ occurrences
        patrones = []
        for (componente, estado), data in defectos_por_componente.items():
            if data["count"] >= 3:
                patron = PatronRecurrente(
                    vehiculo_id=vehiculo_id,
                    componente=componente,
                    tipo_defecto=estado,
                    veces_30d=data["count"],
                    criticidad=estado,
                    primera_ocurrencia=data["first_occurrence"],
                    ultima_ocurrencia=data["last_occurrence"],
                    estado="ACTIVO"
                )
                patrones.append(patron)
        
        return patrones


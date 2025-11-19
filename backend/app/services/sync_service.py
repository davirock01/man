from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Dict, Any

from app.schemas.dvir import SyncItemRequest, SyncResponse


class SyncService:
    def __init__(self, db: Session):
        self.db = db
    
    def process_sync_queue(self, items: List[SyncItemRequest], user_id: UUID) -> SyncResponse:
        """Process offline synchronization queue."""
        sincronizados = 0
        errores = []
        
        for item in items:
            try:
                if item.tipo == "DVIR":
                    self._sync_dvir(item.data, user_id)
                    sincronizados += 1
                elif item.tipo == "EVENTO":
                    self._sync_evento(item.data, user_id)
                    sincronizados += 1
                elif item.tipo == "OT_UPDATE":
                    self._sync_ot_update(item.data, user_id)
                    sincronizados += 1
                else:
                    errores.append({
                        "tipo": item.tipo,
                        "error": f"Tipo de sincronización no soportado: {item.tipo}"
                    })
            except Exception as e:
                errores.append({
                    "tipo": item.tipo,
                    "error": str(e)
                })
        
        return SyncResponse(sincronizados=sincronizados, errores=errores)
    
    def _sync_dvir(self, data: Dict[str, Any], user_id: UUID):
        """Sync DVIR from offline queue."""
        from app.services.dvir_service import DVIRService
        from app.schemas.dvir import DVIRCreate, DVIRItemCreate
        
        # Convert dict to schema
        items = [DVIRItemCreate(**item) for item in data.get("items", [])]
        dvir_data = DVIRCreate(
            vehiculo_id=data["vehiculo_id"],
            tipo=data.get("tipo", "PREOPERATIVO"),
            odometro=data["odometro"],
            gps_lat=data.get("gps_lat"),
            gps_lng=data.get("gps_lng"),
            items=items,
            firma_url=data.get("firma_url"),
            comentarios=data.get("comentarios"),
            modo_offline=True
        )
        
        dvir_service = DVIRService(self.db)
        dvir = dvir_service.create_dvir(dvir_data, user_id)
        
        # Process triggers
        if dvir.estado_resumen == "CRITICO":
            dvir_service.trigger_alerts_if_critical(dvir.id)
        dvir_service.scan_recurrent_patterns(dvir.vehiculo_id)
        
        self.db.flush()
    
    def _sync_evento(self, data: Dict[str, Any], user_id: UUID):
        """Sync driving event from offline queue."""
        from app.models.evento_conducta import EventoConducta
        
        evento = EventoConducta(
            vehiculo_id=data["vehiculo_id"],
            conductor_id=user_id,
            tipo_evento=data["tipo_evento"],
            severidad=data.get("severidad", 1),
            gps_lat=data.get("gps_lat"),
            gps_lng=data.get("gps_lng"),
            datos_extra=data.get("datos_extra")
        )
        self.db.add(evento)
        self.db.flush()
    
    def _sync_ot_update(self, data: Dict[str, Any], user_id: UUID):
        """Sync work order update from offline queue."""
        from app.models.work_order import OrdenWork, OrdenWorkLog
        
        ot = self.db.query(OrdenWork).filter(OrdenWork.id == data["ot_id"]).first()
        if ot:
            if "estado" in data:
                ot.estado = data["estado"]
            if "notas" in data:
                # Add log
                log = OrdenWorkLog(
                    ot_id=ot.id,
                    evento="SYNC_UPDATE",
                    usuario_id=user_id,
                    payload_json=data
                )
                self.db.add(log)
            
            self.db.flush()
    
    def resolve_conflicts(self, local_item: Dict, server_item: Dict) -> Dict:
        """
        Resolve conflicts between local and server data.
        Strategy: last-write-wins based on timestamp.
        """
        local_timestamp = local_item.get("timestamp")
        server_timestamp = server_item.get("updated_at") or server_item.get("timestamp")
        
        if local_timestamp and server_timestamp:
            if local_timestamp > server_timestamp:
                return local_item
            else:
                return server_item
        
        # Default to server if timestamps unavailable
        return server_item


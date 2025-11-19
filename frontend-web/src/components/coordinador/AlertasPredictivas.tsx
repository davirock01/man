import { useEffect, useState } from 'react';
import { coordinadorAPI } from '@/services/api';

export function AlertasPredictivas() {
  const [alertas, setAlertas] = useState<any[]>([]);

  useEffect(() => {
    loadAlertas();
  }, []);

  const loadAlertas = async () => {
    try {
      const res = await coordinadorAPI.getAlertasPredictivas('ACTIVA');
      setAlertas(res.data);
    } catch (error) {
      console.error('Error loading alertas predictivas:', error);
    }
  };

  return (
    <div className="space-y-2 max-h-96 overflow-y-auto">
      {alertas.length === 0 ? (
        <div className="text-gray-500 text-center py-4">No hay alertas pendientes</div>
      ) : (
        alertas.map((alerta) => (
          <div
            key={alerta.id}
            className={`p-3 rounded border-l-4 ${
              alerta.criticidad === 'ALTA' ? 'border-red-500 bg-red-50' :
              alerta.criticidad === 'MEDIA' ? 'border-yellow-500 bg-yellow-50' :
              'border-blue-500 bg-blue-50'
            }`}
          >
            <div className="font-semibold">{alerta.tipo}</div>
            <div className="text-sm">{alerta.mensaje}</div>
            <div className="text-xs text-gray-600 mt-1">
              Veh #{alerta.vehiculo_id} | {new Date(alerta.creado_en).toLocaleDateString()}
            </div>
          </div>
        ))
      )}
    </div>
  );
}



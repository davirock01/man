import { useEffect, useState } from 'react';
import { coordinadorAPI } from '@/services/api';

export function AlertasReactivas() {
  const [alertas, setAlertas] = useState<any[]>([]);

  useEffect(() => {
    loadAlertas();
  }, []);

  const loadAlertas = async () => {
    try {
      const res = await coordinadorAPI.getAlertasReactivas('ACTIVA');
      setAlertas(res.data);
    } catch (error) {
      console.error('Error loading alertas reactivas:', error);
    }
  };

  return (
    <div className="space-y-2 max-h-96 overflow-y-auto">
      {alertas.length === 0 ? (
        <div className="text-gray-500 text-center py-4">No hay alertas críticas</div>
      ) : (
        alertas.map((alerta) => (
          <div
            key={alerta.id}
            className={`p-3 rounded border-l-4 ${
              alerta.criticidad === 'CRITICA' ? 'border-red-600 bg-red-100' :
              alerta.criticidad === 'ALTA' ? 'border-red-500 bg-red-50' :
              'border-orange-500 bg-orange-50'
            }`}
          >
            <div className="font-semibold">{alerta.origen}</div>
            <div className="text-sm">{alerta.mensaje}</div>
            <div className="text-xs text-gray-600 mt-1">
              {alerta.componente_afectado} | Veh #{alerta.vehiculo_id}
            </div>
          </div>
        ))
      )}
    </div>
  );
}



import { useEffect, useState } from 'react';
import { coordinadorAPI } from '@/services/api';

export function PatronesRecurrentes() {
  const [patrones, setPatrones] = useState<any[]>([]);

  useEffect(() => {
    loadPatrones();
  }, []);

  const loadPatrones = async () => {
    try {
      const res = await coordinadorAPI.getPatrones('ACTIVO');
      setPatrones(res.data);
    } catch (error) {
      console.error('Error loading patrones:', error);
    }
  };

  return (
    <div className="space-y-2 max-h-96 overflow-y-auto">
      {patrones.length === 0 ? (
        <div className="text-gray-500 text-center py-4">No hay patrones detectados</div>
      ) : (
        patrones.map((patron) => (
          <div
            key={patron.id}
            className="p-3 rounded border border-purple-300 bg-purple-50"
          >
            <div className="font-semibold">{patron.componente}</div>
            <div className="text-sm">{patron.tipo_defecto}</div>
            <div className="text-xs text-gray-600 mt-1">
              {patron.veces_30d} ocurrencias en 30 días | Veh #{patron.vehiculo_id}
            </div>
          </div>
        ))
      )}
    </div>
  );
}



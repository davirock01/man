import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { coordinadorAPI } from '@/services/api';
import { Loading } from '@/components/common/Loading';

export function Alerts() {
  const [filter, setFilter] = useState<'predictivas' | 'reactivas' | 'all'>('all');
  const [estado, setEstado] = useState('ACTIVA');

  const { data: predictivas, isLoading: loadingP } = useQuery({
    queryKey: ['alertas-predictivas', estado],
    queryFn: () => coordinadorAPI.getAlertasPredictivas(estado).then(res => res.data),
    enabled: filter === 'predictivas' || filter === 'all',
  });

  const { data: reactivas, isLoading: loadingR } = useQuery({
    queryKey: ['alertas-reactivas', estado],
    queryFn: () => coordinadorAPI.getAlertasReactivas(estado).then(res => res.data),
    enabled: filter === 'reactivas' || filter === 'all',
  });

  if (loadingP || loadingR) return <Loading />;

  const allAlertas = [
    ...(predictivas || []).map(a => ({ ...a, tipo_alerta: 'PREDICTIVA' })),
    ...(reactivas || []).map(a => ({ ...a, tipo_alerta: 'REACTIVA' })),
  ].sort((a, b) => new Date(b.creado_en).getTime() - new Date(a.creado_en).getTime());

  const criticidadColor = (criticidad: string) => {
    switch (criticidad) {
      case 'CRITICA': return 'bg-red-100 text-red-800 border-red-500';
      case 'ALTA': return 'bg-orange-100 text-orange-800 border-orange-500';
      case 'MEDIA': return 'bg-yellow-100 text-yellow-800 border-yellow-500';
      default: return 'bg-blue-100 text-blue-800 border-blue-500';
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Alertas</h1>
        
        <div className="flex gap-4">
          <select
            value={filter}
            onChange={(e) => setFilter(e.target.value as any)}
            className="rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="all">Todas</option>
            <option value="predictivas">Predictivas</option>
            <option value="reactivas">Reactivas</option>
          </select>

          <select
            value={estado}
            onChange={(e) => setEstado(e.target.value)}
            className="rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="ACTIVA">Activas</option>
            <option value="ATENDIDA">Atendidas</option>
            <option value="CERRADA">Cerradas</option>
          </select>
        </div>
      </div>

      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {allAlertas.length === 0 ? (
            <li className="px-6 py-12 text-center text-gray-500">
              No hay alertas para mostrar
            </li>
          ) : (
            allAlertas.map((alerta) => (
              <li key={`${alerta.tipo_alerta}-${alerta.id}`} className="px-6 py-4 hover:bg-gray-50">
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <span className={`px-3 py-1 rounded-full text-xs font-semibold border-2 ${criticidadColor(alerta.criticidad)}`}>
                        {alerta.criticidad}
                      </span>
                      <span className={`px-2 py-1 rounded text-xs font-medium ${
                        alerta.tipo_alerta === 'PREDICTIVA' ? 'bg-blue-100 text-blue-800' : 'bg-purple-100 text-purple-800'
                      }`}>
                        {alerta.tipo_alerta}
                      </span>
                      <span className="text-sm text-gray-500">
                        Vehículo #{alerta.vehiculo_id}
                      </span>
                    </div>
                    
                    <p className="text-sm font-medium text-gray-900">{alerta.mensaje}</p>
                    
                    <p className="mt-1 text-xs text-gray-500">
                      {new Date(alerta.creado_en).toLocaleString('es-ES')}
                    </p>
                  </div>

                  <div className="flex gap-2">
                    <button className="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50">
                      Ver Contexto
                    </button>
                    <button className="px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-medium hover:bg-blue-700">
                      Crear OT
                    </button>
                  </div>
                </div>
              </li>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}


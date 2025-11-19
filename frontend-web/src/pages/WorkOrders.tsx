import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { coordinadorAPI } from '@/services/api';
import { Loading } from '@/components/common/Loading';

export function WorkOrders() {
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [estadoFilter, setEstadoFilter] = useState<string>('all');

  // In a real app, we would have an endpoint to list all OTs
  // For now, this is a placeholder
  const ots = [];

  const estadoColor = (estado: string) => {
    switch (estado) {
      case 'COMPLETADA': return 'bg-green-100 text-green-800';
      case 'EN_PROGRESO': return 'bg-blue-100 text-blue-800';
      case 'PAUSADA': return 'bg-yellow-100 text-yellow-800';
      case 'PENDIENTE': return 'bg-gray-100 text-gray-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const prioridadColor = (prioridad: string) => {
    switch (prioridad) {
      case 'URGENTE': return 'text-red-600';
      case 'ALTA': return 'text-orange-600';
      case 'MEDIA': return 'text-yellow-600';
      default: return 'text-gray-600';
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Órdenes de Trabajo</h1>
        
        <div className="flex gap-4">
          <select
            value={estadoFilter}
            onChange={(e) => setEstadoFilter(e.target.value)}
            className="rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500"
          >
            <option value="all">Todos los estados</option>
            <option value="PENDIENTE">Pendiente</option>
            <option value="EN_PROGRESO">En Progreso</option>
            <option value="PAUSADA">Pausada</option>
            <option value="COMPLETADA">Completada</option>
          </select>

          <button
            onClick={() => setShowCreateModal(true)}
            className="px-4 py-2 bg-blue-600 text-white rounded-md font-medium hover:bg-blue-700"
          >
            Nueva OT
          </button>
        </div>
      </div>

      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {ots.length === 0 ? (
            <li className="px-6 py-12 text-center text-gray-500">
              No hay órdenes de trabajo para mostrar
            </li>
          ) : (
            ots.map((ot: any) => (
              <li key={ot.id} className="px-6 py-4 hover:bg-gray-50">
                <div className="flex items-center justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <span className="text-lg font-bold text-gray-900">OT #{ot.id}</span>
                      <span className={`px-3 py-1 rounded-full text-xs font-semibold ${estadoColor(ot.estado)}`}>
                        {ot.estado}
                      </span>
                      <span className={`text-sm font-semibold ${prioridadColor(ot.prioridad)}`}>
                        {ot.prioridad}
                      </span>
                      <span className="text-sm text-gray-500">
                        {ot.tipo}
                      </span>
                    </div>
                    
                    <p className="text-sm text-gray-900 mb-1">{ot.descripcion}</p>
                    
                    <div className="flex items-center gap-4 text-xs text-gray-500">
                      <span>Vehículo #{ot.vehiculo_id}</span>
                      {ot.tecnico_id && <span>Técnico #{ot.tecnico_id}</span>}
                      <span>Creada: {new Date(ot.fecha_creacion).toLocaleDateString('es-ES')}</span>
                    </div>
                  </div>

                  <div className="flex gap-2">
                    <button className="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50">
                      Ver Detalle
                    </button>
                  </div>
                </div>
              </li>
            ))
          )}
        </ul>
      </div>

      {/* Create OT Modal - Simplified */}
      {showCreateModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 max-w-2xl w-full mx-4">
            <h2 className="text-2xl font-bold mb-4">Nueva Orden de Trabajo</h2>
            {/* Form implementation would go here */}
            <div className="flex justify-end gap-2 mt-6">
              <button
                onClick={() => setShowCreateModal(false)}
                className="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50"
              >
                Cancelar
              </button>
              <button
                className="px-4 py-2 bg-blue-600 text-white rounded-md text-sm font-medium hover:bg-blue-700"
              >
                Crear OT
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}


import { useQuery } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import { adminAPI } from '@/services/api';
import { Loading } from '@/components/common/Loading';

export function Vehicles() {
  const { data: vehiculos, isLoading } = useQuery({
    queryKey: ['vehiculos'],
    queryFn: () => adminAPI.getVehiculos().then(res => res.data),
  });

  if (isLoading) return <Loading />;

  const estadoColor = (estado: string) => {
    switch (estado) {
      case 'OPERATIVO': return 'bg-green-100 text-green-800';
      case 'MANTENIMIENTO': return 'bg-yellow-100 text-yellow-800';
      case 'NO_OPERATIVO': return 'bg-red-100 text-red-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Vehículos</h1>
        <button className="px-4 py-2 bg-blue-600 text-white rounded-md font-medium hover:bg-blue-700">
          Agregar Vehículo
        </button>
      </div>

      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {vehiculos?.map((vehiculo: any) => (
            <li key={vehiculo.id}>
              <Link to={`/vehicles/${vehiculo.id}`} className="block hover:bg-gray-50">
                <div className="px-6 py-4">
                  <div className="flex items-center justify-between">
                    <div className="flex-1">
                      <div className="flex items-center gap-4">
                        <div>
                          <p className="text-lg font-semibold text-gray-900">{vehiculo.placa}</p>
                          <p className="text-sm text-gray-500">
                            {vehiculo.marca} {vehiculo.modelo} ({vehiculo.año})
                          </p>
                        </div>
                        <span className={`px-3 py-1 rounded-full text-xs font-semibold ${estadoColor(vehiculo.estado_operativo)}`}>
                          {vehiculo.estado_operativo}
                        </span>
                      </div>
                      
                      <div className="mt-2 flex items-center gap-6 text-sm text-gray-500">
                        <span>Tipo: {vehiculo.vehiculo_tipo}</span>
                        <span>Odómetro: {vehiculo.odometro_actual?.toFixed(0)} km</span>
                        {vehiculo.conductor_asignado_id && (
                          <span>Conductor asignado: #{vehiculo.conductor_asignado_id}</span>
                        )}
                      </div>
                    </div>

                    <div className="flex items-center text-sm text-gray-400">
                      <svg className="h-5 w-5" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
                      </svg>
                    </div>
                  </div>
                </div>
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}


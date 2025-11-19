import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { coordinadorAPI } from '@/services/api';
import { Loading } from '@/components/common/Loading';

export function VehicleDetail() {
  const { id } = useParams<{ id: string }>();

  const { data: contexto, isLoading } = useQuery({
    queryKey: ['vehiculo-contexto', id],
    queryFn: () => coordinadorAPI.getVehiculoContexto(Number(id)).then(res => res.data),
  });

  if (isLoading) return <Loading />;
  if (!contexto) return <div>Vehículo no encontrado</div>;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-900">
          Vehículo {contexto.vehiculo.placa}
        </h1>
        <p className="text-gray-500">
          {contexto.vehiculo.marca} {contexto.vehiculo.modelo} ({contexto.vehiculo.año})
        </p>
      </div>

      {/* Health Score */}
      <div className="bg-white shadow rounded-lg p-6 mb-6">
        <h2 className="text-xl font-bold mb-4">Score de Salud</h2>
        <div className="flex items-center gap-4">
          <div className="text-5xl font-bold text-blue-600">
            {contexto.salud?.toFixed(0) || 'N/A'}
          </div>
          <div>
            <p className="text-sm text-gray-600">Estado General</p>
            <p className="text-lg font-semibold">
              {contexto.salud >= 90 ? 'Excelente' :
               contexto.salud >= 75 ? 'Bueno' :
               contexto.salud >= 60 ? 'Regular' :
               contexto.salud >= 40 ? 'Malo' : 'Crítico'}
            </p>
          </div>
        </div>
      </div>

      {/* PM Prediction */}
      {contexto.prediccion_pm && (
        <div className="bg-white shadow rounded-lg p-6 mb-6">
          <h2 className="text-xl font-bold mb-4">Próximo Mantenimiento</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div>
              <p className="text-sm text-gray-600">KM para próximo PM</p>
              <p className="text-2xl font-bold">{contexto.prediccion_pm.km_proximo_pm?.toFixed(0)}</p>
            </div>
            <div>
              <p className="text-sm text-gray-600">KM restantes</p>
              <p className="text-2xl font-bold text-orange-600">
                {contexto.prediccion_pm.km_restantes?.toFixed(0)}
              </p>
            </div>
            <div>
              <p className="text-sm text-gray-600">Estado</p>
              <p className="text-lg font-semibold">
                {contexto.prediccion_pm.alerta_generada}
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Alertas Activas */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-xl font-bold mb-4">Alertas Predictivas</h2>
          <div className="space-y-2">
            {contexto.alertas_predictivas?.length === 0 ? (
              <p className="text-gray-500">No hay alertas predictivas</p>
            ) : (
              contexto.alertas_predictivas?.map((alerta: any) => (
                <div key={alerta.id} className="p-3 bg-blue-50 rounded border-l-4 border-blue-500">
                  <p className="font-semibold">{alerta.tipo}</p>
                  <p className="text-sm">{alerta.mensaje}</p>
                </div>
              ))
            )}
          </div>
        </div>

        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-xl font-bold mb-4">Alertas Reactivas</h2>
          <div className="space-y-2">
            {contexto.alertas_reactivas?.length === 0 ? (
              <p className="text-gray-500">No hay alertas reactivas</p>
            ) : (
              contexto.alertas_reactivas?.map((alerta: any) => (
                <div key={alerta.id} className="p-3 bg-red-50 rounded border-l-4 border-red-500">
                  <p className="font-semibold">{alerta.origen}</p>
                  <p className="text-sm">{alerta.mensaje}</p>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* Patrones */}
      {contexto.patrones?.length > 0 && (
        <div className="bg-white shadow rounded-lg p-6 mb-6">
          <h2 className="text-xl font-bold mb-4">Patrones Recurrentes</h2>
          <div className="space-y-2">
            {contexto.patrones.map((patron: any) => (
              <div key={patron.id} className="p-3 bg-purple-50 rounded border-l-4 border-purple-500">
                <p className="font-semibold">{patron.componente} - {patron.tipo_defecto}</p>
                <p className="text-sm">{patron.veces_30d} ocurrencias en 30 días</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent DVIRs */}
      <div className="bg-white shadow rounded-lg p-6 mb-6">
        <h2 className="text-xl font-bold mb-4">DVIRs Recientes</h2>
        <div className="space-y-2">
          {contexto.dvirs_recientes?.map((dvir: any) => (
            <div key={dvir.id} className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <div>
                <p className="font-semibold">DVIR #{dvir.id}</p>
                <p className="text-sm text-gray-600">
                  {new Date(dvir.timestamp).toLocaleString('es-ES')}
                </p>
              </div>
              <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                dvir.estado_resumen === 'OK' ? 'bg-green-100 text-green-800' :
                dvir.estado_resumen === 'ALERTA' ? 'bg-yellow-100 text-yellow-800' :
                'bg-red-100 text-red-800'
              }`}>
                {dvir.estado_resumen}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Recent OTs */}
      <div className="bg-white shadow rounded-lg p-6">
        <h2 className="text-xl font-bold mb-4">Órdenes de Trabajo Recientes</h2>
        <div className="space-y-2">
          {contexto.ots_recientes?.length === 0 ? (
            <p className="text-gray-500">No hay órdenes de trabajo</p>
          ) : (
            contexto.ots_recientes?.map((ot: any) => (
              <div key={ot.id} className="flex justify-between items-center p-3 bg-gray-50 rounded">
                <div>
                  <p className="font-semibold">OT #{ot.id} - {ot.tipo}</p>
                  <p className="text-sm text-gray-600">{ot.descripcion}</p>
                </div>
                <span className={`px-3 py-1 rounded-full text-xs font-semibold ${
                  ot.estado === 'COMPLETADA' ? 'bg-green-100 text-green-800' :
                  ot.estado === 'EN_PROGRESO' ? 'bg-blue-100 text-blue-800' :
                  'bg-gray-100 text-gray-800'
                }`}>
                  {ot.estado}
                </span>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}


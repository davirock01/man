export function Alertas() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Alertas del Sistema</h1>
      <div className="grid gap-4">
        {/* Alertas Predictivas */}
        <div className="bg-yellow-50 border border-yellow-200 p-4 rounded">
          <h3 className="font-semibold text-yellow-800 mb-2">⚠️ Alertas Predictivas</h3>
          <p className="text-sm text-yellow-700">Vehículos próximos a mantenimiento preventivo</p>
          <div className="mt-2 text-yellow-900">
            🚧 Módulo en desarrollo - Próximamente disponible
          </div>
        </div>
        
        {/* Alertas Reactivas */}
        <div className="bg-red-50 border border-red-200 p-4 rounded">
          <h3 className="font-semibold text-red-800 mb-2">🚨 Alertas Reactivas</h3>
          <p className="text-sm text-red-700">Defectos reportados que requieren atención</p>
          <div className="mt-2 text-red-900">
            🚧 Módulo en desarrollo - Próximamente disponible
          </div>
        </div>
        
        {/* Patrones Recurrentes */}
        <div className="bg-blue-50 border border-blue-200 p-4 rounded">
          <h3 className="font-semibold text-blue-800 mb-2">🔄 Patrones Recurrentes</h3>
          <p className="text-sm text-blue-700">Fallas que se repiten en la flota</p>
          <div className="mt-2 text-blue-900">
            🚧 Módulo en desarrollo - Próximamente disponible
          </div>
        </div>
      </div>
    </div>
  );
}


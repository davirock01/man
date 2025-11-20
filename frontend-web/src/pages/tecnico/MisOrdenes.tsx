export function MisOrdenes() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Mis Órdenes de Trabajo</h1>
      
      <div className="mb-4">
        <div className="flex gap-2">
          <button className="px-4 py-2 bg-blue-600 text-white rounded">Pendientes</button>
          <button className="px-4 py-2 bg-gray-200 rounded">En Progreso</button>
          <button className="px-4 py-2 bg-gray-200 rounded">Completadas</button>
        </div>
      </div>
      
      <div className="space-y-4">
        {/* OT de ejemplo */}
        <div className="bg-white shadow rounded p-4">
          <div className="flex justify-between items-start">
            <div>
              <div className="font-semibold text-lg">OT-001 - Mantenimiento Preventivo</div>
              <div className="text-sm text-gray-600">Vehículo: TEST123 - Toyota Hilux</div>
              <div className="text-sm text-gray-600">Asignado el: 2025-01-27</div>
            </div>
            <span className="bg-yellow-100 text-yellow-800 px-3 py-1 rounded text-sm">
              Pendiente
            </span>
          </div>
          <div className="mt-4">
            <button className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
              Iniciar Trabajo
            </button>
          </div>
        </div>
        
        <div className="p-4 bg-blue-50 border border-blue-200 rounded">
          <p className="text-sm text-blue-800">
            🚧 Lista completa de órdenes en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
export function Configuracion() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Configuración del Sistema</h1>
      
      <div className="space-y-4">
        {/* Sección Checklists */}
        <div className="bg-white shadow rounded p-6">
          <h2 className="font-semibold mb-4">Checklists DVIR por Tipo de Vehículo</h2>
          <div className="space-y-2">
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <span>Checklist PICKUP</span>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <span>Checklist TURBO</span>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
          </div>
        </div>
        
        {/* Sección Políticas PM */}
        <div className="bg-white shadow rounded p-6">
          <h2 className="font-semibold mb-4">Políticas de Mantenimiento Preventivo</h2>
          <div className="space-y-2">
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <div>
                <div className="font-medium">PICKUP - 10,000 km / 180 días</div>
                <div className="text-sm text-gray-600">Duración estimada: 4 horas</div>
              </div>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <div>
                <div className="font-medium">TURBO - 15,000 km / 180 días</div>
                <div className="text-sm text-gray-600">Duración estimada: 6 horas</div>
              </div>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
          </div>
        </div>
        
        <div className="p-4 bg-blue-50 border border-blue-200 rounded">
          <p className="text-sm text-blue-800">
            🚧 Configuración completa en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
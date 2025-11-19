export function DVIR() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">DVIR - Inspección Diaria del Vehículo</h1>
      
      <div className="bg-white shadow rounded p-6 mb-4">
        <h2 className="font-semibold mb-4">Información del Vehículo</h2>
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium mb-1">Placa</label>
            <input type="text" className="border rounded px-3 py-2 w-full" placeholder="ABC123" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Odómetro</label>
            <input type="number" className="border rounded px-3 py-2 w-full" placeholder="50000" />
          </div>
        </div>
        
        <h3 className="font-semibold mb-2">Checklist de Inspección</h3>
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <input type="checkbox" id="frenos" />
            <label htmlFor="frenos">Frenos</label>
          </div>
          <div className="flex items-center gap-2">
            <input type="checkbox" id="luces" />
            <label htmlFor="luces">Luces</label>
          </div>
          <div className="flex items-center gap-2">
            <input type="checkbox" id="llantas" />
            <label htmlFor="llantas">Llantas</label>
          </div>
        </div>
        
        <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded">
          <p className="text-sm text-yellow-800">
            🚧 Funcionalidad completa en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}


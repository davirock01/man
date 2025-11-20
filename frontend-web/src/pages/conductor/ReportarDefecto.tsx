export function ReportarDefecto() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Reportar Defecto o Novedad</h1>
      <div className="bg-white shadow rounded p-6">
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Vehículo</label>
            <select className="border rounded px-3 py-2 w-full">
              <option>Seleccione un vehículo...</option>
              <option>TEST123 - Toyota Hilux</option>
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-1">Tipo de Defecto</label>
            <select className="border rounded px-3 py-2 w-full">
              <option>Seleccione...</option>
              <option>Mecánico</option>
              <option>Eléctrico</option>
              <option>Carrocería</option>
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-1">Descripción</label>
            <textarea 
              className="border rounded px-3 py-2 w-full" 
              rows={4}
              placeholder="Describa el defecto encontrado..."
            ></textarea>
          </div>
          
          <button className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700">
            Reportar Defecto
          </button>
          
          <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded">
            <p className="text-sm text-yellow-800">
              🚧 Funcionalidad de reporte en desarrollo
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}


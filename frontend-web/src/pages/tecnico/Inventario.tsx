export function Inventario() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Inventario de Repuestos</h1>
      
      <div className="mb-4">
        <input
          type="text"
          placeholder="Buscar repuesto..."
          className="border rounded px-3 py-2 w-full max-w-md"
        />
      </div>
      
      <div className="bg-white shadow rounded overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left">Código</th>
              <th className="px-4 py-3 text-left">Descripción</th>
              <th className="px-4 py-3 text-left">Stock</th>
              <th className="px-4 py-3 text-left">Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t">
              <td className="px-4 py-3">REP-001</td>
              <td className="px-4 py-3">Filtro de Aceite</td>
              <td className="px-4 py-3">25</td>
              <td className="px-4 py-3">
                <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                  Disponible
                </span>
              </td>
            </tr>
            <tr className="border-t">
              <td className="px-4 py-3">REP-002</td>
              <td className="px-4 py-3">Pastillas de Freno</td>
              <td className="px-4 py-3">3</td>
              <td className="px-4 py-3">
                <span className="bg-yellow-100 text-yellow-800 px-2 py-1 rounded text-sm">
                  Stock Bajo
                </span>
              </td>
            </tr>
          </tbody>
        </table>
        
        <div className="p-4 bg-blue-50 border-t border-blue-200">
          <p className="text-sm text-blue-800">
            🚧 Inventario completo en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
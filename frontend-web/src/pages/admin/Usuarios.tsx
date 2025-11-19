export function Usuarios() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Gestión de Usuarios</h1>
      
      <div className="mb-4">
        <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          + Nuevo Usuario
        </button>
      </div>
      
      <div className="bg-white shadow rounded overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left">Nombre</th>
              <th className="px-4 py-3 text-left">Email</th>
              <th className="px-4 py-3 text-left">Rol</th>
              <th className="px-4 py-3 text-left">Estado</th>
              <th className="px-4 py-3 text-left">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t">
              <td className="px-4 py-3">María González</td>
              <td className="px-4 py-3">coordinador@test.com</td>
              <td className="px-4 py-3">
                <span className="bg-purple-100 text-purple-800 px-2 py-1 rounded text-sm">
                  COORDINADOR
                </span>
              </td>
              <td className="px-4 py-3">
                <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                  Activo
                </span>
              </td>
              <td className="px-4 py-3">
                <button className="text-blue-600 hover:underline mr-2">Editar</button>
                <button className="text-red-600 hover:underline">Desactivar</button>
              </td>
            </tr>
            <tr className="border-t">
              <td className="px-4 py-3">Juan Pérez</td>
              <td className="px-4 py-3">conductor@test.com</td>
              <td className="px-4 py-3">
                <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded text-sm">
                  CONDUCTOR
                </span>
              </td>
              <td className="px-4 py-3">
                <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                  Activo
                </span>
              </td>
              <td className="px-4 py-3">
                <button className="text-blue-600 hover:underline mr-2">Editar</button>
                <button className="text-red-600 hover:underline">Desactivar</button>
              </td>
            </tr>
          </tbody>
        </table>
        
        <div className="p-4 bg-blue-50 border-t border-blue-200">
          <p className="text-sm text-blue-800">
            🚧 Gestión completa de usuarios en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
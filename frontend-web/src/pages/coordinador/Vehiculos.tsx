export function Vehiculos() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Gestión de Vehículos</h1>
      <div className="bg-white shadow rounded p-4">
        <div className="mb-4">
          <input
            type="text"
            placeholder="Buscar por placa..."
            className="border rounded px-3 py-2 w-full max-w-md"
          />
        </div>
        <div className="text-gray-600">
          🚧 Lista de vehículos en desarrollo
        </div>
      </div>
    </div>
  );
}


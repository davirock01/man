export function MisVehiculos() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Mis Vehículos Asignados</h1>
      <div className="grid gap-4">
        <div className="bg-white shadow rounded p-4">
          <div className="flex justify-between items-center">
            <div>
              <div className="font-semibold text-lg">Vehículo TEST123</div>
              <div className="text-sm text-gray-600">Toyota Hilux 4x4</div>
            </div>
            <div className="text-green-600 font-semibold">Operativo</div>
          </div>
          <div className="mt-2 text-sm text-gray-600">
            Odómetro: 50,000 km
          </div>
        </div>
        
        <div className="p-4 bg-blue-50 border border-blue-200 rounded">
          <p className="text-sm text-blue-800">
            🚧 Lista completa de vehículos en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}


export function AdminDashboard() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Panel Administrativo</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        {/* KPI Cards */}
        <div className="bg-white shadow rounded p-6">
          <div className="text-gray-600 text-sm">Total Usuarios</div>
          <div className="text-3xl font-bold">24</div>
        </div>
        
        <div className="bg-white shadow rounded p-6">
          <div className="text-gray-600 text-sm">Total Vehículos</div>
          <div className="text-3xl font-bold">50</div>
        </div>
        
        <div className="bg-white shadow rounded p-6">
          <div className="text-gray-600 text-sm">OT Activas</div>
          <div className="text-3xl font-bold">12</div>
        </div>
      </div>
      
      <div className="bg-white shadow rounded p-6">
        <h2 className="font-semibold mb-4">Resumen del Sistema</h2>
        <div className="space-y-2 text-gray-600">
          <div>✅ Sistema operando normalmente</div>
          <div>✅ Todas las conexiones activas</div>
          <div>⚠️ 2 vehículos próximos a mantenimiento</div>
        </div>
        
        <div className="mt-4 p-4 bg-blue-50 border border-blue-200 rounded">
          <p className="text-sm text-blue-800">
            🚧 Dashboard completo en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
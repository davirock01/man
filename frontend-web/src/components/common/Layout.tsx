import { Outlet, Link, useNavigate } from 'react-router-dom';
import { useAuthStore } from '@/store/authStore';

export function Layout() {
  const { user, clearAuth } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    clearAuth();
    navigate('/login');
  };

  const getNavItems = () => {
    switch (user?.rol) {
      case 'CONDUCTOR':
        return [
          { to: '/conductor/dvir', label: 'DVIR' },
          { to: '/conductor/vehiculos', label: 'Mis Vehículos' },
          { to: '/conductor/reportar', label: 'Reportar Defecto' },
        ];
      case 'COORDINADOR':
        return [
          { to: '/dashboard', label: 'Dashboard' },
          { to: '/alertas', label: 'Alertas' },
          { to: '/vehiculos', label: 'Vehículos' },
          { to: '/ordenes-trabajo', label: 'Órdenes de Trabajo' },
        ];
      case 'TECNICO':
        return [
          { to: '/tecnico/ordenes', label: 'Mis Órdenes' },
          { to: '/tecnico/inventario', label: 'Inventario' },
        ];
      case 'ADMIN':
        return [
          { to: '/admin/dashboard', label: 'Dashboard' },
          { to: '/admin/usuarios', label: 'Usuarios' },
          { to: '/admin/configuracion', label: 'Configuración' },
        ];
      default:
        return [];
    }
  };

  const navItems = getNavItems();

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navbar */}
      <nav className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <div className="flex-shrink-0 flex items-center">
                <h1 className="text-xl font-bold text-blue-600">Fleet Maintenance</h1>
              </div>
              <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                {navItems.map((item) => (
                  <Link
                    key={item.to}
                    to={item.to}
                    className="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
                  >
                    {item.label}
                  </Link>
                ))}
              </div>
            </div>
            <div className="flex items-center">
              <span className="text-sm text-gray-700 mr-4">
                {user?.nombre} ({user?.rol})
              </span>
              <button
                onClick={handleLogout}
                className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-md text-sm font-medium"
              >
                Salir
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main content */}
      <main className="py-6">
        <Outlet />
      </main>
    </div>
  );
}


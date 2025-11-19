import { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { useAuthStore } from './store/authStore';
import { RoleGuard, getRoleDefaultPath } from './components/guards';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import { MisOrdenes } from './pages/tecnico/MisOrdenes';
import { Inventario } from './pages/tecnico/Inventario';
import { AdminDashboard } from './pages/admin/AdminDashboard';
import { Usuarios } from './pages/admin/Usuarios';
import { Configuracion } from './pages/admin/Configuracion';
// Coordinador pages
import { Alertas } from './pages/coordinador/Alertas';
import { Vehiculos } from './pages/coordinador/Vehiculos';
import { OrdenesTrabajo } from './pages/coordinador/OrdenesTrabajo';
// Conductor pages
import { DVIR } from './pages/conductor/DVIR';
import { MisVehiculos } from './pages/conductor/MisVehiculos';
import { ReportarDefecto } from './pages/conductor/ReportarDefecto';

function App() {
  const { user, initAuth } = useAuthStore();

  useEffect(() => {
    initAuth();
  }, [initAuth]);

  return (
    <Router>
      <Routes>
        {/* Login - Sin proteccion */}
        <Route path="/login" element={<Login />} />

        {/* Ruta raiz - Redirige segun rol */}
        <Route
          path="/"
          element={
            user ? (
              <Navigate to={getRoleDefaultPath(user.rol)} replace />
            ) : (
              <Navigate to="/login" replace />
            )
          }
        />

        {/* COORDINADOR - Ya existe */}
        <Route
          path="/dashboard"
          element={
            <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
              <Dashboard />
            </RoleGuard>
          }
        />
        <Route
          path="/alertas"
          element={
            <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
              <Alertas />
            </RoleGuard>
          }
        />
        <Route
          path="/vehiculos"
          element={
            <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
              <Vehiculos />
            </RoleGuard>
          }
        />
        <Route
          path="/ordenes-trabajo"
          element={
            <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
              <OrdenesTrabajo />
            </RoleGuard>
          }
        />

        {/* CONDUCTOR - Agente 2 */}
        <Route
          path="/conductor/dvir"
          element={
            <RoleGuard allowedRoles={['CONDUCTOR']}>
              <DVIR />
            </RoleGuard>
          }
        />
        <Route
          path="/conductor/vehiculos"
          element={
            <RoleGuard allowedRoles={['CONDUCTOR']}>
              <MisVehiculos />
            </RoleGuard>
          }
        />
        <Route
          path="/conductor/reportar"
          element={
            <RoleGuard allowedRoles={['CONDUCTOR']}>
              <ReportarDefecto />
            </RoleGuard>
          }
        />

        {/* TECNICO - Agente 3 */}
        <Route
          path="/tecnico/ordenes"
          element={
            <RoleGuard allowedRoles={['TECNICO']}>
              <MisOrdenes />
            </RoleGuard>
          }
        />
        <Route
          path="/tecnico/inventario"
          element={
            <RoleGuard allowedRoles={['TECNICO']}>
              <Inventario />
            </RoleGuard>
          }
        />

        {/* ADMIN - Agente 3 */}
        <Route
          path="/admin/dashboard"
          element={
            <RoleGuard allowedRoles={['ADMIN']}>
              <AdminDashboard />
            </RoleGuard>
          }
        />
        <Route
          path="/admin/usuarios"
          element={
            <RoleGuard allowedRoles={['ADMIN']}>
              <Usuarios />
            </RoleGuard>
          }
        />
        <Route
          path="/admin/configuracion"
          element={
            <RoleGuard allowedRoles={['ADMIN']}>
              <Configuracion />
            </RoleGuard>
          }
        />

        {/* Catch all - Redirige al login */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </Router>
  );
}

export default App;

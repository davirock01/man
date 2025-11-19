import { Navigate } from 'react-router-dom';
import { useAuthStore } from '../../store/authStore';

interface RoleGuardProps {
  allowedRoles: string[];
  children: React.ReactNode;
}

export function RoleGuard({ allowedRoles, children }: RoleGuardProps) {
  const user = useAuthStore((state) => state.user);

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (!allowedRoles.includes(user.rol)) {
    return <Navigate to={getRoleDefaultPath(user.rol)} replace />;
  }

  return <>{children}</>;
}

function getRoleDefaultPath(rol: string): string {
  switch (rol) {
    case 'CONDUCTOR':
      return '/conductor/dvir';
    case 'COORDINADOR':
      return '/dashboard';
    case 'TECNICO':
      return '/tecnico/ordenes';
    case 'ADMIN':
      return '/admin/dashboard';
    default:
      return '/';
  }
}

export { getRoleDefaultPath };

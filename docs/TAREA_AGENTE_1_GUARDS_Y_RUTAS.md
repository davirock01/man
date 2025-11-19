# 🎯 TAREA AGENTE 1: GUARDS DE AUTENTICACIÓN Y RUTAS BASE

**Asignado a**: Agente 1 (Claude/Gemini)  
**Prioridad**: CRÍTICA - Los otros agentes dependen de esto  
**Tiempo estimado**: 45 minutos  
**Inicio**: INMEDIATO

---

## 🎯 TU RESPONSABILIDAD

Crear la infraestructura base de autenticación por roles:
1. Guards de protección de rutas
2. Estructura base de rutas en App.tsx
3. Helpers de redirección por rol

**Los otros 2 agentes esperan que termines esto primero.**

---

## 📍 UBICACIÓN

```
C:\Users\User-PC\Desktop\software engineering\app\man\man\frontend-web
```

Frontend corriendo en: http://localhost:3000

---

## 📝 DOCUMENTACIÓN OBLIGATORIA

**Archivo**: `docs/AGENTE_1_LOG.md`

**Formato**:
```markdown
## [HH:MM] - Agente 1 - Acción
- Archivo: [ruta]
- Qué hice: [descripción]
- Estado: OK / ERROR
```

---

## ✅ CHECKLIST (Orden estricto)

### PASO 1: Crear Guards (20 min)

- [ ] **1.1** Leer `src/store/authStore.ts` para entender estructura de user
- [ ] **1.2** Crear carpeta: `src/components/guards`
- [ ] **1.3** Crear `src/components/guards/RoleGuard.tsx`:

```typescript
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
```

- [ ] **1.4** Crear `src/components/guards/ProtectedRoute.tsx`:

```typescript
import { Navigate } from 'react-router-dom';
import { useAuthStore } from '../../store/authStore';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const user = useAuthStore((state) => state.user);
  
  if (!user) {
    return <Navigate to="/login" replace />;
  }
  
  return <>{children}</>;
}
```

- [ ] **1.5** Crear `src/components/guards/index.ts`:

```typescript
export { RoleGuard } from './RoleGuard';
export { ProtectedRoute } from './ProtectedRoute';
```

- [ ] **1.6** Documentar en `docs/AGENTE_1_LOG.md`
- [ ] **1.7** Verificar que compila sin errores

---

### PASO 2: Modificar App.tsx con Rutas Base (25 min)

- [ ] **2.1** Leer `src/App.tsx` actual
- [ ] **2.2** Agregar imports de guards
- [ ] **2.3** Modificar rutas con estructura por rol:

```typescript
import { RoleGuard } from './components/guards';
import { Dashboard } from './pages/Dashboard';
import { Login } from './pages/Login';
// Los otros componentes los crearán Agentes 2 y 3

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Login - Sin protección */}
        <Route path="/login" element={<Login />} />
        
        {/* Ruta raíz - Redirige según rol */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        
        {/* COORDINADOR - Ya existe */}
        <Route path="/dashboard" element={
          <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
            <Dashboard />
          </RoleGuard>
        } />
        <Route path="/alertas" element={
          <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
            {/* Agente 2 creará este componente */}
            <div>Alertas - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/vehiculos" element={
          <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
            {/* Agente 2 creará este componente */}
            <div>Vehículos - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/ordenes-trabajo" element={
          <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
            {/* Agente 2 creará este componente */}
            <div>Órdenes de Trabajo - Pendiente</div>
          </RoleGuard>
        } />
        
        {/* CONDUCTOR - Agente 2 */}
        <Route path="/conductor/dvir" element={
          <RoleGuard allowedRoles={['CONDUCTOR']}>
            {/* Placeholder - Agente 2 creará */}
            <div>DVIR - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/conductor/vehiculos" element={
          <RoleGuard allowedRoles={['CONDUCTOR']}>
            <div>Mis Vehículos - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/conductor/reportar" element={
          <RoleGuard allowedRoles={['CONDUCTOR']}>
            <div>Reportar - Pendiente</div>
          </RoleGuard>
        } />
        
        {/* TÉCNICO - Agente 3 */}
        <Route path="/tecnico/ordenes" element={
          <RoleGuard allowedRoles={['TECNICO']}>
            {/* Placeholder - Agente 3 creará */}
            <div>Mis Órdenes - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/tecnico/inventario" element={
          <RoleGuard allowedRoles={['TECNICO']}>
            <div>Inventario - Pendiente</div>
          </RoleGuard>
        } />
        
        {/* ADMIN - Agente 3 */}
        <Route path="/admin/dashboard" element={
          <RoleGuard allowedRoles={['ADMIN']}>
            {/* Placeholder - Agente 3 creará */}
            <div>Admin Dashboard - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/admin/usuarios" element={
          <RoleGuard allowedRoles={['ADMIN']}>
            <div>Usuarios - Pendiente</div>
          </RoleGuard>
        } />
        <Route path="/admin/configuracion" element={
          <RoleGuard allowedRoles={['ADMIN']}>
            <div>Configuración - Pendiente</div>
          </RoleGuard>
        } />
        
        {/* Catch all - Redirige al login */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
```

- [ ] **2.4** Guardar y verificar que compila
- [ ] **2.5** Documentar cambios

---

### PASO 3: Pruebas Básicas (10 min)

- [ ] **3.1** Abrir http://localhost:3000
- [ ] **3.2** Login como coordinador@test.com / testpass123
- [ ] **3.3** Verificar que puedes acceder a /dashboard
- [ ] **3.4** Intentar ir a /conductor/dvir manualmente → Debe redirigir a /dashboard
- [ ] **3.5** Hacer logout
- [ ] **3.6** Login como conductor@test.com / testpass123
- [ ] **3.7** Debe redirigir a /conductor/dvir (aunque sea placeholder)
- [ ] **3.8** Intentar ir a /dashboard manualmente → Debe redirigir a /conductor/dvir
- [ ] **3.9** Documentar resultados de pruebas

---

### PASO 4: Notificar Completado

- [ ] **4.1** Crear `docs/AGENTE_1_COMPLETADO.md`:

```markdown
# ✅ AGENTE 1 - COMPLETADO

## Archivos Creados:
- src/components/guards/RoleGuard.tsx
- src/components/guards/ProtectedRoute.tsx
- src/components/guards/index.ts

## Archivos Modificados:
- src/App.tsx - Agregadas rutas protegidas por rol

## Pruebas:
✅ Coordinador puede acceder a /dashboard
✅ Coordinador NO puede acceder a /conductor/dvir
✅ Conductor puede acceder a /conductor/dvir
✅ Conductor NO puede acceder a /dashboard

## Estado:
COMPLETADO - Agentes 2 y 3 pueden continuar

## Problemas:
[Ninguno / Lista de problemas encontrados]
```

- [ ] **4.2** Avisar al supervisor: "Agente 1 completado, guards funcionando"

---

## 🚨 SI ALGO FALLA

**DETENTE y reporta**:
```
🚨 AGENTE 1 - PROBLEMA
Paso: [número]
Error: [mensaje]
Archivo: [ruta]
```

---

## ✅ CRITERIOS DE ÉXITO

- [ ] Guards creados y funcionando
- [ ] Rutas protegidas en App.tsx
- [ ] Redirección automática funciona
- [ ] Coordinador ve dashboard, Conductor ve su menú
- [ ] Sin errores de compilación
- [ ] Documentación completa

---

**TIEMPO TOTAL**: 45 minutos  
**INICIO**: AHORA  
**PRIORIDAD**: CRÍTICA (bloquea a otros agentes)


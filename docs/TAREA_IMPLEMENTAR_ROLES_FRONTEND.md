# 🎯 TAREA CRÍTICA: IMPLEMENTAR CONTROL DE ACCESO POR ROLES EN FRONTEND

**Asignado a**: Agente Frontend (Claude/Gemini - el que responda primero)  
**Prioridad**: ALTA  
**Fecha**: 2025-01-27  
**Supervisor**: Director de Proyecto  
**Tiempo estimado**: 1-2 horas

---

## 📋 OBJETIVO

Implementar control de acceso basado en roles (RBAC) en el frontend React para que cada usuario vea SOLO las pantallas y funcionalidades de su rol.

---

## 🚨 REGLAS OBLIGATORIAS

1. ✅ **NO uses Docker ni terminal** - Solo edita archivos del frontend
2. ✅ **Documenta CADA cambio** en `docs/REGISTRO_IMPLEMENTACION_ROLES.md`
3. ✅ **Usa el formato**: `[HH:MM] - Agente X - Archivo modificado - Qué hiciste`
4. ✅ **Prueba cada cambio** navegando en http://localhost:3000
5. ✅ **NO rompas funcionalidad existente** - Solo agrega/modifica control de roles
6. ✅ **Si algo falla, DOCUMÉNTALO** y pide ayuda al supervisor

---

## 📍 UBICACIÓN DE TRABAJO

```
C:\Users\User-PC\Desktop\software engineering\app\man\man\frontend-web
```

**Frontend ya está corriendo en**: http://localhost:3000

---

## 🎭 ROLES Y PANTALLAS REQUERIDAS

### CONDUCTOR
**Pantallas**:
- `/conductor/dvir` - Hacer inspección DVIR
- `/conductor/vehiculos` - Ver mis vehículos asignados
- `/conductor/reportar` - Reportar defectos

**Navegación**: Solo esas 3 opciones en el menú

---

### COORDINADOR (Ya existe pero verificar)
**Pantallas**:
- `/dashboard` - Dashboard con 3 paneles (Alertas Predictivas, Reactivas, Patrones)
- `/alertas` - Ver todas las alertas
- `/vehiculos` - Gestionar vehículos
- `/ordenes-trabajo` - Crear y asignar OT

**Navegación**: Dashboard, Alertas, Vehículos, Órdenes de Trabajo

---

### TÉCNICO
**Pantallas**:
- `/tecnico/ordenes` - Mis órdenes de trabajo asignadas
- `/tecnico/inventario` - Ver inventario de repuestos
- `/tecnico/orden/:id` - Actualizar estado de OT

**Navegación**: Mis Órdenes, Inventario

---

### ADMIN
**Pantallas**:
- `/admin/dashboard` - Dashboard administrativo
- `/admin/vehiculos` - Gestionar vehículos
- `/admin/usuarios` - Gestionar usuarios y permisos
- `/admin/configuracion` - Configurar checklists y políticas

**Navegación**: Dashboard, Vehículos, Usuarios, Configuración

---

## 📝 CHECKLIST DE IMPLEMENTACIÓN (ORDEN ESTRICTO)

### FASE 1: Preparación (15 min)

- [ ] **1.1** Leer archivo actual: `src/App.tsx`
- [ ] **1.2** Leer archivo actual: `src/pages/Dashboard.tsx`
- [ ] **1.3** Leer archivo actual: `src/components/common/Layout.tsx`
- [ ] **1.4** Crear documento: `docs/REGISTRO_IMPLEMENTACION_ROLES.md`
- [ ] **1.5** Documentar estado inicial

**Formato de documentación**:
```markdown
## [12:00] - Agente Claude - FASE 1 INICIADA
- Leí App.tsx
- Estado actual: Solo ruta /dashboard para todos los roles
```

---

### FASE 2: Crear Guards de Autenticación (20 min)

- [ ] **2.1** Crear `src/components/guards/RoleGuard.tsx`
  - Componente que verifica el rol del usuario
  - Si no tiene permiso, redirige a su dashboard correspondiente
  
- [ ] **2.2** Crear `src/components/guards/ProtectedRoute.tsx`
  - Wrapper para rutas protegidas por autenticación

- [ ] **2.3** Documentar cambios

**Código esperado para RoleGuard.tsx**:
```typescript
import { Navigate } from 'react-router-dom';
import { useAuthStore } from '@/store/authStore';

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
    // Redirigir a su dashboard correspondiente
    return <Navigate to={getRoleDefaultPath(user.rol)} replace />;
  }
  
  return <>{children}</>;
}

function getRoleDefaultPath(rol: string): string {
  switch (rol) {
    case 'CONDUCTOR': return '/conductor/dvir';
    case 'COORDINADOR': return '/dashboard';
    case 'TECNICO': return '/tecnico/ordenes';
    case 'ADMIN': return '/admin/dashboard';
    default: return '/';
  }
}
```

- [ ] **2.4** Probar que compile: Guardar archivo y verificar que no hay errores en terminal del frontend

---

### FASE 3: Crear Páginas por Rol (40 min)

**CONDUCTOR**:
- [ ] **3.1** Crear `src/pages/conductor/DVIR.tsx` (placeholder con mensaje "Módulo DVIR - En construcción")
- [ ] **3.2** Crear `src/pages/conductor/MisVehiculos.tsx` (placeholder)
- [ ] **3.3** Crear `src/pages/conductor/ReportarDefecto.tsx` (placeholder)
- [ ] **3.4** Documentar creación

**TÉCNICO**:
- [ ] **3.5** Crear `src/pages/tecnico/MisOrdenes.tsx` (placeholder)
- [ ] **3.6** Crear `src/pages/tecnico/Inventario.tsx` (placeholder)
- [ ] **3.7** Documentar creación

**ADMIN**:
- [ ] **3.8** Crear `src/pages/admin/Dashboard.tsx` (placeholder)
- [ ] **3.9** Crear `src/pages/admin/Usuarios.tsx` (placeholder con tabla de usuarios)
- [ ] **3.10** Crear `src/pages/admin/Configuracion.tsx` (placeholder)
- [ ] **3.11** Documentar creación

**Formato de placeholder**:
```typescript
export function DVIR() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">DVIR - Inspección Diaria</h1>
      <div className="bg-yellow-50 border border-yellow-200 p-4 rounded">
        <p className="text-yellow-800">
          🚧 Módulo en construcción - Próximamente disponible
        </p>
      </div>
    </div>
  );
}
```

---

### FASE 4: Modificar Rutas en App.tsx (20 min)

- [ ] **4.1** Leer `src/App.tsx` actual
- [ ] **4.2** Agregar imports de nuevas páginas y guards
- [ ] **4.3** Modificar rutas usando RoleGuard
- [ ] **4.4** Documentar cambios

**Estructura esperada**:
```typescript
import { RoleGuard } from './components/guards/RoleGuard';
// ... otros imports

<Routes>
  <Route path="/login" element={<Login />} />
  
  {/* Rutas COORDINADOR */}
  <Route path="/dashboard" element={
    <RoleGuard allowedRoles={['COORDINADOR', 'ADMIN']}>
      <Dashboard />
    </RoleGuard>
  } />
  
  {/* Rutas CONDUCTOR */}
  <Route path="/conductor/dvir" element={
    <RoleGuard allowedRoles={['CONDUCTOR']}>
      <DVIR />
    </RoleGuard>
  } />
  
  {/* ... más rutas */}
</Routes>
```

- [ ] **4.5** Probar que compile sin errores

---

### FASE 5: Modificar Navegación por Rol (30 min)

- [ ] **5.1** Leer `src/components/common/Layout.tsx`
- [ ] **5.2** Modificar navegación para mostrar links según rol
- [ ] **5.3** Documentar cambios

**Lógica esperada**:
```typescript
const user = useAuthStore((state) => state.user);

const getNavItems = () => {
  switch (user?.rol) {
    case 'CONDUCTOR':
      return [
        { to: '/conductor/dvir', label: 'DVIR' },
        { to: '/conductor/vehiculos', label: 'Mis Vehículos' },
        { to: '/conductor/reportar', label: 'Reportar' },
      ];
    case 'COORDINADOR':
      return [
        { to: '/dashboard', label: 'Dashboard' },
        { to: '/alertas', label: 'Alertas' },
        // ... etc
      ];
    // ... otros roles
  }
};
```

- [ ] **5.4** Probar visualmente en http://localhost:3000

---

### FASE 6: PRUEBAS (30 min)

**Para CADA rol, hacer lo siguiente**:

#### Test COORDINADOR:
- [ ] **6.1** Hacer logout
- [ ] **6.2** Login con: coordinador@test.com / testpass123
- [ ] **6.3** Verificar que ve: Dashboard, Alertas, Vehículos, Órdenes de Trabajo
- [ ] **6.4** Intentar navegar a /conductor/dvir manualmente (debe redirigir)
- [ ] **6.5** Documentar resultado

#### Test CONDUCTOR:
- [ ] **6.6** Hacer logout
- [ ] **6.7** Login con: conductor@test.com / testpass123
- [ ] **6.8** Verificar que ve: DVIR, Mis Vehículos, Reportar
- [ ] **6.9** Verificar que NO ve opciones de coordinador
- [ ] **6.10** Intentar navegar a /dashboard manualmente (debe redirigir)
- [ ] **6.11** Documentar resultado

#### Test TÉCNICO:
- [ ] **6.12** Hacer logout
- [ ] **6.13** Login con: tecnico@test.com / testpass123
- [ ] **6.14** Verificar que ve: Mis Órdenes, Inventario
- [ ] **6.15** Verificar que NO ve opciones de otros roles
- [ ] **6.16** Documentar resultado

#### Test ADMIN:
- [ ] **6.17** Hacer logout
- [ ] **6.18** Login con: admin@test.com / testpass123
- [ ] **6.19** Verificar que ve: Dashboard, Vehículos, Usuarios, Configuración
- [ ] **6.20** Verificar que puede acceder a TODO
- [ ] **6.21** Documentar resultado

---

### FASE 7: Documentación Final (15 min)

- [ ] **7.1** Actualizar `docs/REGISTRO_IMPLEMENTACION_ROLES.md` con resumen
- [ ] **7.2** Crear `docs/COMO_PROBAR_ROLES.md` con instrucciones para usuario final
- [ ] **7.3** Listar archivos modificados/creados
- [ ] **7.4** Reportar al supervisor

**Formato de resumen**:
```markdown
## RESUMEN FINAL

### Archivos Creados:
- src/components/guards/RoleGuard.tsx
- src/components/guards/ProtectedRoute.tsx
- src/pages/conductor/DVIR.tsx
- ... (lista completa)

### Archivos Modificados:
- src/App.tsx - Agregadas rutas por rol
- src/components/common/Layout.tsx - Navegación dinámica
- ... (lista completa)

### Pruebas Realizadas:
✅ COORDINADOR - Funciona correctamente
✅ CONDUCTOR - Funciona correctamente
✅ TÉCNICO - Funciona correctamente
✅ ADMIN - Funciona correctamente

### Problemas Encontrados:
- [Si hubo alguno, listarlo aquí]

### Estado Final:
COMPLETADO ✅ / PARCIAL ⚠️ / FALLIDO ❌
```

---

## 🚨 PUNTOS DE CONTROL (CHECKPOINTS)

**Después de cada fase, DEBES**:
1. Documentar en `REGISTRO_IMPLEMENTACION_ROLES.md`
2. Verificar que el frontend compile sin errores
3. Probar navegando en http://localhost:3000
4. Si algo falla, DETENTE y documenta el error

**NO continues a la siguiente fase si la actual tiene errores**

---

## 📞 COMUNICACIÓN CON SUPERVISOR

**Reporta INMEDIATAMENTE si**:
- Encuentras un error que no puedes resolver en 10 minutos
- Un archivo no existe donde se esperaba
- El frontend no compila
- Las pruebas no pasan

**Formato de reporte**:
```
🚨 PROBLEMA EN FASE X
Archivo: [ruta]
Error: [mensaje exacto]
Qué intenté: [tus acciones]
```

---

## ✅ CRITERIOS DE ÉXITO

La tarea está COMPLETADA cuando:
1. ✅ Los 4 roles ven pantallas diferentes
2. ✅ Cada rol solo puede acceder a sus rutas
3. ✅ La navegación muestra solo opciones permitidas para cada rol
4. ✅ Todas las pruebas (Fase 6) pasan
5. ✅ La documentación está completa
6. ✅ No hay errores en consola del navegador
7. ✅ El frontend compila sin warnings críticos

---

## 🎯 ENTREGABLES

1. Código modificado en `frontend-web/src`
2. `docs/REGISTRO_IMPLEMENTACION_ROLES.md` - Log detallado
3. `docs/COMO_PROBAR_ROLES.md` - Guía de pruebas
4. Screenshots o descripción de cada rol funcionando

---

## ⏱️ TIEMPO ESTIMADO POR FASE

- Fase 1: 15 min
- Fase 2: 20 min
- Fase 3: 40 min
- Fase 4: 20 min
- Fase 5: 30 min
- Fase 6: 30 min
- Fase 7: 15 min

**Total**: ~2 horas 50 minutos

---

## 🔥 PRIORIDAD DE IMPLEMENTACIÓN

Si tienes poco tiempo, implementa en este orden:
1. PRIMERO: Guards y rutas básicas (Fases 1-4)
2. SEGUNDO: Navegación dinámica (Fase 5)
3. TERCERO: Páginas de placeholders (Fase 3)
4. ÚLTIMO: Pruebas exhaustivas (Fase 6)

---

**¡COMIENZA AHORA! Documenta tu inicio en el REGISTRO.**


# 🎯 TAREA AGENTE 2: PÁGINAS COORDINADOR Y CONDUCTOR

**Asignado a**: Agente 2 (Claude/Gemini)  
**Prioridad**: ALTA  
**Tiempo estimado**: 60 minutos  
**Depende de**: Agente 1 debe terminar primero

---

## ⏸️ ESPERA A AGENTE 1

**NO COMIENCES** hasta que veas el archivo:
```
docs/AGENTE_1_COMPLETADO.md
```

Cuando lo veas, puedes empezar.

---

## 🎯 TU RESPONSABILIDAD

Crear páginas y componentes para:
1. **COORDINADOR**: Alertas, Vehículos, Órdenes de Trabajo
2. **CONDUCTOR**: DVIR, Mis Vehículos, Reportar Defecto
3. Navegación dinámica para estos roles

---

## 📍 UBICACIÓN

```
C:\Users\User-PC\Desktop\software engineering\app\man\man\frontend-web
```

---

## 📝 DOCUMENTACIÓN

**Archivo**: `docs/AGENTE_2_LOG.md`

**Formato**:
```markdown
## [HH:MM] - Agente 2 - Acción
- Archivo: [ruta]
- Qué hice: [descripción]
- Estado: OK / ERROR
```

---

## ✅ CHECKLIST

### PARTE 1: Páginas COORDINADOR (25 min)

- [ ] **1.1** Crear `src/pages/coordinador/Alertas.tsx`:

```typescript
export function Alertas() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Alertas del Sistema</h1>
      <div className="grid gap-4">
        {/* Alertas Predictivas */}
        <div className="bg-yellow-50 border border-yellow-200 p-4 rounded">
          <h3 className="font-semibold text-yellow-800 mb-2">⚠️ Alertas Predictivas</h3>
          <p className="text-sm text-yellow-700">Vehículos próximos a mantenimiento preventivo</p>
          <div className="mt-2 text-yellow-900">
            🚧 Módulo en desarrollo - Próximamente disponible
          </div>
        </div>
        
        {/* Alertas Reactivas */}
        <div className="bg-red-50 border border-red-200 p-4 rounded">
          <h3 className="font-semibold text-red-800 mb-2">🚨 Alertas Reactivas</h3>
          <p className="text-sm text-red-700">Defectos reportados que requieren atención</p>
          <div className="mt-2 text-red-900">
            🚧 Módulo en desarrollo - Próximamente disponible
          </div>
        </div>
        
        {/* Patrones Recurrentes */}
        <div className="bg-blue-50 border border-blue-200 p-4 rounded">
          <h3 className="font-semibold text-blue-800 mb-2">🔄 Patrones Recurrentes</h3>
          <p className="text-sm text-blue-700">Fallas que se repiten en la flota</p>
          <div className="mt-2 text-blue-900">
            🚧 Módulo en desarrollo - Próximamente disponible
          </div>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **1.2** Crear `src/pages/coordinador/Vehiculos.tsx`:

```typescript
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
```

- [ ] **1.3** Crear `src/pages/coordinador/OrdenesTrabajo.tsx`:

```typescript
export function OrdenesTrabajo() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Órdenes de Trabajo</h1>
      <div className="mb-4">
        <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          + Nueva Orden de Trabajo
        </button>
      </div>
      <div className="bg-white shadow rounded p-4">
        <div className="text-gray-600">
          🚧 Lista de OT en desarrollo
        </div>
      </div>
    </div>
  );
}
```

- [ ] **1.4** Actualizar `src/App.tsx` - Reemplazar placeholders de coordinador con componentes reales
- [ ] **1.5** Documentar en `docs/AGENTE_2_LOG.md`

---

### PARTE 2: Páginas CONDUCTOR (25 min)

- [ ] **2.1** Crear carpeta: `src/pages/conductor`
- [ ] **2.2** Crear `src/pages/conductor/DVIR.tsx`:

```typescript
export function DVIR() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">DVIR - Inspección Diaria del Vehículo</h1>
      
      <div className="bg-white shadow rounded p-6 mb-4">
        <h2 className="font-semibold mb-4">Información del Vehículo</h2>
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium mb-1">Placa</label>
            <input type="text" className="border rounded px-3 py-2 w-full" placeholder="ABC123" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Odómetro</label>
            <input type="number" className="border rounded px-3 py-2 w-full" placeholder="50000" />
          </div>
        </div>
        
        <h3 className="font-semibold mb-2">Checklist de Inspección</h3>
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <input type="checkbox" id="frenos" />
            <label htmlFor="frenos">Frenos</label>
          </div>
          <div className="flex items-center gap-2">
            <input type="checkbox" id="luces" />
            <label htmlFor="luces">Luces</label>
          </div>
          <div className="flex items-center gap-2">
            <input type="checkbox" id="llantas" />
            <label htmlFor="llantas">Llantas</label>
          </div>
        </div>
        
        <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded">
          <p className="text-sm text-yellow-800">
            🚧 Funcionalidad completa en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **2.3** Crear `src/pages/conductor/MisVehiculos.tsx`:

```typescript
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
```

- [ ] **2.4** Crear `src/pages/conductor/ReportarDefecto.tsx`:

```typescript
export function ReportarDefecto() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Reportar Defecto o Novedad</h1>
      <div className="bg-white shadow rounded p-6">
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1">Vehículo</label>
            <select className="border rounded px-3 py-2 w-full">
              <option>Seleccione un vehículo...</option>
              <option>TEST123 - Toyota Hilux</option>
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-1">Tipo de Defecto</label>
            <select className="border rounded px-3 py-2 w-full">
              <option>Seleccione...</option>
              <option>Mecánico</option>
              <option>Eléctrico</option>
              <option>Carrocería</option>
            </select>
          </div>
          
          <div>
            <label className="block text-sm font-medium mb-1">Descripción</label>
            <textarea 
              className="border rounded px-3 py-2 w-full" 
              rows={4}
              placeholder="Describa el defecto encontrado..."
            ></textarea>
          </div>
          
          <button className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700">
            Reportar Defecto
          </button>
          
          <div className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded">
            <p className="text-sm text-yellow-800">
              🚧 Funcionalidad de reporte en desarrollo
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **2.5** Actualizar `src/App.tsx` - Reemplazar placeholders de conductor con componentes reales
- [ ] **2.6** Documentar cambios

---

### PARTE 3: Navegación Dinámica (10 min)

- [ ] **3.1** Leer `src/components/common/Layout.tsx`
- [ ] **3.2** Modificar navegación para mostrar menú según rol:

```typescript
import { useAuthStore } from '../../store/authStore';
import { Link } from 'react-router-dom';

export function Layout() {
  const user = useAuthStore((state) => state.user);
  
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
    <div>
      <nav className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between h-16">
            <div className="flex space-x-4">
              {navItems.map((item) => (
                <Link
                  key={item.to}
                  to={item.to}
                  className="inline-flex items-center px-3 text-gray-700 hover:text-blue-600"
                >
                  {item.label}
                </Link>
              ))}
            </div>
            <div className="flex items-center">
              <span className="mr-4">{user?.nombre} ({user?.rol})</span>
              <button className="text-red-600" onClick={/* logout */}>
                Salir
              </button>
            </div>
          </div>
        </div>
      </nav>
      {/* contenido */}
    </div>
  );
}
```

- [ ] **3.3** Documentar cambios

---

### PASO 4: Pruebas (15 min)

#### Test COORDINADOR:
- [ ] **4.1** Login: coordinador@test.com / testpass123
- [ ] **4.2** Verificar menú: Dashboard, Alertas, Vehículos, Órdenes de Trabajo
- [ ] **4.3** Navegar a cada página, verificar que carga
- [ ] **4.4** Intentar ir a /conductor/dvir → Debe redirigir

#### Test CONDUCTOR:
- [ ] **4.5** Logout y login: conductor@test.com / testpass123
- [ ] **4.6** Verificar menú: DVIR, Mis Vehículos, Reportar Defecto
- [ ] **4.7** Navegar a cada página, verificar que carga
- [ ] **4.8** Intentar ir a /dashboard → Debe redirigir

- [ ] **4.9** Documentar resultados

---

### PASO 5: Completar

- [ ] **5.1** Crear `docs/AGENTE_2_COMPLETADO.md`:

```markdown
# ✅ AGENTE 2 - COMPLETADO

## Archivos Creados:
- src/pages/coordinador/Alertas.tsx
- src/pages/coordinador/Vehiculos.tsx
- src/pages/coordinador/OrdenesTrabajo.tsx
- src/pages/conductor/DVIR.tsx
- src/pages/conductor/MisVehiculos.tsx
- src/pages/conductor/ReportarDefecto.tsx

## Archivos Modificados:
- src/App.tsx - Agregados componentes reales
- src/components/common/Layout.tsx - Navegación dinámica

## Pruebas:
✅ Coordinador ve su menú y páginas
✅ Conductor ve su menú y páginas
✅ Redirecciones funcionan

## Estado: COMPLETADO
```

---

## ✅ CRITERIOS DE ÉXITO

- [ ] 6 páginas creadas (3 coordinador, 3 conductor)
- [ ] Navegación muestra opciones correctas por rol
- [ ] Todas las páginas cargan sin errores
- [ ] Pruebas pasan para ambos roles

**TIEMPO**: 60 minutos  
**ESPERA A**: Agente 1


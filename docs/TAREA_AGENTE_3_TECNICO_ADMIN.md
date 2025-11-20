# 🎯 TAREA AGENTE 3: PÁGINAS TÉCNICO Y ADMIN

**Asignado a**: Agente 3 (Claude/Gemini)  
**Prioridad**: ALTA  
**Tiempo estimado**: 50 minutos  
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
1. **TÉCNICO**: Mis Órdenes de Trabajo, Inventario
2. **ADMIN**: Dashboard, Usuarios, Configuración

---

## 📍 UBICACIÓN

```
C:\Users\User-PC\Desktop\software engineering\app\man\man\frontend-web
```

---

## 📝 DOCUMENTACIÓN

**Archivo**: `docs/AGENTE_3_LOG.md`

**Formato**:
```markdown
## [HH:MM] - Agente 3 - Acción
- Archivo: [ruta]
- Qué hice: [descripción]
- Estado: OK / ERROR
```

---

## ✅ CHECKLIST

### PARTE 1: Páginas TÉCNICO (20 min)

- [ ] **1.1** Crear carpeta: `src/pages/tecnico`
- [ ] **1.2** Crear `src/pages/tecnico/MisOrdenes.tsx`:

```typescript
export function MisOrdenes() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Mis Órdenes de Trabajo</h1>
      
      <div className="mb-4">
        <div className="flex gap-2">
          <button className="px-4 py-2 bg-blue-600 text-white rounded">Pendientes</button>
          <button className="px-4 py-2 bg-gray-200 rounded">En Progreso</button>
          <button className="px-4 py-2 bg-gray-200 rounded">Completadas</button>
        </div>
      </div>
      
      <div className="space-y-4">
        {/* OT de ejemplo */}
        <div className="bg-white shadow rounded p-4">
          <div className="flex justify-between items-start">
            <div>
              <div className="font-semibold text-lg">OT-001 - Mantenimiento Preventivo</div>
              <div className="text-sm text-gray-600">Vehículo: TEST123 - Toyota Hilux</div>
              <div className="text-sm text-gray-600">Asignado el: 2025-01-27</div>
            </div>
            <span className="bg-yellow-100 text-yellow-800 px-3 py-1 rounded text-sm">
              Pendiente
            </span>
          </div>
          <div className="mt-4">
            <button className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
              Iniciar Trabajo
            </button>
          </div>
        </div>
        
        <div className="p-4 bg-blue-50 border border-blue-200 rounded">
          <p className="text-sm text-blue-800">
            🚧 Lista completa de órdenes en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **1.3** Crear `src/pages/tecnico/Inventario.tsx`:

```typescript
export function Inventario() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Inventario de Repuestos</h1>
      
      <div className="mb-4">
        <input
          type="text"
          placeholder="Buscar repuesto..."
          className="border rounded px-3 py-2 w-full max-w-md"
        />
      </div>
      
      <div className="bg-white shadow rounded overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left">Código</th>
              <th className="px-4 py-3 text-left">Descripción</th>
              <th className="px-4 py-3 text-left">Stock</th>
              <th className="px-4 py-3 text-left">Estado</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t">
              <td className="px-4 py-3">REP-001</td>
              <td className="px-4 py-3">Filtro de Aceite</td>
              <td className="px-4 py-3">25</td>
              <td className="px-4 py-3">
                <span className="bg-green-100 text-green-800 px-2 py-1 rounded text-sm">
                  Disponible
                </span>
              </td>
            </tr>
            <tr className="border-t">
              <td className="px-4 py-3">REP-002</td>
              <td className="px-4 py-3">Pastillas de Freno</td>
              <td className="px-4 py-3">3</td>
              <td className="px-4 py-3">
                <span className="bg-yellow-100 text-yellow-800 px-2 py-1 rounded text-sm">
                  Stock Bajo
                </span>
              </td>
            </tr>
          </tbody>
        </table>
        
        <div className="p-4 bg-blue-50 border-t border-blue-200">
          <p className="text-sm text-blue-800">
            🚧 Inventario completo en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **1.4** Actualizar `src/App.tsx` - Reemplazar placeholders de técnico
- [ ] **1.5** Documentar cambios

---

### PARTE 2: Páginas ADMIN (25 min)

- [ ] **2.1** Crear carpeta: `src/pages/admin`
- [ ] **2.2** Crear `src/pages/admin/AdminDashboard.tsx`:

```typescript
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
```

- [ ] **2.3** Crear `src/pages/admin/Usuarios.tsx`:

```typescript
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
```

- [ ] **2.4** Crear `src/pages/admin/Configuracion.tsx`:

```typescript
export function Configuracion() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Configuración del Sistema</h1>
      
      <div className="space-y-4">
        {/* Sección Checklists */}
        <div className="bg-white shadow rounded p-6">
          <h2 className="font-semibold mb-4">Checklists DVIR por Tipo de Vehículo</h2>
          <div className="space-y-2">
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <span>Checklist PICKUP</span>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <span>Checklist TURBO</span>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
          </div>
        </div>
        
        {/* Sección Políticas PM */}
        <div className="bg-white shadow rounded p-6">
          <h2 className="font-semibold mb-4">Políticas de Mantenimiento Preventivo</h2>
          <div className="space-y-2">
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <div>
                <div className="font-medium">PICKUP - 10,000 km / 180 días</div>
                <div className="text-sm text-gray-600">Duración estimada: 4 horas</div>
              </div>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded">
              <div>
                <div className="font-medium">TURBO - 15,000 km / 180 días</div>
                <div className="text-sm text-gray-600">Duración estimada: 6 horas</div>
              </div>
              <button className="text-blue-600 hover:underline">Editar</button>
            </div>
          </div>
        </div>
        
        <div className="p-4 bg-blue-50 border border-blue-200 rounded">
          <p className="text-sm text-blue-800">
            🚧 Configuración completa en desarrollo
          </p>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **2.5** Actualizar `src/App.tsx` - Reemplazar placeholders de admin
- [ ] **2.6** Documentar cambios

---

### PARTE 3: Pruebas (15 min)

#### Test TÉCNICO:
- [ ] **3.1** Login: tecnico@test.com / testpass123
- [ ] **3.2** Verificar menú: Mis Órdenes, Inventario
- [ ] **3.3** Navegar a cada página, verificar que carga
- [ ] **3.4** Intentar ir a /dashboard → Debe redirigir

#### Test ADMIN:
- [ ] **3.5** Logout y login: admin@test.com / testpass123
- [ ] **3.6** Verificar menú: Dashboard, Usuarios, Configuración
- [ ] **3.7** Navegar a cada página, verificar que carga
- [ ] **3.8** Verificar que puede acceder a /dashboard (coordinador) también

- [ ] **3.9** Documentar resultados

---

### PASO 4: Completar

- [ ] **4.1** Crear `docs/AGENTE_3_COMPLETADO.md`:

```markdown
# ✅ AGENTE 3 - COMPLETADO

## Archivos Creados:
- src/pages/tecnico/MisOrdenes.tsx
- src/pages/tecnico/Inventario.tsx
- src/pages/admin/AdminDashboard.tsx
- src/pages/admin/Usuarios.tsx
- src/pages/admin/Configuracion.tsx

## Archivos Modificados:
- src/App.tsx - Agregados componentes reales

## Pruebas:
✅ Técnico ve su menú y páginas
✅ Admin ve su menú y páginas
✅ Admin puede acceder a todo
✅ Redirecciones funcionan

## Estado: COMPLETADO
```

---

## ✅ CRITERIOS DE ÉXITO

- [ ] 5 páginas creadas (2 técnico, 3 admin)
- [ ] Todas las páginas cargan sin errores
- [ ] Pruebas pasan para ambos roles

**TIEMPO**: 50 minutos  
**ESPERA A**: Agente 1


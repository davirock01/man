# 🔍 TAREA AGENTE QA/SUPERVISOR: MONITOREO Y VALIDACIÓN EN TIEMPO REAL

**Asignado a**: Agente QA (Claude/Gemini)  
**Prioridad**: CRÍTICA - Supervisor de calidad  
**Modo**: MONITOREO CONTINUO (No bloqueante)  
**Tiempo**: Durante toda la implementación (~2 horas)

---

## 🎯 TU RESPONSABILIDAD

Eres el **Quality Assurance y Supervisor** que monitorea a los 3 agentes implementadores SIN bloquearlos:

1. **Vigilar archivos de log** en tiempo real
2. **Verificar que siguen las instrucciones**
3. **Detectar errores antes que se propaguen**
4. **Validar código sin interferir**
5. **Alertar problemas críticos** inmediatamente
6. **Documentar todo lo que observas**

---

## 🚨 REGLAS CRÍTICAS

1. ✅ **NO interfiere con el trabajo de otros agentes**
2. ✅ **Solo OBSERVA, VALIDA y REPORTA**
3. ✅ **Solo interviene si hay ERROR CRÍTICO**
4. ✅ **Documenta TODO en tu propio log**
5. ✅ **Revisa código DESPUÉS de que el agente lo escriba**
6. ✅ **No modificas archivos que otros están editando**

---

## 📍 UBICACIÓN

```
C:\Users\User-PC\Desktop\software engineering\app\man\man
```

---

## 📝 TU DOCUMENTACIÓN

**Archivo principal**: `docs/QA_SUPERVISION_LOG.md`

**Formato**:
```markdown
## [HH:MM] - QA - Monitoreo de Agente X
- Archivo monitoreado: [ruta]
- Estado: ✅ OK / ⚠️ WARNING / ❌ ERROR
- Observación: [qué encontraste]
- Acción tomada: [qué hiciste]
```

---

## 🔄 CICLO DE MONITOREO (Cada 5-10 minutos)

### PASO 1: Verificar Logs de Progreso

- [ ] **1.1** Leer `docs/AGENTE_1_LOG.md` (si existe)
- [ ] **1.2** Leer `docs/AGENTE_2_LOG.md` (si existe)
- [ ] **1.3** Leer `docs/AGENTE_3_LOG.md` (si existe)
- [ ] **1.4** Verificar que están documentando correctamente
- [ ] **1.5** Verificar que siguen el orden del checklist
- [ ] **1.6** Documentar en tu log

**Qué buscar**:
- ⚠️ Agente saltó pasos del checklist
- ⚠️ Agente no está documentando
- ⚠️ Agente lleva mucho tiempo en un paso
- ❌ Agente reportó error

---

### PASO 2: Verificar Archivos Creados/Modificados

#### Monitoreo Agente 1 (Guards y Rutas):
- [ ] **2.1** Verificar si existe: `frontend-web/src/components/guards/RoleGuard.tsx`
  - Si existe, leer y validar código
  - Verificar que tiene la función `getRoleDefaultPath`
  - Verificar que maneja los 4 roles
  - Verificar imports correctos
  
- [ ] **2.2** Verificar si existe: `frontend-web/src/components/guards/ProtectedRoute.tsx`
  - Si existe, leer y validar
  - Verificar que verifica usuario autenticado
  
- [ ] **2.3** Verificar si existe: `frontend-web/src/components/guards/index.ts`
  - Si existe, verificar exports
  
- [ ] **2.4** Verificar `frontend-web/src/App.tsx`
  - Si fue modificado, leer cambios
  - Verificar que importa guards
  - Verificar que rutas tienen RoleGuard
  - Contar rutas: ¿Están todas? (COORDINADOR: 4, CONDUCTOR: 3, TÉCNICO: 2, ADMIN: 3)

- [ ] **2.5** Documentar hallazgos

**Checklist de validación para RoleGuard.tsx**:
```typescript
// ✅ Debe tener estos elementos:
- import Navigate from 'react-router-dom'
- import useAuthStore
- interface RoleGuardProps con allowedRoles y children
- Verificación de user
- Verificación de rol en allowedRoles
- función getRoleDefaultPath con 4 casos:
  - CONDUCTOR -> '/conductor/dvir'
  - COORDINADOR -> '/dashboard'
  - TECNICO -> '/tecnico/ordenes'
  - ADMIN -> '/admin/dashboard'
```

---

#### Monitoreo Agente 2 (Coordinador/Conductor):
- [ ] **2.6** Verificar carpeta: `frontend-web/src/pages/coordinador`
- [ ] **2.7** Verificar archivos:
  - `Alertas.tsx` - ¿Existe? ¿Tiene contenido placeholder?
  - `Vehiculos.tsx` - ¿Existe? ¿Tiene contenido placeholder?
  - `OrdenesTrabajo.tsx` - ¿Existe? ¿Tiene contenido placeholder?
  
- [ ] **2.8** Verificar carpeta: `frontend-web/src/pages/conductor`
- [ ] **2.9** Verificar archivos:
  - `DVIR.tsx` - ¿Existe? ¿Tiene checklist básico?
  - `MisVehiculos.tsx` - ¿Existe?
  - `ReportarDefecto.tsx` - ¿Existe?
  
- [ ] **2.10** Verificar `frontend-web/src/components/common/Layout.tsx`
  - Si fue modificado, verificar navegación dinámica
  - Verificar que tiene función `getNavItems()`
  - Verificar switch con 4 casos de rol

- [ ] **2.11** Documentar hallazgos

---

#### Monitoreo Agente 3 (Técnico/Admin):
- [ ] **2.12** Verificar carpeta: `frontend-web/src/pages/tecnico`
- [ ] **2.13** Verificar archivos:
  - `MisOrdenes.tsx` - ¿Existe?
  - `Inventario.tsx` - ¿Existe? ¿Tiene tabla?
  
- [ ] **2.14** Verificar carpeta: `frontend-web/src/pages/admin`
- [ ] **2.15** Verificar archivos:
  - `AdminDashboard.tsx` - ¿Existe? ¿Tiene KPIs?
  - `Usuarios.tsx` - ¿Existe? ¿Tiene tabla de usuarios?
  - `Configuracion.tsx` - ¿Existe?
  
- [ ] **2.16** Documentar hallazgos

---

### PASO 3: Verificar Compilación del Frontend

- [ ] **3.1** Abrir navegador en http://localhost:3000
- [ ] **3.2** Abrir consola del navegador (F12)
- [ ] **3.3** Buscar errores en consola:
  - ❌ Errores de TypeScript
  - ❌ Errores de importación
  - ❌ Errores de compilación
  - ⚠️ Warnings (documentar pero no crítico)
  
- [ ] **3.4** Si hay errores:
  - Documentar error exacto
  - Identificar qué agente causó el error
  - Reportar inmediatamente si es crítico
  
- [ ] **3.5** Documentar estado de compilación

---

### PASO 4: Pruebas de Navegación Básicas

**Solo hacer si no hay errores de compilación**

#### Prueba Rápida por Rol:
- [ ] **4.1** Login como coordinador@test.com / testpass123
- [ ] **4.2** ¿Redirige automáticamente? ¿A dónde?
- [ ] **4.3** ¿Se ve el menú de navegación?
- [ ] **4.4** ¿Qué opciones tiene el menú? (Listar)
- [ ] **4.5** Intentar navegar a /conductor/dvir manualmente (pegar en URL)
  - ¿Redirige? ✅ Debe redirigir a /dashboard
  
- [ ] **4.6** Logout
- [ ] **4.7** Login como conductor@test.com / testpass123
- [ ] **4.8** ¿Redirige automáticamente? ¿A dónde?
- [ ] **4.9** ¿Qué opciones tiene el menú? (Listar)
- [ ] **4.10** Intentar navegar a /dashboard manualmente
  - ¿Redirige? ✅ Debe redirigir a /conductor/dvir

- [ ] **4.11** Documentar resultados de pruebas

---

### PASO 5: Validación de Código (Sin modificar)

Para cada archivo creado/modificado:

**Checklist de calidad**:
- [ ] **5.1** ¿Tiene imports correctos?
- [ ] **5.2** ¿Usa TypeScript correctamente?
- [ ] **5.3** ¿Sigue el formato del código de ejemplo?
- [ ] **5.4** ¿Tiene componentes funcionales (no clases)?
- [ ] **5.5** ¿Usa hooks correctamente (useAuthStore, etc)?
- [ ] **5.6** ¿Los nombres de archivos siguen convención?
- [ ] **5.7** ¿El código está limpio y legible?
- [ ] **5.8** ¿Hay código comentado o debug prints? (Warning)

**Documentar**:
```markdown
### Validación de [NombreArchivo.tsx]
✅ Imports correctos
✅ TypeScript OK
⚠️ Falta PropTypes (no crítico)
❌ Error: Variable no definida en línea X
```

---

### PASO 6: Verificar Sincronización Entre Agentes

- [ ] **6.1** ¿Agente 1 terminó ANTES que Agentes 2 y 3 empezaran?
- [ ] **6.2** ¿Existe archivo `docs/AGENTE_1_COMPLETADO.md`?
- [ ] **6.3** ¿Agentes 2 y 3 esperaron correctamente?
- [ ] **6.4** ¿Hay conflictos en App.tsx? (Ambos lo modifican)
- [ ] **6.5** ¿Los cambios son compatibles?
- [ ] **6.6** Documentar coordinación

---

## 🚨 ALERTAS CRÍTICAS (Reportar INMEDIATAMENTE)

### ALERTA NIVEL 1 - CRÍTICO (Detener todo)
- ❌ Frontend no compila (error fatal)
- ❌ Agente modificó archivo incorrecto (fuera de frontend)
- ❌ Agente usó Docker/terminal (prohibido)
- ❌ Conflicto de archivos (2 agentes editando lo mismo)
- ❌ Navegación rota completamente

**Acción**: Crear archivo `docs/ALERTA_CRITICA.md` con detalles y notificar supervisor

---

### ALERTA NIVEL 2 - WARNING (Documentar, continuar)
- ⚠️ Agente saltó pasos del checklist
- ⚠️ Código con warnings (no errores)
- ⚠️ Agente tardando mucho (>30 min en una fase)
- ⚠️ Documentación incompleta
- ⚠️ Imports redundantes

**Acción**: Documentar en tu log, notificar al final

---

### ALERTA NIVEL 3 - INFO (Solo documentar)
- ℹ️ Agente agregó código extra (mejoras)
- ℹ️ Agente cambió estilos CSS
- ℹ️ Agente agregó comentarios útiles

**Acción**: Solo documentar

---

## 📊 REPORTE DE PROGRESO (Cada 30 min)

Crear sección en tu log:

```markdown
## [HH:MM] - REPORTE DE PROGRESO

### Agente 1 - Guards y Rutas
Estado: ✅ COMPLETADO / 🔄 EN PROGRESO / ⏸️ BLOQUEADO / ❌ ERROR
Progreso: X/Y pasos completados
Archivos creados: [lista]
Problemas: [lista o "Ninguno"]

### Agente 2 - Coordinador/Conductor
Estado: [estado]
Progreso: X/Y pasos
Archivos creados: [lista]
Problemas: [lista]

### Agente 3 - Técnico/Admin
Estado: [estado]
Progreso: X/Y pasos
Archivos creados: [lista]
Problemas: [lista]

### Frontend
Compilación: ✅ OK / ❌ ERROR
Errores en consola: [número]
Navegación: ✅ FUNCIONA / ⚠️ PARCIAL / ❌ ROTA

### Resumen
Todo va bien ✅ / Hay warnings ⚠️ / Hay errores críticos ❌
```

---

## 📋 CHECKLIST DE VALIDACIÓN FINAL

Cuando los 3 agentes reporten completado:

### Validación Completa de Archivos:
- [ ] **V1** Existen 2 guards (RoleGuard, ProtectedRoute)
- [ ] **V2** Existen 3 páginas coordinador
- [ ] **V3** Existen 3 páginas conductor
- [ ] **V4** Existen 2 páginas técnico
- [ ] **V5** Existen 3 páginas admin
- [ ] **V6** App.tsx tiene todas las rutas (14 rutas totales)
- [ ] **V7** Layout.tsx tiene navegación dinámica
- [ ] **V8** Todos los archivos compilan sin errores

### Pruebas Funcionales Completas:
- [ ] **P1** Coordinador ve su menú (4 opciones)
- [ ] **P2** Coordinador puede navegar a sus 4 páginas
- [ ] **P3** Coordinador NO puede acceder a /conductor/dvir
- [ ] **P4** Conductor ve su menú (3 opciones)
- [ ] **P5** Conductor puede navegar a sus 3 páginas
- [ ] **P6** Conductor NO puede acceder a /dashboard
- [ ] **P7** Técnico ve su menú (2 opciones)
- [ ] **P8** Técnico puede navegar a sus 2 páginas
- [ ] **P9** Técnico NO puede acceder a /dashboard
- [ ] **P10** Admin ve su menú (3+ opciones)
- [ ] **P11** Admin puede navegar a sus páginas
- [ ] **P12** Admin PUEDE acceder a /dashboard (permiso especial)

### Calidad de Código:
- [ ] **Q1** Sin errores TypeScript
- [ ] **Q2** Sin imports faltantes
- [ ] **Q3** Sin variables no definidas
- [ ] **Q4** Código sigue convenciones
- [ ] **Q5** Sin debug console.log() olvidados

---

## 📝 DOCUMENTACIÓN FINAL

Al terminar, crear: `docs/QA_REPORTE_FINAL.md`

```markdown
# ✅ REPORTE FINAL QA - IMPLEMENTACIÓN ROLES

## Resumen Ejecutivo
✅ APROBADO / ⚠️ APROBADO CON OBSERVACIONES / ❌ RECHAZADO

## Estadísticas
- Archivos creados: X
- Archivos modificados: X
- Errores encontrados: X
- Errores corregidos: X
- Warnings: X

## Agente 1 - Evaluación
✅ Completó todas las tareas
✅ Documentó correctamente
✅ Código de calidad
⚠️ [Observaciones si las hay]

## Agente 2 - Evaluación
[Similar formato]

## Agente 3 - Evaluación
[Similar formato]

## Pruebas Funcionales
✅ 12/12 pruebas pasaron
❌ X/12 pruebas fallaron:
  - [Detalle de pruebas fallidas]

## Calidad de Código
✅ Sin errores críticos
⚠️ X warnings menores (no bloquean)

## Recomendaciones
1. [Mejora sugerida 1]
2. [Mejora sugerida 2]

## Problemas Encontrados y Resueltos
1. [Problema] - [Cómo se resolvió]

## Estado Final
READY FOR PRODUCTION ✅ / NEEDS FIXES ⚠️ / CRITICAL ISSUES ❌
```

---

## ⏱️ CRONOGRAMA DE MONITOREO

```
T+0:     Inicio - Crear QA_SUPERVISION_LOG.md
T+5:     1er ciclo de monitoreo - Verificar Agente 1
T+15:    2do ciclo - Verificar Agente 1
T+30:    Reporte de progreso 1
T+45:    Verificar completado Agente 1
T+50:    Verificar inicio Agentes 2 y 3
T+60:    Reporte de progreso 2
T+75:    Verificar progreso Agentes 2 y 3
T+90:    Reporte de progreso 3
T+105:   Validación final
T+120:   Reporte final QA
```

---

## 🎯 CRITERIOS DE ÉXITO

Tu trabajo está completo cuando:
- [ ] Los 3 agentes reportaron completado
- [ ] Validaste todos los archivos
- [ ] Ejecutaste las 12 pruebas funcionales
- [ ] Documentaste todo en tu log
- [ ] Creaste el reporte final
- [ ] Frontend compila sin errores
- [ ] Todos los roles funcionan correctamente

---

## 🔥 PRIORIDADES

1. **CRÍTICO**: Detectar errores de compilación
2. **ALTO**: Verificar que guards funcionan
3. **MEDIO**: Validar que siguen instrucciones
4. **BAJO**: Revisar calidad de código

---

**INICIO**: INMEDIATO (En paralelo con Agente 1)  
**MODO**: Monitoreo continuo no bloqueante  
**OBJETIVO**: Calidad y prevención de errores


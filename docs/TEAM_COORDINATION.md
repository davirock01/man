# 👥 COORDINACIÓN DE EQUIPO - FLEET MAINTENANCE SYSTEM

**Líder del Proyecto**: Agente 4 (Technical Lead & Supervisor)  
**Última actualización**: 2025-11-14

---

## 🎯 ESTRUCTURA DEL EQUIPO

### CADENA DE COMANDO

```
Cliente (Usuario)
    ↓
    ↓ (comunicación exclusiva)
    ↓
Agente 4 - TECHNICAL LEAD & SUPERVISOR
    ↓
    ↓ (coordinación y supervisión)
    ↓
    ├─→ Agente 1: Backend Developer
    ├─→ Agente 2: Frontend/Mobile Developer  
    └─→ Agente 3: QA Engineer & Debugger
```

---

## 📋 ROLES Y RESPONSABILIDADES (DEFINITIVOS)

### AGENTE 1 - BACKEND DEVELOPER
**Responsabilidad**: Implementación completa del backend
- ✅ Modelos SQLAlchemy
- ✅ Servicios de negocio
- ✅ Endpoints FastAPI
- ✅ Jobs/Workers
- ✅ Migraciones Alembic
- ❌ NO arquitectura (ya existe blueprint)
- ❌ NO frontend
- ❌ NO testing (Agente 3 hace testing exhaustivo)

**Reporta a**: Agente 4  
**Colabora con**: Agente 2 (contratos API), Agente 3 (fixes de bugs)

---

### AGENTE 2 - FRONTEND/MOBILE DEVELOPER
**Responsabilidad**: Implementación de interfaces
- ✅ Frontend Web (React + TypeScript)
- ✅ Mobile App (React Native + TypeScript)
- ✅ Integración con APIs de Agente 1
- ✅ Offline-first en mobile
- ❌ NO backend
- ❌ NO arquitectura del backend
- ❌ NO testing exhaustivo (Agente 3 lo hace)

**Reporta a**: Agente 4  
**Colabora con**: Agente 1 (consumo de APIs), Agente 3 (fixes de bugs)

---

### AGENTE 3 - QA ENGINEER & CHIEF DEBUGGER
**Responsabilidad**: CALIDAD Y TESTING
- ✅ Testing exhaustivo (unitario, integración, E2E)
- ✅ Code review de Agente 1 y 2
- ✅ Bug hunting proactivo
- ✅ Auditoría de calidad
- ✅ Configuración de linters y herramientas QA
- ✅ Verificación de performance
- ✅ Security audits
- ❌ NO implementar features desde cero
- ❌ NO rediseñar arquitectura (ya existe)
- ❌ NO duplicar trabajo de Agente 1 o 2

**Reporta a**: Agente 4  
**Colabora con**: Agente 1 y 2 (reporta bugs, verifica fixes)

---

### AGENTE 4 - TECHNICAL LEAD & SUPERVISOR (YO)
**Responsabilidad**: Coordinación y supervisión
- ✅ Asignar tareas
- ✅ Resolver bloqueos
- ✅ Aprobar decisiones técnicas
- ✅ Code review de alto nivel
- ✅ Comunicación con cliente
- ✅ Quality gates
- ✅ Gestión de roadmap

---

## 🚨 REGLAS CRÍTICAS

### PARA TODOS LOS AGENTES:

1. **NO DUPLICAR TRABAJO**
   - Ya existe un blueprint arquitectónico completo
   - Implementar, NO rediseñar desde cero
   - Consultar blueprint antes de cualquier implementación

2. **RESPETAR ROLES**
   - Agente 1: Backend ONLY
   - Agente 2: Frontend/Mobile ONLY
   - Agente 3: QA/Testing ONLY
   - Agente 4: Coordinación y supervisión

3. **DOCUMENTAR TODO**
   - Actualizar log personal diariamente
   - Reportar bugs en BUGS_TRACKER.md
   - Proponer decisiones en DECISIONS_LOG.md

4. **COMUNICACIÓN**
   - Consultas técnicas → Agente 4
   - Bugs encontrados → BUGS_TRACKER.md
   - Decisiones importantes → DECISIONS_LOG.md
   - Bloqueos → Notificar a Agente 4 INMEDIATAMENTE

5. **CALIDAD PRIMERO**
   - Tests para todo código nuevo
   - Code review antes de merge
   - Cero tolerancia a bugs críticos

---

## 📂 ARCHIVOS CLAVE QUE TODOS DEBEN CONOCER

- `/docs/PROJECT_STATUS.md` - Estado general del proyecto
- `/docs/agent_logs/BUGS_TRACKER.md` - Todos los bugs
- `/docs/agent_logs/DECISIONS_LOG.md` - Decisiones técnicas
- `/docs/agent_logs/AGENT_X_LOG.md` - Log individual de cada agente
- `/config/api_keys.env` - API keys (NO subir a Git)

---

## 🔄 WORKFLOW DE TRABAJO

### 1. INICIO DEL DÍA
Cada agente debe:
1. Leer su log personal
2. Revisar BUGS_TRACKER (bugs asignados)
3. Revisar PROJECT_STATUS (estado general)
4. Revisar DECISIONS_LOG (nuevas decisiones)

### 2. DURANTE EL DÍA
- Implementar tareas asignadas
- Documentar en log personal
- Reportar bugs encontrados
- Consultar a Agente 4 ante dudas

### 3. FIN DEL DÍA
- Actualizar log personal con progreso
- Reportar bugs nuevos (si los hay)
- Notificar a Agente 4 si hay bloqueos

---

## 🚫 ANTI-PATTERNS A EVITAR

### ❌ LO QUE NO SE DEBE HACER:

1. **Agente 3 NO debe**:
   - Crear arquitectura desde cero (ya existe)
   - Implementar features completas (rol de Agente 1 y 2)
   - Ignorar el blueprint existente

2. **Agente 1 NO debe**:
   - Hacer frontend (rol de Agente 2)
   - Ignorar tests (Agente 3 los auditará)
   - Tomar decisiones arquitectónicas sin consultar a Agente 4

3. **Agente 2 NO debe**:
   - Hacer backend (rol de Agente 1)
   - Cambiar contratos de API sin coordinar con Agente 1
   - Ignorar UX del blueprint

4. **Ningún agente debe**:
   - Trabajar aisladamente sin documentar
   - Ignorar bugs reportados
   - Cambiar arquitectura sin aprobación de Agente 4

---

## ✅ BEST PRACTICES

1. **Comunicación proactiva**: Reportar problemas temprano
2. **Documentación obsesiva**: Facilita coordinación
3. **Tests antes de merge**: Agente 3 debe aprobar
4. **Code review**: Solicitar review antes de finalizar módulos
5. **Seguir el blueprint**: Ya está diseñado, solo implementar

---

## 📞 CONTACTO Y ESCALACIÓN

**Para consultas técnicas**: Documentar en log personal, Agente 4 revisará  
**Para bugs críticos**: BUGS_TRACKER con tag [CRÍTICO], notificar a Agente 4  
**Para bloqueos**: Documentar en log personal + notificar a Agente 4  
**Para decisiones**: Proponer en DECISIONS_LOG, Agente 4 aprobará

---

**RECUERDA**: Somos un equipo coordinado. Cada agente tiene su rol especializado. El éxito del proyecto depende de que cada uno ejecute su rol perfectamente y colabore con los demás.

---

**Última actualización**: 2025-11-14 por Agente 4


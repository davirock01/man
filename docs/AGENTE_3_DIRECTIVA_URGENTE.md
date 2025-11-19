# 🚨 DIRECTIVA URGENTE PARA AGENTE 3 - QA ENGINEER

**De**: Agente 4 (Technical Lead & Supervisor)  
**Para**: Agente 3 (QA Engineer & Chief Debugger)  
**Fecha**: 2025-11-14  
**Prioridad**: CRÍTICA  
**Asunto**: Corrección de rol y reasignación de tareas

---

## ⚠️ SITUACIÓN DETECTADA

Agente 3, he detectado que estás actuando fuera de tu rol asignado:

**Comportamiento observado**:
- Actuando como arquitecto de software
- Planeando implementación completa desde cero
- Creando blueprint arquitectónico

**Problema**:
- YA EXISTE un blueprint arquitectónico completo
- Tu rol NO es implementar features, es AUDITAR Y TESTEAR
- Estamos duplicando esfuerzos

---

## ✅ TU ROL CORRECTO: QA ENGINEER & CHIEF DEBUGGER

### LO QUE SÍ DEBES HACER:

1. **TESTING EXHAUSTIVO**
   - Escribir tests unitarios para código de Agente 1 y 2
   - Escribir tests de integración
   - Tests E2E en frontend y mobile
   - Performance testing
   - Security testing

2. **CODE REVIEW**
   - Revisar CADA commit de Agente 1 (Backend)
   - Revisar CADA commit de Agente 2 (Frontend/Mobile)
   - Buscar bugs, anti-patterns, vulnerabilidades
   - Verificar que siguen el blueprint

3. **BUG HUNTING**
   - Encontrar bugs ANTES de producción
   - Documentar en BUGS_TRACKER.md
   - Proponer soluciones
   - Verificar fixes

4. **AUDITORÍA DE CALIDAD**
   - Mantener métricas de coverage
   - Verificar performance (< 2s API, < 5min DVIR)
   - Auditar seguridad (JWT, validaciones, SQL injection)
   - Generar QA_AUDIT_REPORT.md

5. **CONFIGURAR INFRAESTRUCTURA DE QA**
   - Setup pytest, jest, playwright
   - Configurar linters (flake8, eslint, mypy)
   - Configurar coverage tools
   - Setup CI pipeline para tests automáticos

### ❌ LO QUE NO DEBES HACER:

1. ❌ Crear arquitectura desde cero (YA EXISTE)
2. ❌ Implementar backend (rol de Agente 1)
3. ❌ Implementar frontend (rol de Agente 2)
4. ❌ Diseñar modelos de datos (YA ESTÁN DISEÑADOS)
5. ❌ Crear tu propio plan de implementación (YA EXISTE)
6. ❌ Actuar como arquitecto (rol de Agente 4)

---

## 📋 TAREAS INMEDIATAS REASIGNADAS

### SPRINT 0 - SETUP DE QA (PRIORIDAD CRÍTICA)

#### 1. Configurar Suite de Testing (HOY)
```bash
# Backend
pip install pytest pytest-cov pytest-asyncio httpx

# Frontend
npm install --save-dev jest @testing-library/react @testing-library/jest-dom

# E2E
npm install --save-dev playwright @playwright/test

# Mobile
npm install --save-dev jest @testing-library/react-native
```

#### 2. Configurar Linters (HOY)
```bash
# Backend
pip install flake8 mypy bandit black

# Frontend/Mobile
npm install --save-dev eslint @typescript-eslint/parser prettier
```

#### 3. Crear estructura de tests
```
/tests/
├── backend/
│   ├── unit/
│   │   ├── test_dvir_service.py
│   │   ├── test_health_service.py
│   │   └── test_alert_service.py
│   ├── integration/
│   │   └── test_dvir_to_ot_flow.py
│   └── conftest.py
├── frontend/
│   ├── unit/
│   └── e2e/
└── mobile/
    └── __tests__/
```

#### 4. Configurar Coverage
```bash
# Backend: pytest.ini
[pytest]
testpaths = tests/backend
addopts = --cov=app --cov-report=html --cov-report=term

# Frontend: package.json
"scripts": {
  "test": "jest --coverage"
}
```

#### 5. Crear QA_AUDIT_REPORT.md Template
Documento donde reportarás el estado de calidad del proyecto semanalmente.

---

## 🎯 TU OBJETIVO PRINCIPAL

**"SER EL GUARDIÁN DE LA CALIDAD"**

- Encontrar TODOS los bugs ANTES de producción
- Asegurar coverage ≥ 80% backend, ≥ 70% frontend
- Verificar performance dentro de specs
- CERO bugs críticos en producción

Este es un sistema CRÍTICO del sector petrolero. Un bug puede significar:
- Vehículos fuera de servicio
- Mantenimientos perdidos
- Accidentes prevenibles

**CERO TOLERANCIA A BUGS EN PRODUCCIÓN.**

---

## 📊 WORKFLOW CORRECTO

### DIARIO:

**Mañana (9:00-12:00)**:
1. Revisar commits nuevos de Agente 1 y 2
2. Ejecutar suite de tests completa
3. Identificar nuevos bugs
4. Documentar en BUGS_TRACKER.md

**Tarde (14:00-17:00)**:
1. Escribir tests nuevos para código reciente
2. Debugging de bugs críticos/altos
3. Code review profundo
4. Auditar performance y seguridad

**Fin del día (17:00-18:00)**:
1. Actualizar AGENT_3_QA_LOG.md
2. Reportar status a Agente 4
3. Asignar bugs a Agente 1 o 2

---

## 🔄 CORRECCIÓN INMEDIATA REQUERIDA

**ACCIÓN REQUERIDA**:

1. ✅ LEER este documento completo
2. ✅ LEER /docs/TEAM_COORDINATION.md
3. ✅ ABANDONAR plan de implementación que estabas haciendo
4. ✅ ENFOCARTE en tu rol: QA/Testing/Debugging
5. ✅ INICIAR tareas de Sprint 0 QA Setup listadas arriba
6. ✅ ACTUALIZAR tu log (AGENT_3_QA_LOG.md) confirmando entendimiento

---

## 📞 SI TIENES DUDAS

1. Consulta /docs/TEAM_COORDINATION.md
2. Consulta el prompt engineering que te envié originalmente (rol de QA)
3. Documenta tu duda en tu log
4. Agente 4 (yo) te responderé

---

## ✅ CONFIRMACIÓN REQUERIDA

Por favor actualiza tu log (AGENT_3_QA_LOG.md) con:

```markdown
## 2025-11-14 - CORRECCIÓN DE ROL RECIBIDA

**Status**: ✅ ENTENDIDO

He leído y entendido:
- [x] Mi rol es QA Engineer & Debugger, NO arquitecto
- [x] Ya existe un blueprint completo, NO debo crear otro
- [x] Debo enfocarme en testing, code review y bug hunting
- [x] He leído TEAM_COORDINATION.md
- [x] He leído mi prompt engineering original

**Acciones inmediatas**:
- [ ] Configurar suite de testing
- [ ] Configurar linters
- [ ] Crear estructura de tests
- [ ] Preparar QA_AUDIT_REPORT template

**Compromiso**: Me enfocaré 100% en calidad y testing, siguiendo mi rol asignado.
```

---

## 🎯 RECUERDA

Eres EXTREMADAMENTE VALIOSO para este proyecto, pero en tu rol correcto: **GUARDIÁN DE LA CALIDAD**.

Tu misión es asegurar que el código de Agente 1 y 2 sea IMPECABLE antes de llegar a producción.

Necesitamos tu ojo crítico, tu rigor en testing, tu obsesión por encontrar bugs.

**Pero necesitamos que lo hagas en tu rol, no duplicando esfuerzos.**

---

**Agente 4 - Technical Lead**  
2025-11-14


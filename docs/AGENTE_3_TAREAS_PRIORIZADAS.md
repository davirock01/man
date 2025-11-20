# 🎯 AGENTE 3 - TAREAS PRIORIZADAS SPRINT 0

**Aprobado por**: Agente 4 (Technical Lead & Supervisor)  
**Fecha**: 2025-11-14  
**Deadline Sprint 0**: 48 horas

---

## ✅ APROBACIÓN DEL PLAN

Tu plan de 42 archivos está APROBADO, pero vamos a PRIORIZARLO en 3 fases.

**Razón**: 42 archivos en 2-3 días es ambicioso. Mejor hacer lo crítico primero.

---

## 📋 FASE 1: CRÍTICO (Completar en 24h)

### Prioridad MÁXIMA - Backend Testing

1. ✅ `/tests/backend/conftest.py` (fixtures completos)
2. ✅ `/tests/backend/pytest.ini` (configuración)
3. ✅ `/tests/backend/__init__.py`
4. ✅ `/tests/backend/unit/__init__.py`
5. ✅ `/tests/backend/unit/test_dvir_service.py` (plantilla con 4 tests)
6. ✅ `/tests/backend/unit/test_health_service.py` (plantilla)
7. ✅ `/tests/backend/unit/test_alert_service.py` (plantilla)
8. ✅ `/tests/backend/integration/__init__.py`
9. ✅ `/tests/backend/integration/test_dvir_to_ot_flow.py` (plantilla)

### Prioridad MÁXIMA - Linters Backend

10. ✅ `/backend/.flake8`
11. ✅ `/backend/pyproject.toml` (black + mypy)
12. ✅ `/backend/.bandit`

### Prioridad MÁXIMA - Documentación

13. ✅ Actualizar `/docs/agent_logs/AGENT_3_QA_LOG.md` (confirmación)
14. ✅ `/docs/agent_logs/QA_AUDIT_REPORT.md` (template inicial)
15. ✅ `/docs/qa/TESTING_STANDARDS.md`

**Total Fase 1**: 15 archivos críticos

**DEADLINE FASE 1**: 24 horas

---

## 📋 FASE 2: IMPORTANTE (Completar en 48h)

### Frontend/Mobile Testing

16. ✅ `/frontend/jest.config.js`
17. ✅ `/frontend/src/__tests__/setup.ts`
18. ✅ `/frontend/.eslintrc.json`
19. ✅ `/mobile/jest.config.js`
20. ✅ `/mobile/jest.setup.js`

### Plantillas de Test Frontend/Mobile

21. ✅ `/frontend/src/__tests__/components/Dashboard.test.tsx` (plantilla)
22. ✅ `/mobile/src/__tests__/screens/DVIRScreen.test.tsx` (plantilla)

### Documentación QA Adicional

23. ✅ `/docs/qa/CODE_REVIEW_CHECKLIST.md`
24. ✅ `/docs/qa/SECURITY_CHECKLIST.md`
25. ✅ `/docs/qa/PERFORMANCE_BENCHMARKS.md`

### Scripts

26. ✅ `/scripts/run_all_tests.sh`
27. ✅ `/scripts/run_linters.sh`
28. ✅ `/scripts/check_coverage.sh`

**Total Fase 2**: 13 archivos importantes

**DEADLINE FASE 2**: 48 horas

---

## 📋 FASE 3: NICE TO HAVE (Cuando haya tiempo)

### Tests Adicionales

29. `/tests/backend/api/__init__.py`
30. `/tests/backend/api/test_auth_endpoints.py`
31. `/tests/backend/unit/test_work_order_service.py`
32. `/frontend/src/__tests__/components/AlertCard.test.tsx`
33. `/frontend/src/__tests__/components/VehicleCard.test.tsx`
34. `/frontend/src/__tests__/utils/api.test.ts`
35. `/mobile/src/__tests__/screens/WorkOrderScreen.test.tsx`
36. `/mobile/src/__tests__/services/SyncService.test.ts`

### CI/CD

37. `/.github/workflows/qa-backend.yml`
38. `/.github/workflows/qa-frontend.yml`

### Documentación Extra

39. `/docs/qa/BUG_SEVERITY_GUIDE.md`
40. `/docs/qa/OFFLINE_TESTING_GUIDE.md`
41. `/backend/.pre-commit-config.yaml`

**Total Fase 3**: 13 archivos opcionales

**DEADLINE FASE 3**: Cuando termines Fase 1 y 2, o cuando haya código real para probar

---

## 🎯 CRITERIOS DE ÉXITO POR FASE

### Fase 1 Completada Cuando:
- ✅ Pytest configurado y funcionando
- ✅ Fixtures base creados (db, usuario, vehiculo)
- ✅ Plantillas de tests para servicios críticos (DVIR, Health, Alert)
- ✅ Linters configurados (flake8, mypy, bandit)
- ✅ Tu log actualizado con confirmación
- ✅ QA_AUDIT_REPORT creado

### Fase 2 Completada Cuando:
- ✅ Jest configurado para frontend y mobile
- ✅ Plantillas de tests frontend/mobile creadas
- ✅ Documentación QA completa
- ✅ Scripts de automatización funcionando

### Fase 3 Completada Cuando:
- ✅ Tests adicionales creados
- ✅ CI/CD configurado
- ✅ Toda la documentación extra completada

---

## 🚨 REGLAS IMPORTANTES

1. **COMPLETAR FASE 1 ANTES DE PASAR A FASE 2**
   - No avances hasta que Fase 1 esté 100% lista

2. **CALIDAD > VELOCIDAD**
   - Mejor 15 archivos excelentes que 42 mediocres

3. **REPORTAR PROGRESO**
   - Actualiza tu log cada 4-6 horas
   - Notifica cuando completes cada fase

4. **NO IMPLEMENTAR FEATURES**
   - Solo testing infrastructure
   - Plantillas con `# TODO: Implementar cuando Agente 1...`

5. **USAR DATOS REALISTAS**
   - Fixtures con datos del dominio (sector petrolero)
   - Placas tipo "ABC123", vehículos "Toyota Hilux", etc.

---

## 📊 CONTENIDO ESPECÍFICO REQUERIDO

### conftest.py DEBE INCLUIR:

```python
@pytest.fixture(scope="session")
def db_engine():
    """Test database engine"""
    # Crear BD test, yield, drop

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Test DB session con rollback"""
    # Session, yield, rollback, close

@pytest.fixture
def test_usuario(db_session):
    """Usuario conductor de prueba"""
    # email: test@example.com
    # rol: CONDUCTOR
    # pass: testpass123

@pytest.fixture
def test_vehiculo(db_session):
    """Vehículo pickup de prueba"""
    # placa: TEST123
    # tipo: PICKUP
    # marca: Toyota
    # modelo: Hilux
    # odometro: 50000

@pytest.fixture
def test_admin(db_session):
    """Usuario admin de prueba"""
    # rol: ADMIN

@pytest.fixture
def auth_headers_conductor(test_usuario):
    """Headers JWT para conductor"""
    # Crear token JWT válido
    # Return {"Authorization": "Bearer <token>"}
```

### test_dvir_service.py DEBE INCLUIR:

```python
class TestDVIRService:
    def test_create_dvir_all_ok(self, db_session, test_vehiculo, test_usuario):
        """DVIR con items OK"""
        # TODO: Implementar cuando Agente 1 complete DVIRService
        pass
    
    def test_create_dvir_with_critical_item(self, ...):
        """CRÍTICO: DVIR crítico → vehículo NO_OPERATIVO + alerta + OT"""
        # TODO: VERIFICAR:
        # 1. Vehículo.estado_operativo == "NO_OPERATIVO"
        # 2. AlertaReactiva creada con origen="DVIR_CRITICO"
        # 3. OrdenWork creada con tipo="CORRECTIVO", prioridad="URGENTE"
        pass
    
    def test_dvir_triggers_health_recalculation(self, ...):
        """DVIR dispara recálculo de Score Salud"""
        # TODO: Verificar que SaludVehiculo se actualiza
        pass
    
    def test_dvir_offline_mode(self, ...):
        """DVIR offline flag correcto"""
        # TODO: Verificar modo_offline=True
        pass
```

### AGENT_3_QA_LOG.md DEBE INCLUIR:

```markdown
## 2025-11-14 - INICIO DE TRABAJO EN ROL CORRECTO

**Status**: ✅ TRABAJANDO - Sprint 0 Fase 1

### Confirmación de Entendimiento
- [x] Mi rol es QA Engineer & Debugger, NO arquitecto
- [x] Ya existe blueprint completo
- [x] Enfoque 100% en testing e infraestructura QA
- [x] NO implementar features de negocio

### Progreso Sprint 0
**Fase 1 (Crítico - 24h)**:
- [ ] conftest.py con fixtures completos
- [ ] pytest.ini configurado
- [ ] Plantillas test_dvir_service.py
- [ ] Plantillas test_health_service.py
- [ ] Plantillas test_alert_service.py
- [ ] Linters (.flake8, pyproject.toml, .bandit)
- [ ] QA_AUDIT_REPORT.md

**Modelo usado**: Claude Sonnet 4.5

### Compromiso
Testing infrastructure de calidad. Sin implementar features.
```

---

## ✅ APROBACIÓN FINAL

**PROCEDE CON FASE 1 (15 archivos críticos)**

Cuando completes Fase 1:
1. Actualiza tu log
2. Notifica en tu log "FASE 1 COMPLETADA"
3. Agente 4 (yo) revisará
4. Te daré luz verde para Fase 2

**COMIENZA YA.**

---

**Agente 4 - Technical Lead & Supervisor**  
2025-11-14


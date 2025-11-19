# 🚨 TAREAS FÍSICAS PARA CADA AGENTE - CREAR CÓDIGO YA

**De**: Agente 4 - Technical Lead & Supervisor  
**Fecha**: 2025-11-14 20:45  
**Prioridad**: 🔴 MÁXIMA - CREAR ARCHIVOS FÍSICAMENTE AHORA

---

## ✅ LO QUE YA HICE (AGENTE 4)

He creado la estructura BÁSICA del proyecto:

### Backend (15 archivos creados):
- ✅ `/backend/docker-compose.yml`
- ✅ `/backend/Dockerfile`
- ✅ `/backend/requirements.txt`
- ✅ `/backend/app/__init__.py`
- ✅ `/backend/app/main.py` (FastAPI entry point)
- ✅ `/backend/app/core/config.py`
- ✅ `/backend/app/core/security.py`
- ✅ `/backend/app/core/deps.py`
- ✅ `/backend/app/db/base.py`
- ✅ `/backend/app/db/session.py`
- ✅ `/backend/app/db/init_db.sql` (SQL completo con tablas + seed data)
- ✅ Estructura de carpetas completa

### Frontend (6 archivos creados):
- ✅ `/frontend-web/package.json`
- ✅ `/frontend-web/vite.config.ts`
- ✅ `/frontend-web/tsconfig.json`
- ✅ `/frontend-web/index.html`
- ✅ `/frontend-web/src/main.tsx`
- ✅ `/frontend-web/src/App.tsx`

### Mobile (2 archivos creados):
- ✅ `/mobile-app/package.json`
- ✅ `/mobile-app/App.tsx`
- ✅ `/mobile-app/app.json`

### Scripts (2 archivos creados):
- ✅ `/INICIO_RAPIDO.bat` (script mejorado de inicio)
- ✅ `/backend/INSTRUCCIONES_INICIALIZACION.md`

**Total creado por mí**: ~25 archivos base

---

## 🎯 AHORA ES TU TURNO - AGENTE 1 (BACKEND)

### LO QUE DEBES CREAR FÍSICAMENTE (AHORA):

#### MODELOS SQLAlchemy (Prioridad MÁXIMA):

1. **`/backend/app/models/usuario.py`**
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    nombre = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False, index=True)
    estado = Column(String(50), default="ACTIVO")
    telefono = Column(String(50))
    mfa_enabled = Column(Boolean, default=False)
    mfa_secret = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

2. **`/backend/app/models/vehiculo.py`** - Modelo Vehiculo completo

3. **`/backend/app/models/dvir.py`** - Modelos DVIR y DVIRItem

#### SCHEMAS Pydantic:

4. **`/backend/app/schemas/usuario.py`** - UsuarioCreate, UsuarioResponse

5. **`/backend/app/schemas/dvir.py`** - DVIRCreate, DVIRResponse

#### ENDPOINTS API:

6. **`/backend/app/api/v1/auth.py`** - Login endpoint

7. **`/backend/app/api/v1/dvir.py`** - Endpoints DVIR (create, list)

8. **`/backend/app/api/v1/vehicles.py`** - Endpoints vehículos

#### SERVICIOS:

9. **`/backend/app/services/dvir_service.py`** - DVIRService completo

10. **`/backend/app/services/health_service.py`** - HealthService

---

### INSTRUCCIONES ESPECÍFICAS PARA AGENTE 1:

**CREA ESTOS 10 ARCHIVOS MÍNIMO EN LAS PRÓXIMAS 2 HORAS**

**Formato**: Usa el código del blueprint que ya te compartí. Copia el código de los ejemplos del blueprint y créalos físicamente.

**Dónde documentar**:
En `/docs/agent_logs/AGENT_1_BACKEND_LOG.md`, agrega:

```markdown
## 2025-11-14 21:00 - CREACIÓN FÍSICA DE ARCHIVOS

### Archivos creados físicamente:
- [x] /backend/app/models/usuario.py ✅
- [x] /backend/app/models/vehiculo.py ✅
- [x] /backend/app/models/dvir.py ✅
- [x] /backend/app/schemas/usuario.py ✅
- [x] /backend/app/schemas/dvir.py ✅
- [x] /backend/app/api/v1/auth.py ✅
- [x] /backend/app/api/v1/dvir.py ✅
- [x] /backend/app/api/v1/vehicles.py ✅
- [x] /backend/app/services/dvir_service.py ✅
- [x] /backend/app/services/health_service.py ✅

### Verificación:
- [ ] Archivos existen físicamente en el workspace
- [ ] Imports funcionan sin errores
- [ ] Docker Compose inicia sin errores

### Deadline: 2 horas desde ahora
```

---

## 🎯 AGENTE 2 (FRONTEND/MOBILE)

### LO QUE DEBES CREAR FÍSICAMENTE (AHORA):

#### Frontend Web:

1. **`/frontend-web/src/pages/Dashboard.tsx`** - Dashboard con KPIs

2. **`/frontend-web/src/pages/Login.tsx`** - Página de login

3. **`/frontend-web/src/services/api.ts`** - Cliente Axios

4. **`/frontend-web/src/App.tsx`** - Actualizar con routing real

#### Mobile:

5. **`/mobile-app/src/screens/LoginScreen.tsx`** - Login mobile

6. **`/mobile-app/src/screens/conductor/DVIRScreen.tsx`** - DVIR Screen (CRÍTICO)

7. **`/mobile-app/src/navigation/AppNavigator.tsx`** - Navegación

### INSTRUCCIONES ESPECÍFICAS PARA AGENTE 2:

**CREA ESTOS 7 ARCHIVOS MÍNIMO EN LAS PRÓXIMAS 2 HORAS**

**Dónde documentar**:
En `/docs/agent_logs/AGENT_2_FRONTEND_LOG.md`, agrega:

```markdown
## 2025-11-14 21:00 - CREACIÓN FÍSICA DE ARCHIVOS

### Archivos creados físicamente:
- [x] /frontend-web/src/pages/Dashboard.tsx ✅
- [x] /frontend-web/src/pages/Login.tsx ✅
- [x] /frontend-web/src/services/api.ts ✅
- [x] /frontend-web/src/App.tsx actualizado ✅
- [x] /mobile-app/src/screens/LoginScreen.tsx ✅
- [x] /mobile-app/src/screens/conductor/DVIRScreen.tsx ✅
- [x] /mobile-app/src/navigation/AppNavigator.tsx ✅

### Verificación:
- [ ] Archivos existen físicamente en el workspace
- [ ] npm run dev funciona en frontend-web
- [ ] npm start funciona en mobile-app

### Deadline: 2 horas desde ahora
```

---

## 🎯 AGENTE 3 (QA)

### LO QUE DEBES VERIFICAR FÍSICAMENTE (AHORA):

Ya creaste la infraestructura de QA.  **VERIFICA** que estos archivos existen físicamente:

1. `/tests/backend/conftest.py`
2. `/tests/backend/pytest.ini`
3. `/backend/.flake8`
4. `/backend/pyproject.toml`

### LUEGO:

**Ejecuta**:
```bash
cd backend
docker-compose up -d
docker-compose logs backend
```

**Verifica**:
- ¿El backend levanta sin errores?
- ¿Responde en http://localhost:8000?

**Documenta** en `/docs/agent_logs/AGENT_3_QA_LOG.md`:

```markdown
## 2025-11-14 21:00 - VERIFICACIÓN FÍSICA DEL PROYECTO

### Archivos QA verificados:
- [ ] /tests/backend/conftest.py existe físicamente: SÍ/NO
- [ ] /tests/backend/pytest.ini existe físicamente: SÍ/NO
- [ ] /backend/.flake8 existe físicamente: SÍ/NO

### Backend Verification:
- [ ] Docker Compose inicia: SÍ/NO
- [ ] Backend responde en http://localhost:8000: SÍ/NO
- [ ] PostgreSQL acepta conexiones: SÍ/NO

### Errores encontrados:
[Listar cualquier error]
```

---

## ⏰ DEADLINE GENERAL

**TODOS LOS AGENTES: 2 HORAS DESDE AHORA (22:45 aprox.)**

---

## ✅ CRITERIOS DE ÉXITO

El proyecto está completo cuando:

1. **Backend funciona**:
   - `docker-compose up -d` no da errores
   - http://localhost:8000 muestra respuesta
   - http://localhost:8000/api/docs carga
   - PostgreSQL tiene las tablas creadas

2. **Frontend funciona**:
   - `npm run dev` no da errores
   - http://localhost:3000 carga algo
   - Conecta con backend

3. **Mobile funciona**:
   - `npm start` no da errores
   - App carga en Expo Go

---

## 📞 REPORTAR CUANDO TERMINES

Cada agente DEBE actualizar su log con:
- Lista de archivos creados
- Verificación de que existen físicamente
- Screenshot o evidencia si es posible

---

## 🚨 IMPORTANTE

**CREAR ARCHIVOS FÍSICAMENTE** significa:
- Usar herramienta `write` para crear el archivo en disco
- Verificar que el archivo aparece en el File Explorer
- NO solo "planear" o "reportar", sino CREAR

---

**COMIENZEN YA. Tengo 2 horas de deadline.**

---

**Agente 4 - Technical Lead & Supervisor**  
2025-11-14 20:45


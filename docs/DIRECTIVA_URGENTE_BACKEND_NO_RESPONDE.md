# 🚨 DIRECTIVA URGENTE: BACKEND NO RESPONDE EN LOCALHOST:8000

**Fecha**: 2025-01-27  
**Prioridad**: CRÍTICA  
**Estado**: ✅ RESUELTO - Ver `DOCKER_FIX_LOG.md` para cambios aplicados  
**Problema**: Usuario no puede acceder a http://localhost:8000 - "localhost rechazó la conexión"

**NOTA**: Este documento es de referencia histórica. Los problemas fueron resueltos por el agente de Docker. Ver `COMO_ABRIR_APP_FINAL.md` para instrucciones actuales.

---

## 🎯 OBJETIVO

El backend debe responder correctamente en http://localhost:8000. Actualmente el navegador dice "localhost rechazó la conexión", lo que significa que:

1. **El contenedor backend NO está corriendo**, O
2. **El contenedor está corriendo pero crasheó**, O
3. **El puerto 8000 no está expuesto correctamente**, O
4. **Hay un error en el código que impide que uvicorn inicie**

---

## ✅ VERIFICACIONES OBLIGATORIAS (EN ORDEN)

### 1. VERIFICAR QUE EL CONTENEDOR BACKEND ESTÁ CORRIENDO

**Comando**:
```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker ps
```

**Qué buscar**:
- Debe aparecer un contenedor llamado `fleet_backend`
- El STATUS debe ser "Up" (no "Exited", no "Restarting")
- El puerto debe mostrar "0.0.0.0:8000->8000/tcp"

**Si NO está corriendo**:
```bash
docker-compose up -d backend
```

**Si está en estado "Exited" o "Restarting"**:
→ **PROBLEMA CRÍTICO** - Ve al paso 2

---

### 2. REVISAR LOGS DEL CONTENEDOR BACKEND

**Comando**:
```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose logs backend
```

**O los últimos 100 líneas**:
```bash
docker-compose logs --tail=100 backend
```

**Qué buscar**:
- ❌ **Errores de importación**: `ModuleNotFoundError`, `ImportError`
- ❌ **Errores de sintaxis**: `SyntaxError`, `IndentationError`
- ❌ **Errores de conexión a DB**: `Connection refused`, `could not connect to server`
- ❌ **Errores de uvicorn**: `Address already in use`, `Permission denied`
- ❌ **Errores de dependencias**: `No module named 'xxx'`

**Si ves errores**:
→ **DOCUMENTA EL ERROR COMPLETO** en `man/docs/BACKEND_ERROR_LOG.md`
→ **CORRIGE EL ERROR** según corresponda

---

### 3. VERIFICAR QUE EL PUERTO 8000 NO ESTÁ OCUPADO

**Comando en PowerShell**:
```powershell
netstat -ano | findstr :8000
```

**Qué buscar**:
- Si hay un proceso usando el puerto 8000 que NO sea Docker
- Si el puerto está libre (no debería aparecer nada)

**Si hay conflicto**:
```powershell
# Encontrar PID del proceso
netstat -ano | findstr :8000

# Matar proceso (reemplaza PID con el número)
taskkill /PID <PID> /F
```

---

### 4. VERIFICAR CONFIGURACIÓN DE DOCKER-COMPOSE

**Archivo**: `man/backend/docker-compose.yml`

**Verificar**:
- ✅ Línea 35: `command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`
- ✅ Línea 39: `- "8000:8000"` (puerto host:puerto contenedor)
- ✅ Línea 47: `PYTHONPATH=/app`

**Si está mal**:
→ **CORREGIR** el archivo docker-compose.yml

---

### 5. VERIFICAR QUE EL CÓDIGO PUEDE INICIAR

**Problema común**: Errores de importación en `app/main.py`

**Verificar imports en `man/backend/app/main.py`**:
- Línea 8: `from app.core.config import settings` → ¿Existe `app/core/config.py`?
- Línea 9: `from app.api.v1 import auth` → ¿Existe `app/api/v1/auth.py`?
- Línea 10: `from app.db.base import Base` → ¿Existe `app/db/base.py`?
- Línea 13: `from app.models import Usuario, Vehiculo` → ¿Existen estos modelos?

**Comando para verificar**:
```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose exec backend python -c "from app.main import app; print('OK')"
```

**Si falla**:
→ **DOCUMENTA EL ERROR** y **CORRIGE** los imports faltantes

---

### 6. VERIFICAR CONEXIÓN A BASE DE DATOS

**Problema común**: El backend crashea al intentar conectar a PostgreSQL

**Verificar en logs**:
- Buscar: `could not connect to server`
- Buscar: `Connection refused`
- Buscar: `database "fleet_maintenance" does not exist`

**Verificar que PostgreSQL está corriendo**:
```bash
docker ps | findstr postgres
```

**Si PostgreSQL no está corriendo**:
```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d postgres
```

**Verificar variables de entorno en docker-compose.yml**:
- Línea 41: `POSTGRES_SERVER=postgres` (correcto para Docker)
- Línea 44: `POSTGRES_DB=fleet_maintenance`

**Verificar en `app/core/config.py`**:
- Línea 15: `POSTGRES_SERVER: str = "localhost"` → **PROBLEMA**: En Docker debe ser "postgres"
- Línea 19: `POSTGRES_PORT: int = 5432` → **CORRECTO** (puerto interno del contenedor)

**Si hay problema de configuración**:
→ **CORREGIR** `app/core/config.py` para que use variables de entorno de Docker

---

### 7. VERIFICAR QUE UVICORN ESTÁ INSTALADO

**Comando**:
```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose exec backend pip list | findstr uvicorn
```

**Si no está instalado**:
```bash
docker-compose exec backend pip install uvicorn[standard]
```

**Verificar requirements.txt**:
- Debe contener: `uvicorn[standard]==0.27.0` o similar

---

### 8. REINICIAR EL CONTENEDOR BACKEND

**Después de hacer correcciones**:
```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose restart backend
```

**O reconstruir si cambiaste código**:
```bash
docker-compose up -d --build backend
```

**Ver logs en tiempo real**:
```bash
docker-compose logs -f backend
```

**Buscar en los logs**:
- ✅ `Application startup complete`
- ✅ `Uvicorn running on http://0.0.0.0:8000`
- ✅ `Started reloader process`
- ❌ Cualquier error o excepción

---

## 🔧 PROBLEMAS COMUNES Y SOLUCIONES

### Problema 1: "ModuleNotFoundError: No module named 'app'"

**Causa**: PYTHONPATH incorrecto o estructura de carpetas mal

**Solución**:
1. Verificar que `docker-compose.yml` tiene: `PYTHONPATH=/app`
2. Verificar que el Dockerfile copia el código correctamente
3. Verificar que `app/` está en la raíz de `backend/`

---

### Problema 2: "could not connect to server: Connection refused"

**Causa**: PostgreSQL no está corriendo o backend intenta conectar antes de que PostgreSQL esté listo

**Solución**:
1. Verificar que `depends_on` en docker-compose.yml tiene `condition: service_healthy`
2. Verificar que PostgreSQL tiene healthcheck configurado
3. Agregar retry logic en `app/main.py` para la conexión a DB

---

### Problema 3: "Address already in use"

**Causa**: Puerto 8000 ocupado por otro proceso

**Solución**:
1. Matar proceso que usa puerto 8000 (ver paso 3)
2. O cambiar puerto en docker-compose.yml a otro (ej: 8001)

---

### Problema 4: Backend inicia pero crashea inmediatamente

**Causa**: Error en el código que se ejecuta al importar

**Solución**:
1. Revisar logs completos
2. Verificar que `init_db()` no falla
3. Verificar que todos los imports son correctos
4. Agregar try/except alrededor de código de inicialización

---

## 📝 DOCUMENTACIÓN REQUERIDA

**Crea/Actualiza**: `man/docs/BACKEND_ERROR_LOG.md`

**Formato**:
```markdown
# Backend Error Log

## [Fecha] - Diagnóstico Backend No Responde

### Verificación 1: Estado del Contenedor
- [ ] Contenedor corriendo: SÍ/NO
- [ ] Estado: Up/Exited/Restarting
- [ ] Puerto expuesto: SÍ/NO

### Verificación 2: Logs del Contenedor
```
[PEGAR LOGS COMPLETOS AQUÍ]
```

### Errores Encontrados:
1. [Error específico]
   - Ubicación: [archivo:línea]
   - Causa: [explicación]
   - Solución aplicada: [qué se hizo]

### Correcciones Realizadas:
1. [Archivo modificado]
   - Cambio: [qué se cambió]
   - Razón: [por qué]

### Verificación Final:
- [ ] Backend responde en http://localhost:8000
- [ ] Health check funciona: http://localhost:8000/health
- [ ] API docs carga: http://localhost:8000/api/docs
```

---

## ✅ CHECKLIST FINAL

Antes de marcar como resuelto, verifica:

- [ ] Contenedor `fleet_backend` está en estado "Up"
- [ ] Logs muestran "Uvicorn running on http://0.0.0.0:8000"
- [ ] No hay errores en los logs
- [ ] `curl http://localhost:8000` o abrir en navegador funciona
- [ ] `curl http://localhost:8000/health` retorna JSON con status "healthy"
- [ ] `http://localhost:8000/api/docs` carga Swagger UI
- [ ] Documentación completa en `BACKEND_ERROR_LOG.md`

---

## 🎯 PRIORIDADES

1. **CRÍTICO**: Verificar logs del contenedor (paso 2)
2. **CRÍTICO**: Corregir errores encontrados en logs
3. **ALTO**: Verificar configuración de Docker (paso 4)
4. **ALTO**: Verificar conexión a base de datos (paso 6)
5. **MEDIO**: Verificar imports y código (paso 5)

---

## 🚀 COMANDOS RÁPIDOS DE DIAGNÓSTICO

```bash
# 1. Ver estado de contenedores
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose ps

# 2. Ver logs del backend
docker-compose logs --tail=50 backend

# 3. Ver logs en tiempo real
docker-compose logs -f backend

# 4. Reiniciar backend
docker-compose restart backend

# 5. Reconstruir y reiniciar
docker-compose up -d --build backend

# 6. Entrar al contenedor para debug
docker-compose exec backend bash

# 7. Probar importación de app
docker-compose exec backend python -c "from app.main import app; print('OK')"

# 8. Verificar puerto 8000
netstat -ano | findstr :8000
```

---

**¡REVISA ESTO INMEDIATAMENTE Y CORRIGE EL PROBLEMA!**

El usuario necesita que el backend responda AHORA. No dejes pasar ningún error sin corregir.


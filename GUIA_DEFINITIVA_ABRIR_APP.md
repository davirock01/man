# 🚀 GUÍA DEFINITIVA - CÓMO ABRIR LA APLICACIÓN

**Fleet Maintenance System**  
**Última actualización**: 2025-01-27

---

## 📋 REQUISITOS PREVIOS

- ✅ Docker Desktop instalado y corriendo
- ✅ Node.js instalado (versión 16 o superior)
- ✅ Navegador web (Chrome, Firefox, Edge)

**Verificar Docker**:
```powershell
docker ps
```
Si ves una tabla (aunque esté vacía), Docker está funcionando. ✅

---

## 🎯 INICIO EN 3 PASOS

### PASO 1: Iniciar Servicios Base (PostgreSQL + Redis)

Abre **PowerShell** y ejecuta:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d postgres redis
```

**Espera 10-15 segundos** para que los servicios estén listos.

**Verificar**:
```powershell
docker-compose ps
```

**Debes ver**:
- ✅ `fleet_postgres` - Estado: Up (healthy)
- ✅ `fleet_redis` - Estado: Up (healthy)

---

### PASO 2: Iniciar Backend API

En la **misma terminal**, ejecuta:

```powershell
docker-compose up -d --build backend
```

**Verificar que inició correctamente**:
```powershell
docker-compose logs --tail=20 backend
```

**Busca en los logs**:
- ✅ `Uvicorn running on http://0.0.0.0:8000`
- ✅ `Application startup complete`
- ✅ `Database tables created successfully`

**Si ves errores**, ve a la sección "Solucionar Problemas" más abajo.

**Verificar en el navegador**:
1. Abre: **http://localhost:8000**
   - Deberías ver: `{"message": "Fleet Maintenance System API", ...}`

2. Abre: **http://localhost:8000/health**
   - Deberías ver: `{"status": "healthy", ...}`

3. Abre: **http://localhost:8000/api/docs**
   - Deberías ver la documentación Swagger UI

✅ **Si todo esto funciona, el backend está listo.**

---

### PASO 3: Iniciar Frontend Web

Abre una **NUEVA terminal** (PowerShell) y ejecuta:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm install
npm run dev
```

**Nota**: `npm install` solo es necesario la **primera vez**. Si ya tienes `node_modules`, puedes saltarlo.

**El navegador se abrirá automáticamente en**: **http://localhost:3000**

Si no se abre automáticamente, ábrelo manualmente.

---

## 🔑 INICIAR SESIÓN

En la pantalla de login (http://localhost:3000), usa estas credenciales:

| Rol | Email | Contraseña |
|-----|-------|------------|
| **Coordinador** | coordinador@test.com | testpass123 |
| **Conductor** | conductor@test.com | testpass123 |
| **Técnico** | tecnico@test.com | testpass123 |
| **Admin** | admin@test.com | testpass123 |

**Recomendado**: Usa `coordinador@test.com` para ver el dashboard completo.

---

## ✅ VERIFICACIÓN FINAL

**Todo está funcionando si**:

- [ ] Docker Desktop está corriendo
- [ ] PostgreSQL está corriendo (puerto 5435)
- [ ] Redis está corriendo (puerto 6380)
- [ ] Backend responde en http://localhost:8000
- [ ] Health check funciona: http://localhost:8000/health
- [ ] Frontend se abre en http://localhost:3000
- [ ] Puedes hacer login con las credenciales de prueba

---

## 🆘 SOLUCIONAR PROBLEMAS

### Problema 1: "localhost rechazó la conexión" en http://localhost:8000

**Diagnóstico**:
```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man"
DIAGNOSTICAR_BACKEND.bat
```

**Soluciones**:

**A) Contenedor backend no está corriendo**:
```powershell
cd backend
docker-compose up -d backend
```

**B) Contenedor crasheó (estado "Exited")**:
```powershell
# Ver el error
docker-compose logs backend

# Reconstruir y reiniciar
docker-compose up -d --build backend

# Ver logs en tiempo real
docker-compose logs -f backend
```

**C) Error de conexión a PostgreSQL**:
```powershell
# Verificar que PostgreSQL está corriendo
docker ps | findstr postgres

# Si no está corriendo
docker-compose up -d postgres

# Esperar 10 segundos y reiniciar backend
timeout /t 10
docker-compose restart backend
```

**D) Puerto 8000 ocupado**:
```powershell
# Ver qué proceso usa el puerto
netstat -ano | findstr :8000

# Matar el proceso (reemplaza <PID> con el número que aparece)
taskkill /PID <PID> /F

# Reiniciar backend
docker-compose restart backend
```

---

### Problema 2: Frontend no se conecta al backend

**Síntomas**:
- Frontend carga pero muestra errores en consola
- No puede hacer login
- Errores de CORS

**Soluciones**:

1. **Verificar que backend está corriendo**:
   - Abre: http://localhost:8000/health
   - Debe responder con JSON

2. **Verificar CORS** (ya está configurado, pero verifica):
   - Abre consola del navegador (F12)
   - Busca errores de CORS
   - Si hay errores, el backend necesita reiniciarse

3. **Reiniciar backend**:
   ```powershell
   cd backend
   docker-compose restart backend
   ```

---

### Problema 3: "ModuleNotFoundError" o errores de imports

**Solución**:
```powershell
cd backend
docker-compose exec backend pip install -r requirements.txt
docker-compose restart backend
```

---

### Problema 4: Frontend muestra "npm: command not found"

**Solución**:
1. Instala Node.js desde: https://nodejs.org/
2. Reinicia la terminal
3. Verifica: `node --version` y `npm --version`
4. Vuelve a ejecutar `npm install` y `npm run dev`

---

### Problema 5: "Port 3000 is already in use"

**Solución**:
```powershell
# Matar proceso en puerto 3000
npx kill-port 3000

# O usar otro puerto (edita frontend-web/vite.config.ts)
```

---

## 📞 COMANDOS ÚTILES

### Ver estado de todos los servicios
```powershell
cd backend
docker-compose ps
```

### Ver logs del backend (últimas 50 líneas)
```powershell
docker-compose logs --tail=50 backend
```

### Ver logs en tiempo real
```powershell
docker-compose logs -f backend
```

### Reiniciar backend
```powershell
docker-compose restart backend
```

### Reconstruir y reiniciar backend
```powershell
docker-compose up -d --build backend
```

### Detener todos los servicios
```powershell
docker-compose down
```

### Iniciar todo de nuevo
```powershell
docker-compose up -d
```

### Verificar puerto 8000
```powershell
netstat -ano | findstr :8000
```

---

## 🔄 FLUJO COMPLETO DE INICIO

```powershell
# Terminal 1: Backend
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d postgres redis
timeout /t 15
docker-compose up -d --build backend
docker-compose logs -f backend

# Terminal 2: Frontend (nueva terminal)
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm run dev
```

---

## 📍 URLs IMPORTANTES

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **Frontend Web** | http://localhost:3000 | Aplicación principal (LOGIN AQUÍ) |
| **Backend API** | http://localhost:8000 | API REST |
| **Health Check** | http://localhost:8000/health | Verificar estado del backend |
| **API Docs (Swagger)** | http://localhost:8000/api/docs | Documentación interactiva |
| **ReDoc** | http://localhost:8000/api/redoc | Documentación alternativa |

---

## 🎯 RESUMEN RÁPIDO (Copy-Paste)

```powershell
# 1. Iniciar servicios base
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d postgres redis

# 2. Esperar 15 segundos
timeout /t 15

# 3. Iniciar backend
docker-compose up -d --build backend

# 4. Verificar (en navegador)
# http://localhost:8000
# http://localhost:8000/health

# 5. En NUEVA terminal: Iniciar frontend
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm run dev

# 6. Abrir navegador
# http://localhost:3000
```

---

## 📚 DOCUMENTACIÓN ADICIONAL

- **Cambios realizados**: `docs/DOCKER_FIX_LOG.md`
- **Resumen de agentes**: `docs/RESUMEN_CAMBIOS_AGENTES.md`
- **Diagnóstico automático**: Ejecuta `DIAGNOSTICAR_BACKEND.bat`

---

## ✅ CHECKLIST DE INICIO

Usa este checklist cada vez que inicies la app:

- [ ] Docker Desktop está corriendo
- [ ] Ejecuté `docker-compose up -d postgres redis`
- [ ] Esperé 15 segundos
- [ ] Ejecuté `docker-compose up -d --build backend`
- [ ] Verifiqué que http://localhost:8000 responde
- [ ] Verifiqué que http://localhost:8000/health funciona
- [ ] Ejecuté `npm run dev` en frontend-web
- [ ] Abrí http://localhost:3000 en el navegador
- [ ] Puedo hacer login con las credenciales de prueba

---

## 🎉 ¡LISTO!

Si seguiste todos los pasos, deberías tener:

- ✅ Backend API funcionando en http://localhost:8000
- ✅ Frontend Web funcionando en http://localhost:3000
- ✅ Puedes hacer login y usar la aplicación

**Si algo no funciona**, revisa la sección "Solucionar Problemas" arriba o ejecuta `DIAGNOSTICAR_BACKEND.bat`.

---

**¡Disfruta usando la aplicación!** 🚀


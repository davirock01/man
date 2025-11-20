# 🚀 CÓMO ABRIR LA APLICACIÓN - GUÍA FINAL

**Fecha**: 2025-01-27  
**Estado**: Docker configurado, Backend necesita iniciarse

---

## ✅ VERIFICACIÓN PREVIA

### Paso 1: Verificar Docker Desktop

Asegúrate que Docker Desktop está corriendo (ícono de ballena en la barra de tareas).

### Paso 2: Verificar Servicios Base

Abre PowerShell y ejecuta:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose ps
```

**Debes ver**:
- ✅ `fleet_postgres` - Estado: Up (puerto 5435)
- ✅ `fleet_redis` - Estado: Up (puerto 6380)

**Si NO están corriendo**:
```powershell
docker-compose up -d postgres redis
```

---

## 🎯 INICIAR EL BACKEND

### Opción A: Con Docker (Recomendado)

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d --build backend
```

**Verificar que inició**:
```powershell
docker-compose logs --tail=20 backend
```

**Busca en los logs**:
- ✅ `Uvicorn running on http://0.0.0.0:8000`
- ✅ `Application startup complete`
- ❌ Si ves errores, revisa la sección de problemas abajo

### Opción B: Sin Docker (Alternativa)

Si el contenedor Docker no funciona, puedes iniciar el backend directamente:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Nota**: Asegúrate de tener Python 3.11+ y las dependencias instaladas:
```powershell
pip install -r requirements.txt
```

---

## ✅ VERIFICAR QUE EL BACKEND FUNCIONA

Abre en tu navegador:

1. **http://localhost:8000** 
   - Deberías ver: `{"message": "Fleet Maintenance System API", ...}`

2. **http://localhost:8000/health**
   - Deberías ver: `{"status": "healthy", ...}`

3. **http://localhost:8000/api/docs**
   - Deberías ver la documentación Swagger UI

**Si NO funciona**: Ve a la sección "Solucionar Problemas" abajo.

---

## 🌐 INICIAR EL FRONTEND

Abre una **nueva terminal** (PowerShell) y ejecuta:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm install
npm run dev
```

**Nota**: `npm install` solo es necesario la primera vez.

**El navegador se abrirá automáticamente en**: http://localhost:3000

---

## 🔑 CREDENCIALES DE PRUEBA

| Rol | Email | Contraseña |
|-----|-------|------------|
| Coordinador | coordinador@test.com | testpass123 |
| Conductor | conductor@test.com | testpass123 |
| Técnico | tecnico@test.com | testpass123 |
| Admin | admin@test.com | testpass123 |

---

## 🆘 SOLUCIONAR PROBLEMAS

### Problema: Backend no responde en localhost:8000

**Diagnóstico rápido**:
```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man"
DIAGNOSTICAR_BACKEND.bat
```

**Soluciones**:

1. **Contenedor backend no está corriendo**:
   ```powershell
   cd backend
   docker-compose up -d backend
   ```

2. **Contenedor crasheó (estado Exited)**:
   ```powershell
   docker-compose logs backend  # Ver error
   docker-compose up -d --build backend  # Reconstruir
   ```

3. **Error de conexión a PostgreSQL**:
   - Verifica que PostgreSQL está corriendo: `docker ps | findstr postgres`
   - Si no está: `docker-compose up -d postgres`
   - Espera 10 segundos y reinicia backend: `docker-compose restart backend`

4. **Puerto 8000 ocupado**:
   ```powershell
   netstat -ano | findstr :8000
   # Matar proceso si es necesario
   taskkill /PID <PID> /F
   ```

### Problema: Frontend no se conecta al backend

**Verifica**:
1. Backend está corriendo: http://localhost:8000/health
2. CORS está configurado (ya está en `main.py`)
3. No hay errores en consola del navegador (F12)

### Problema: "ModuleNotFoundError" en backend

**Solución**:
```powershell
cd backend
docker-compose exec backend pip install -r requirements.txt
docker-compose restart backend
```

---

## 📋 RESUMEN RÁPIDO

```powershell
# Terminal 1: Iniciar Backend
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d --build backend

# Terminal 2: Iniciar Frontend
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm run dev
```

**URLs**:
- 🌐 Frontend: http://localhost:3000
- 🔧 Backend: http://localhost:8000
- 📚 API Docs: http://localhost:8000/api/docs

---

## ✅ CHECKLIST FINAL

Antes de reportar problemas, verifica:

- [ ] Docker Desktop está corriendo
- [ ] PostgreSQL está corriendo (`docker ps` muestra `fleet_postgres`)
- [ ] Redis está corriendo (`docker ps` muestra `fleet_redis`)
- [ ] Backend está corriendo (`docker ps` muestra `fleet_backend` O proceso Python)
- [ ] http://localhost:8000 responde
- [ ] http://localhost:8000/health retorna JSON
- [ ] Frontend tiene `node_modules` instalado
- [ ] Frontend se inicia sin errores
- [ ] Navegador abre http://localhost:3000

---

## 📞 COMANDOS ÚTILES

```powershell
# Ver estado de contenedores
docker-compose ps

# Ver logs del backend
docker-compose logs -f backend

# Reiniciar backend
docker-compose restart backend

# Reconstruir backend
docker-compose up -d --build backend

# Detener todo
docker-compose down

# Verificar puerto 8000
netstat -ano | findstr :8000
```

---

**¡Listo! La aplicación debería estar funcionando.** 🚀

Si encuentras problemas, revisa la sección "Solucionar Problemas" o ejecuta `DIAGNOSTICAR_BACKEND.bat`.


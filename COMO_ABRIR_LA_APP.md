# 🚀 CÓMO ABRIR LA APLICACIÓN - GUÍA COMPLETA

**Fecha**: 2025-01-27  
**Estado**: ✅ Docker funcionando (PostgreSQL 5435, Redis 6380, Backend 8000)

---

## ✅ VERIFICACIÓN PREVIA

Antes de continuar, verifica que Docker esté funcionando:

```bash
docker ps
```

Deberías ver los contenedores:
- `fleet_postgres` (puerto 5435)
- `fleet_redis` (puerto 6380)
- `fleet_backend` (puerto 8000)

Si no están corriendo, ejecuta:
```bash
cd man/backend
docker-compose up -d
```

---

## 🎯 PASOS PARA ABRIR LA APP COMPLETA

### PASO 1: Verificar Backend API (Ya está corriendo)

Abre en tu navegador:
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/api/docs
- **Health Check**: http://localhost:8000/health

**Deberías ver**:
```json
{
  "message": "Fleet Maintenance System API",
  "docs": "/api/docs",
  "health": "/health",
  "version": "1.0.0"
}
```

✅ **Si ves esto, el backend está funcionando correctamente.**

---

### PASO 2: Iniciar Frontend Web

Abre una **nueva terminal** (PowerShell o CMD) y ejecuta:

```bash
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm install
npm run dev
```

**Nota**: `npm install` solo es necesario la primera vez. Si ya tienes `node_modules`, puedes saltarlo.

**El frontend se abrirá automáticamente en**: http://localhost:3000

---

### PASO 3: Usar la Aplicación

1. **Abre el navegador** en: http://localhost:3000
2. **Verás la pantalla de Login**
3. **Usa estas credenciales de prueba**:

| Rol | Email | Contraseña |
|-----|-------|------------|
| Coordinador | coordinador@test.com | testpass123 |
| Conductor | conductor@test.com | testpass123 |
| Técnico | tecnico@test.com | testpass123 |
| Admin | admin@test.com | testpass123 |

4. **Después del login**, serás redirigido al Dashboard

---

## 📋 RESUMEN RÁPIDO

```bash
# Terminal 1: Verificar Docker (ya está corriendo)
docker ps

# Terminal 2: Iniciar Frontend
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm run dev
```

**URLs importantes**:
- 🌐 **Frontend Web**: http://localhost:3000
- 🔧 **Backend API**: http://localhost:8000
- 📚 **API Docs**: http://localhost:8000/api/docs
- ❤️ **Health Check**: http://localhost:8000/health

---

## 🔍 VERIFICACIÓN DE CONFIGURACIÓN

### Backend (Docker)
- ✅ PostgreSQL: Puerto 5435
- ✅ Redis: Puerto 6380
- ✅ Backend API: Puerto 8000

### Frontend
- ✅ Puerto: 3000
- ✅ API URL: http://localhost:8000 (configurado en `frontend-web/src/services/api.ts`)
- ✅ CORS: Configurado en backend para aceptar `http://localhost:3000`

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Problema: "Port 3000 is already in use"

**Solución**:
```bash
# Opción 1: Matar proceso en puerto 3000
npx kill-port 3000

# Opción 2: Usar otro puerto
# Edita frontend-web/vite.config.ts y cambia el puerto
```

### Problema: Frontend no se conecta al backend

**Verifica**:
1. Backend está corriendo: http://localhost:8000/health
2. CORS está configurado (ya está en `main.py`)
3. No hay firewall bloqueando

**Solución**:
```bash
# Verificar que backend responde
curl http://localhost:8000/health
```

### Problema: "npm: command not found"

**Solución**:
1. Instala Node.js desde: https://nodejs.org/
2. Reinicia la terminal
3. Verifica: `node --version` y `npm --version`

### Problema: Frontend muestra errores en consola

**Verifica**:
1. Backend está corriendo (http://localhost:8000)
2. Revisa la consola del navegador (F12) para ver errores específicos
3. Verifica que `frontend-web/src/services/api.ts` apunta a `http://localhost:8000`

---

## 📝 ESTRUCTURA DE LA APP

```
man/
├── backend/              ✅ Docker (PostgreSQL + Redis + Backend API)
│   └── docker-compose.yml
│
├── frontend-web/         ✅ React + TypeScript + Vite
│   ├── src/
│   │   ├── pages/       (Login, Dashboard, etc.)
│   │   ├── components/  (Componentes reutilizables)
│   │   ├── services/    (API client)
│   │   └── store/       (Estado global)
│   └── package.json
│
└── docs/                 ✅ Documentación
```

---

## ✅ CHECKLIST DE VERIFICACIÓN

Antes de reportar problemas, verifica:

- [ ] Docker Desktop está corriendo
- [ ] Contenedores Docker están activos (`docker ps`)
- [ ] Backend responde en http://localhost:8000
- [ ] Health check funciona: http://localhost:8000/health
- [ ] Frontend tiene `node_modules` instalado
- [ ] Frontend se inicia sin errores (`npm run dev`)
- [ ] Navegador abre http://localhost:3000
- [ ] Puedes hacer login con credenciales de prueba

---

## 🎯 COMANDOS ÚTILES

```bash
# Ver logs del backend
cd man/backend
docker-compose logs -f backend

# Reiniciar servicios Docker
cd man/backend
docker-compose restart

# Detener servicios Docker
cd man/backend
docker-compose down

# Ver estado de contenedores
docker ps

# Ver logs del frontend (en la terminal donde corre npm run dev)
# Los logs aparecen automáticamente
```

---

## 📞 PRÓXIMOS PASOS

Una vez que la app esté corriendo:

1. **Probar Login**: Usa las credenciales de prueba
2. **Explorar Dashboard**: Ver las funcionalidades disponibles
3. **Revisar API Docs**: http://localhost:8000/api/docs para ver endpoints disponibles
4. **Probar Endpoints**: Usa Swagger UI para probar la API directamente

---

**¡Listo! La aplicación debería estar funcionando completamente.** 🚀

Si encuentras algún problema, revisa la sección "Solución de Problemas" arriba o consulta los logs.


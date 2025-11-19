# 🚀 INICIO RÁPIDO - FLEET MAINTENANCE SYSTEM

**Guía simplificada para iniciar la aplicación**

---

## ⚡ INICIO EN 3 PASOS

### 1️⃣ Verificar Docker

Abre PowerShell y ejecuta:

```powershell
docker ps
```

Si ves contenedores o una tabla vacía, Docker está funcionando. ✅

Si hay error, inicia Docker Desktop y espera 1-2 minutos.

---

### 2️⃣ Iniciar Backend

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d --build backend
```

**Verificar que funciona**:
- Abre: http://localhost:8000
- Deberías ver: `{"message": "Fleet Maintenance System API"}`

---

### 3️⃣ Iniciar Frontend

Abre una **nueva terminal**:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm run dev
```

**El navegador se abrirá en**: http://localhost:3000

---

## 🔑 LOGIN

**Email**: `coordinador@test.com`  
**Contraseña**: `testpass123`

---

## 🆘 SI ALGO FALLA

Ejecuta el diagnóstico:
```
DIAGNOSTICAR_BACKEND.bat
```

O lee la guía completa: `COMO_ABRIR_APP_FINAL.md`

---

**¡Listo!** 🎉


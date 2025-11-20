# 🚨 SOLUCIÓN AL PROBLEMA: Docker no puede descargar imágenes

**Error recibido**:
```
failed to resolve source metadata for docker.io/library/python:3.11-slim
dial tcp: lookup registry-1.docker.io: no such host
```

## 🎯 CAUSA DEL PROBLEMA

**No tienes conexión a internet** o **hay un problema de DNS** y Docker no puede descargar la imagen de Python desde Docker Hub.

---

## ✅ SOLUCIÓN INMEDIATA (SIN INTERNET)

### Opción A: Usar script sin Docker para el backend

He creado un script que **NO usa Docker para el backend**, solo para PostgreSQL y Redis:

**Archivo**: `ABRIR_APP_SIN_DOCKER.bat`

**Haz doble clic** en `ABRIR_APP_SIN_DOCKER.bat`

Este script:
1. Usa Docker SOLO para PostgreSQL y Redis (ya tienes esas imágenes localmente)
2. Corre el backend **localmente con Python** (no necesita internet)
3. Inicia el frontend normalmente

**Requisito**: Python 3.11+ instalado en tu PC

---

### Opción B: Manual (si tienes Python)

```powershell
# Terminal 1: Iniciar solo PostgreSQL y Redis
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
docker-compose up -d postgres redis

# Terminal 2: Iniciar Backend local
cd "C:\Users\User-PC\Desktop\software engineering\app\man\backend"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 3: Iniciar Frontend
cd "C:\Users\User-PC\Desktop\software engineering\app\man\frontend-web"
npm run dev
```

---

## 🔧 SOLUCIÓN PERMANENTE (Arreglar Docker)

### 1. Verificar conexión a internet

```powershell
ping google.com
ping registry-1.docker.io
```

Si falla, tienes problema de internet o DNS.

### 2. Configurar DNS en Docker Desktop

1. Abre **Docker Desktop**
2. Ve a **Settings** (⚙️)
3. Ve a **Docker Engine**
4. Agrega esto en la configuración JSON:

```json
{
  "dns": ["8.8.8.8", "8.8.4.4"]
}
```

5. Haz clic en **Apply & Restart**

### 3. Configurar DNS en Windows

1. Abre **Panel de Control** → **Red e Internet** → **Centro de redes y recursos compartidos**
2. Haz clic en tu conexión activa
3. Haz clic en **Propiedades**
4. Selecciona **Protocolo de Internet versión 4 (TCP/IPv4)**
5. Haz clic en **Propiedades**
6. Selecciona **Usar las siguientes direcciones de servidor DNS**:
   - DNS preferido: `8.8.8.8`
   - DNS alternativo: `8.8.4.4`
7. Haz clic en **Aceptar**

### 4. Reiniciar Docker Desktop

Cierra Docker Desktop completamente y vuelve a abrirlo.

### 5. Probar de nuevo

Ejecuta `ABRIR_APP.bat` de nuevo.

---

## 🎯 RESUMEN

**AHORA MISMO** (sin arreglar Docker):
- Usa: `ABRIR_APP_SIN_DOCKER.bat` ⭐ **SOLUCIÓN INMEDIATA**

**DESPUÉS** (cuando arregles internet/DNS):
- Configura DNS en Docker Desktop
- Usa: `ABRIR_APP.bat`

---

## ✅ VENTAJAS DE ABRIR_APP_SIN_DOCKER.bat

1. **Funciona sin internet** ✅
2. **No necesita descargar imágenes Docker** ✅
3. **Más rápido para desarrollo** ✅
4. **Más fácil de debuggear** ✅
5. **Usa las mismas bases de datos (PostgreSQL y Redis en Docker)** ✅

---

**Usa `ABRIR_APP_SIN_DOCKER.bat` y listo.** 🚀


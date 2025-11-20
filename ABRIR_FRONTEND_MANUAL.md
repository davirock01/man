# 🎯 ABRIR FRONTEND - INSTRUCCIONES MANUALES

**Fecha**: 2025-11-14 22:00  
**Para**: Cliente

---

## ⚡ PASOS EXACTOS (Copia y pega cada comando)

### PASO 1: Abrir PowerShell

Ya lo tienes abierto ✅

---

### PASO 2: Ir a la carpeta frontend

```powershell
cd frontend-web
```

---

### PASO 3: Instalar dependencias (solo primera vez)

```powershell
npm install
```

**Esto tardará 2-3 minutos**. Verás muchos mensajes de instalación.

**Espera hasta que termine** (vuelve a aparecer `PS C:\...>`).

---

### PASO 4: Iniciar el servidor

```powershell
npm run dev
```

**Espera 10-15 segundos**. Deberías ver:

```
VITE v5.0.11  ready in 1234 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

---

### PASO 5: Abrir en navegador

Abre tu navegador y ve a:

```
http://localhost:3000
```

**Deberías ver**: Página de login elegante con gradiente morado

---

## 🆘 SI DA ERROR

### Error: "npm: command not found"

**Node.js no está instalado.**

Descarga e instala: https://nodejs.org/

Elige la versión **LTS** (recomendada).

---

### Error durante "npm install"

```powershell
# Limpiar caché
npm cache clean --force

# Intentar de nuevo
npm install
```

---

### Error: "Port 3000 is already in use"

```powershell
# Matar proceso en puerto 3000
npx kill-port 3000

# Intentar de nuevo
npm run dev
```

---

## 📞 SI SIGUE SIN FUNCIONAR

Envíame el **mensaje de error completo** que aparece después de ejecutar `npm run dev`.

---

**Agente 4 - Supervisor**


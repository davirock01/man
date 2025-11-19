# 🎯 CÓMO USAR EL SISTEMA - GUÍA COMPLETA

**Para**: Cliente  
**De**: Agente 4 - Supervisor  
**Fecha**: 2025-11-14 21:40

---

## ⚡ OPCIÓN 1: INICIAR TODO (RECOMENDADA)

Haz doble clic en:

### **`INICIAR_TODO.bat`** ⭐

**Qué hace**:
- Inicia Backend (localhost:8000)
- Inicia Frontend (localhost:3000)
- Abre 2 ventanas (NO las cierres)

**Tiempo**: 3-5 minutos la primera vez

---

## ⚡ OPCIÓN 2: INICIAR SEPARADO

### Primero el Backend:
```
Doble clic: INICIAR_BACKEND_SIMPLE.bat
```

### Luego el Frontend (en nueva terminal):
```
Doble clic: INICIAR_FRONTEND.bat
```

---

## 🌐 URLS IMPORTANTES

Una vez iniciado todo:

| Servicio | URL | Qué es |
|----------|-----|--------|
| **Frontend** | http://localhost:3000 | Aplicación web (LOGIN aquí) |
| **Backend API** | http://localhost:8000 | API REST |
| **API Docs** | http://localhost:8000/api/docs | Documentación Swagger |

---

## 👤 USUARIOS DE PRUEBA

Todos con password: **`testpass123`**

| Email | Rol | Acceso |
|-------|-----|--------|
| coordinador@test.com | COORDINADOR | Dashboard completo |
| admin@test.com | ADMIN | Todos los módulos |
| conductor@test.com | CONDUCTOR | App móvil (futuro) |
| tecnico@test.com | TECNICO | App móvil (futuro) |

---

## 🧪 CÓMO PROBAR

### 1. Abrir Frontend

```
http://localhost:3000
```

Verás pantalla de **Login** elegante con:
- Campo email
- Campo password
- Botones rápidos para usuarios de prueba

### 2. Login

**Opción A - Login rápido**:
- Click en el botón "👔 Coordinador: coordinador@test.com"
- Click "Iniciar Sesión"

**Opción B - Login manual**:
- Email: `coordinador@test.com`
- Password: `testpass123`
- Click "Iniciar Sesión"

### 3. Ver Dashboard

Después del login, verás el **Dashboard** con:

**KPIs Principales**:
- Cumplimiento PM: 87.5%
- Disponibilidad Flota: 90%
- MTBF: 45.2 días
- MTTR: 6.5 horas

**Estado de Flota**:
- Total: 50 vehículos
- Operativos: 45
- No operativos: 3
- En mantenimiento: 2

**Paneles de Alertas**:
- 🔮 Alertas Predictivas: 8
- 🚨 Alertas Reactivas: 5
- 📊 Patrones Recurrentes: 2

**Órdenes de Trabajo**:
- Pendientes: 12
- En progreso: 8
- Vencidas: 2

---

## 📊 LO QUE FUNCIONA AHORA

### Backend ✅
- API REST corriendo
- Login con JWT
- Base de datos SQLite
- 4 usuarios + 2 vehículos de prueba
- Swagger UI documentación

### Frontend Web ✅
- Página de Login elegante
- Botones rápidos para login
- Dashboard completo con:
  - KPIs en tarjetas
  - Estado de flota
  - 3 paneles de alertas
  - Resumen de OT
- Routing (Login ↔ Dashboard)
- Auth con Zustand
- Logout funcional

### Total Archivos Creados: 75

---

## 🎯 FLUJO COMPLETO

```
1. INICIAR_TODO.bat
   ↓
2. Esperar 3-5 min
   ↓
3. Abrir http://localhost:3000
   ↓
4. Ver página de Login elegante
   ↓
5. Click en botón "Coordinador"
   ↓
6. Click "Iniciar Sesión"
   ↓
7. Ver Dashboard completo con KPIs
   ↓
8. Click "Cerrar Sesión" para volver al login
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### "npm not found"

Instala Node.js: https://nodejs.org/

### "Port 3000 already in use"

```bash
# Detener proceso en puerto 3000
npx kill-port 3000

# O cambiar puerto en vite.config.ts
```

### "Backend no responde"

Verifica que el backend esté corriendo (ventana separada).

### Frontend no carga

```bash
cd frontend-web
rm -rf node_modules
npm install
npm run dev
```

---

## 📁 ARCHIVOS DEL FRONTEND

```
frontend-web/
├── package.json               ✅ Dependencias
├── vite.config.ts             ✅ Configuración Vite
├── tsconfig.json              ✅ TypeScript config
├── tsconfig.node.json         ✅ TypeScript Node config
├── index.html                 ✅ HTML principal
└── src/
    ├── main.tsx               ✅ Entry point
    ├── App.tsx                ✅ Routing
    ├── index.css              ✅ Estilos globales
    ├── pages/
    │   ├── Login.tsx          ✅ Página Login
    │   └── Dashboard.tsx      ✅ Dashboard completo
    ├── services/
    │   └── api.ts             ✅ Cliente API
    └── store/
        └── authStore.ts       ✅ Auth state management
```

---

## ✅ CARACTERÍSTICAS DEL FRONTEND

### Login Page
- ✅ Diseño elegante (gradiente morado)
- ✅ Formulario funcional
- ✅ Botones rápidos para usuarios de prueba
- ✅ Validación
- ✅ Mensajes de error
- ✅ Loading state

### Dashboard
- ✅ Header con usuario y logout
- ✅ 4 KPIs principales con colores
- ✅ Estado de flota (grid responsive)
- ✅ 3 paneles de alertas (con hover effect)
- ✅ Resumen de Órdenes de Trabajo
- ✅ Diseño moderno y limpio
- ✅ Responsive (funciona en desktop y tablet)

### Arquitectura
- ✅ React 18 + TypeScript
- ✅ Vite (build tool rápido)
- ✅ React Router (navegación)
- ✅ Zustand (state management)
- ✅ Axios (HTTP client)
- ✅ JWT authentication
- ✅ Protected routes

---

## 🚀 PRÓXIMOS PASOS

Una vez veas el Dashboard funcionando:

### Yo puedo agregar:
1. Página de Alertas (lista filtrable)
2. Página de Vehículos (lista + detalle)
3. Página de Órdenes de Trabajo
4. Página de Admin (usuarios, config)

**Pero primero prueba lo que está** y dime si te gusta el diseño.

---

## 📞 EJECUTA ESTO

```
Doble clic en: INICIAR_TODO.bat
```

**Espera 3-5 minutos** y luego abre: **http://localhost:3000**

**Dime qué ves** 😊

---

**Agente 4 - Supervisor**  
*Frontend web completo con Login + Dashboard* 🎨


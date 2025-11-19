# 🚗 FLEET MAINTENANCE SYSTEM

Sistema de mantenimiento para vehículos de transporte especial (pick-ups y turbos) del sector petrolero.

---

## 🚀 INICIO RÁPIDO - UN SOLO CLIC

### 🪟 Windows
**Haz doble clic en**: `MANTENIMIENTO.bat`

### 🐧 Linux / Mac
```bash
chmod +x MANTENIMIENTO.sh
./MANTENIMIENTO.sh
```

Esto iniciará automáticamente todo el sistema y abrirá el navegador.

---

## 📋 ACCESOS RÁPIDOS

| Servicio | URL | Usuario Demo |
|----------|-----|--------------|
| 🌐 **Frontend Web** | http://localhost:3000 | coordinador@test.com / testpass123 |
| 🔧 **Backend API** | http://localhost:8000 | - |
| 📚 **API Docs** | http://localhost:8000/api/docs | Documentación interactiva |
| 📱 **Mobile App** | Expo Go (ver instrucciones abajo) | conductor@test.com / testpass123 |

---

## 📱 CÓMO VER LA APP MÓVIL

### Opción 1: En tu teléfono (Recomendado)

1. **Instala Expo Go**:
   - [Android - Google Play](https://play.google.com/store/apps/details?id=host.exp.exponent)
   - [iOS - App Store](https://apps.apple.com/app/expo-go/id982107779)

2. **Inicia el proyecto**:
   ```bash
   cd mobile-app
   npm install    # Solo primera vez
   npm start
   ```

3. **Escanea el código QR**:
   - Android: Abre Expo Go → "Scan QR Code"
   - iOS: Abre Cámara → Escanea QR → Toca notificación

4. **Login**: 
   - Email: `conductor@test.com`
   - Password: `testpass123`

### Opción 2: Emulador/Simulador

```bash
cd mobile-app
npm run android  # Android (requiere Android Studio)
npm run ios      # iOS (requiere Xcode - solo Mac)
```

---

## 🎯 FUNCIONALIDADES PRINCIPALES

### ✅ IMPLEMENTADO Y FUNCIONANDO

| Módulo | Descripción | Acceso |
|--------|-------------|--------|
| **DVIR Digital** ⭐ | Checklist preoperativo optimizado (≤5 min) | Mobile - Conductor |
| **Dashboard** | KPIs, alertas, estado de flota | Web - Coordinador |
| **Gestión de Alertas** | Predictivas y reactivas | Web - Coordinador |
| **Órdenes de Trabajo** | Crear, asignar, ejecutar OT | Web + Mobile |
| **Health Score** | Score de salud de vehículos (0-100) | Web + Mobile |
| **Offline-First** | App funciona sin conexión | Mobile |
| **Admin Panel** | Usuarios, vehículos, configuración | Web - Admin |

---

## 👥 USUARIOS DE PRUEBA

| Rol | Email | Password | Descripción |
|-----|-------|----------|-------------|
| **Conductor** | conductor@test.com | testpass123 | Hace DVIR, reporta defectos |
| **Coordinador** | coordinador@test.com | testpass123 | Dashboard, alertas, crea OT |
| **Técnico** | tecnico@test.com | testpass123 | Ejecuta OT, registra repuestos |
| **Admin** | admin@test.com | admin123 | Configuración del sistema |

---

## 📚 DOCUMENTACIÓN COMPLETA

### Para Usuarios
- **[COMO_REVISAR_EL_SISTEMA.md](./COMO_REVISAR_EL_SISTEMA.md)** ← **LEE ESTO PRIMERO**
  - Cómo probar cada funcionalidad
  - Cómo ver la app móvil
  - Solución de problemas
  - URLs importantes

### Para Desarrolladores
- **Backend**: `/backend/README.md`
- **Frontend**: `/frontend-web/README.md`
- **Mobile**: `/mobile-app/README.md`

### Documentación del Proyecto
- **Estado del Proyecto**: `/docs/PROJECT_STATUS.md`
- **Bugs Conocidos**: `/docs/agent_logs/BUGS_TRACKER.md`
- **Coordinación del Equipo**: `/docs/TEAM_COORDINATION.md`

---

## 🏗️ ARQUITECTURA

```
┌─────────────────────────────────────────┐
│         FRONTEND WEB (React)            │
│  Dashboard │ Alertas │ OT │ Admin      │
└────────────┬────────────────────────────┘
             │
┌────────────┴────────────────────────────┐
│         MOBILE APP (React Native)       │
│  DVIR │ Defectos │ OT (Técnico)        │
└────────────┬────────────────────────────┘
             │
             │ REST API (JWT Auth)
             │
┌────────────▼────────────────────────────┐
│      BACKEND API (FastAPI/Python)       │
├─────────────────────────────────────────┤
│ • DVIRService     • HealthService       │
│ • AlertService    • WorkOrderService    │
│ • PredictionService • SyncService       │
└────────┬────────────────────┬───────────┘
         │                    │
    ┌────▼─────┐         ┌───▼────┐
    │PostgreSQL│         │ Redis  │
    │   DB     │         │ Jobs   │
    └──────────┘         └────────┘
```

---

## 🔧 STACK TECNOLÓGICO

### Backend
- **FastAPI** (Python) - API REST
- **PostgreSQL** - Base de datos relacional
- **SQLAlchemy** - ORM
- **Alembic** - Migraciones
- **Celery** - Background jobs
- **Redis** - Cache y colas
- **JWT** - Autenticación

### Frontend Web
- **React 18** + **TypeScript**
- **Vite** - Build tool
- **Tailwind CSS** - Estilos
- **Zustand** - State management
- **React Query** - Server state
- **React Router** - Navegación

### Mobile
- **React Native** + **TypeScript**
- **Expo** - Toolchain
- **AsyncStorage** - Almacenamiento offline
- **React Navigation** - Navegación

---

## 📊 ESTADO DEL PROYECTO

**Progreso General**: 85% ✅

| Componente | Estado |
|------------|--------|
| Backend API | 🟡 95% (3 bugs menores pendientes) |
| Frontend Web | ✅ 100% (crítico completado) |
| Mobile DVIR | ✅ 100% (optimizado ≤5min) |
| QA Infrastructure | ✅ 100% |
| Testing | 🔄 En progreso |

**Bugs conocidos**: Ver `/docs/agent_logs/BUGS_TRACKER.md`

---

## 🧪 TESTING

### Ejecutar Tests Backend
```bash
cd backend
pytest tests/backend/ -v --cov=app
```

### Linters
```bash
cd backend
flake8 app/     # Estilo de código
mypy app/       # Type checking
bandit -r app/  # Seguridad
```

---

## 🚀 DEPLOYMENT

### Backend
```bash
cd backend
docker-compose up -d  # Producción
```

### Frontend Web
```bash
cd frontend-web
npm run build
# Deploy dist/ a servidor web
```

### Mobile
```bash
cd mobile-app
expo build:android  # APK para Android
expo build:ios      # IPA para iOS
```

---

## 🐛 BUGS CONOCIDOS

Ver archivo completo: `/docs/agent_logs/BUGS_TRACKER.md`

**Resumen**:
- BUG-001: Missing datetime import (MEDIO) - En corrección
- BUG-002: Missing imports coordinador (MEDIO) - En corrección
- BUG-003: Typo en alert.py (BAJO) - En corrección

**Tiempo estimado de corrección**: 30 minutos

---

## 📞 SOPORTE Y CONTACTO

### Documentación del Equipo
- **Agente 1 (Backend)**: `/docs/agent_logs/AGENT_1_BACKEND_LOG.md`
- **Agente 2 (Frontend/Mobile)**: `/docs/agent_logs/AGENT_2_FRONTEND_LOG.md`
- **Agente 3 (QA)**: `/docs/agent_logs/AGENT_3_QA_LOG.md`
- **Agente 4 (Supervisor)**: `/docs/agent_logs/AGENT_4_SUPERVISOR_LOG.md`

### Reportar Problemas
1. Consultar `/docs/agent_logs/BUGS_TRACKER.md`
2. Reportar nuevo bug siguiendo el formato del tracker
3. Asignar severidad: CRÍTICO / ALTO / MEDIO / BAJO

---

## ⚡ COMANDOS ÚTILES

### Backend
```bash
cd backend
docker-compose up -d          # Iniciar servicios
docker-compose down           # Detener servicios
docker-compose logs -f        # Ver logs
docker-compose ps             # Ver estado
docker-compose restart        # Reiniciar
```

### Base de Datos
```bash
# Conectar a PostgreSQL
docker-compose exec postgres psql -U postgres -d fleet_maintenance

# Ver tablas
\dt

# Ver datos
SELECT * FROM usuarios;
SELECT * FROM vehiculos;
```

### Migraciones
```bash
cd backend
docker-compose exec backend alembic revision --autogenerate -m "descripcion"
docker-compose exec backend alembic upgrade head
```

---

## 🎓 CARACTERÍSTICAS DESTACADAS

### 1. DVIR Digital Optimizado ⭐
- ✅ Completable en ≤ 5 minutos
- ✅ Máximo 3 toques por ítem
- ✅ Funciona 100% offline
- ✅ Genera alertas automáticamente si hay defectos críticos
- ✅ Captura fotos y firma digital

### 2. Alertas Inteligentes
- **Predictivas**: Se generan al 90% del intervalo PM
- **Reactivas**: Se crean automáticamente desde DVIR críticos
- **Patrones**: Detecta defectos recurrentes (≥3 veces en 30 días)

### 3. Health Score Automático
- Algoritmo heurístico que calcula score 0-100
- Factores: DVIR (60%), PM compliance (20%), eventos conducción (10%), patrones (10%)
- Se recalcula automáticamente con cada DVIR

### 4. Órdenes de Trabajo Inteligentes
- **Contexto automático**: Historial, patrones, repuestos sugeridos
- **Cronómetro**: Alertas al 20% y 50% de sobretiempo
- **Métricas**: Desviaciones de tiempo/costo calculadas automáticamente

### 5. Offline-First (Mobile)
- App funciona ≥24 horas sin conexión
- AsyncStorage + cola de sincronización
- Auto-sync al recuperar conexión

---

## 📈 MÉTRICAS Y KPIs

El sistema permite tracking de:
- **Cumplimiento PM**: % de vehículos con PM al día
- **MTBF**: Mean Time Between Failures
- **MTTR**: Mean Time To Repair
- **Disponibilidad de Flota**: % vehículos operativos
- **Score de Salud promedio**: Salud general de la flota
- **Tiempo DVIR promedio**: Eficiencia de conductores

---

## 🔐 SEGURIDAD

- ✅ JWT Authentication
- ✅ RBAC (4 roles: Conductor, Coordinador, Técnico, Admin)
- ✅ Passwords hasheados (bcrypt)
- ✅ MFA para Admin (opcional)
- ✅ HTTPS en producción
- ✅ Input validation (Pydantic)
- ✅ SQL injection prevention (SQLAlchemy ORM)

---

## 📄 LICENCIA

[Definir licencia según necesidades del proyecto]

---

## 🙏 CRÉDITOS

**Equipo de Desarrollo**:
- **Agente 1**: Backend Developer (FastAPI, PostgreSQL, Services)
- **Agente 2**: Frontend/Mobile Developer (React, React Native)
- **Agente 3**: QA Engineer & Chief Debugger (Testing, Linters)
- **Agente 4**: Technical Lead & Supervisor (Coordinación, Arquitectura)

**Arquitectura y Blueprint**: Basado en mejores prácticas de RCM (Reliability-Centered Maintenance) y PdM (Predictive Maintenance)

---

**Última actualización**: 2025-11-14  
**Versión**: 1.0.0  
**Estado**: Beta - 85% completado


# 📱 CÓMO REVISAR EL SISTEMA - FLEET MAINTENANCE

**Fecha**: 2025-11-14  
**Sistema**: Fleet Maintenance System para vehículos de transporte

---

## 🚀 INICIO RÁPIDO - UN SOLO CLIC

### Windows
Haz doble clic en: **`MANTENIMIENTO.bat`**

### Linux / Mac
```bash
chmod +x MANTENIMIENTO.sh
./MANTENIMIENTO.sh
```

Esto iniciará automáticamente:
- ✅ PostgreSQL (Base de datos)
- ✅ Redis (Cache/Jobs)
- ✅ Backend API (FastAPI)
- 🌐 Abrirá el navegador en http://localhost:3000

---

## 🌐 CÓMO REVISAR LA APLICACIÓN WEB

### Paso 1: Iniciar Backend (si no lo hiciste con el script)

```bash
cd backend
docker-compose up -d
```

### Paso 2: Iniciar Frontend Web

```bash
cd frontend-web

# Primera vez - instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

El navegador se abrirá automáticamente en: **http://localhost:3000**

### Paso 3: Probar la Aplicación Web

#### **Login**
- **Coordinador**: 
  - Email: `coordinador@test.com`
  - Password: `testpass123`
- **Admin**: 
  - Email: `admin@test.com`
  - Password: `admin123`

#### **Páginas disponibles**:
1. **Dashboard** (`/dashboard`)
   - Vista general de flota
   - KPIs principales
   - Alertas activas

2. **Alertas** (`/alerts`)
   - Alertas predictivas (PM próximas)
   - Alertas reactivas (defectos críticos)
   - Patrones recurrentes

3. **Vehículos** (`/vehicles`)
   - Lista de vehículos
   - Detalle con contexto completo
   - Score de salud

4. **Órdenes de Trabajo** (`/work-orders`)
   - Lista de OT
   - Crear nueva OT
   - Seguimiento de estados

5. **Administración** (`/admin`)
   - Usuarios
   - Vehículos
   - Checklists
   - Configuración PM

---

## 📱 CÓMO REVISAR LA APP MÓVIL (React Native)

### Opción 1: Expo Go (MÁS FÁCIL - Recomendado)

#### Paso 1: Instalar Expo Go en tu teléfono
- **Android**: [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)
- **iOS**: [App Store](https://apps.apple.com/app/expo-go/id982107779)

#### Paso 2: Iniciar el proyecto
```bash
cd mobile-app

# Primera vez - instalar dependencias
npm install

# Iniciar Expo
npm start
```

#### Paso 3: Escanear QR
1. Se abrirá una página web con un **código QR**
2. **Android**: Abre Expo Go → "Scan QR Code" → Escanea
3. **iOS**: Abre la Cámara → Escanea el QR → Toca la notificación

#### Paso 4: Probar la App
**Login Conductor**:
- Email: `conductor@test.com`
- Password: `testpass123`

**Flujos disponibles**:
- ✅ Login
- ✅ Selección de vehículo
- ✅ **DVIR Screen completa** (el componente más crítico)
  - Checklist por categorías
  - Fotos para defectos
  - Firma digital
  - GPS automático
  - **Optimizado para ≤5 minutos**

---

### Opción 2: Simulador/Emulador (Desarrollo)

#### Android Emulator
```bash
cd mobile-app

# Iniciar en Android
npm run android
```

Requiere:
- Android Studio instalado
- Un emulador de Android configurado

#### iOS Simulator (Solo Mac)
```bash
cd mobile-app

# Iniciar en iOS
npm run ios
```

Requiere:
- Xcode instalado (solo Mac)
- Simulador de iOS configurado

---

## 🧪 CÓMO PROBAR FUNCIONALIDADES CLAVE

### 1. DVIR Digital (CRÍTICO ⭐⭐⭐)

**App Móvil → Conductor**

1. Login como conductor
2. Seleccionar vehículo (ej. "Toyota Hilux TEST123")
3. Ver **Score de Salud** del vehículo
4. Tap en "Iniciar DVIR"
5. Completar checklist:
   - Marcar ítems como OK / ALERTA / CRÍTICO
   - Si marcas CRÍTICO → pide foto + comentario
   - Progreso visual en tiempo real
6. Ingresar odómetro
7. Firmar digitalmente
8. Enviar

**Resultado esperado**:
- ⏱️ Tiempo de completado: < 5 minutos
- ✅ Si hay ítems CRÍTICOS:
  - Vehículo cambia a "NO OPERATIVO"
  - Se crea alerta reactiva
  - Se crea OT correctiva urgente
- 📊 Score de Salud se recalcula

**Cómo verificar en Web**:
- Dashboard → Ver alerta nueva
- Vehículos → Ver estado del vehículo
- Órdenes de Trabajo → Ver OT creada

---

### 2. Gestión de Alertas

**App Web → Coordinador**

1. Login como coordinador
2. Ir a **Dashboard**
3. Ver 3 paneles:
   - **Panel A**: Alertas Predictivas (PM próximas)
   - **Panel B**: Alertas Reactivas (defectos HOY)
   - **Panel C**: Patrones Recurrentes

4. Click en una alerta
5. Ver **contexto del vehículo**:
   - Score de salud
   - Historial DVIR
   - Próximo PM
   - Defectos recientes
   - Uso (normal/severo)

6. Acciones:
   - Crear OT desde alerta
   - Marcar como atendida
   - Agregar a monitoreo

---

### 3. Creación y Gestión de OT

**App Web → Coordinador**

1. Ir a **Órdenes de Trabajo**
2. Click "Nueva OT"
3. Seleccionar:
   - Vehículo
   - Tipo (Preventivo/Correctivo/Diagnóstico)
   - Prioridad
   - Técnico asignado
4. El sistema automáticamente sugiere:
   - Duración estimada (basado en histórico)
   - Repuestos probables
   - Técnico recomendado

5. Crear OT

**App Móvil → Técnico**

1. Login como técnico
2. Ver lista de OT asignadas
3. Abrir OT
4. Ver contexto del vehículo
5. Iniciar trabajo (cronómetro arranca)
6. Completar tareas
7. Registrar repuestos usados
8. Cerrar OT

**Resultado esperado**:
- ⏱️ Alertas si excede 20% o 50% del tiempo estimado
- 📊 Métricas de eficiencia calculadas
- ✅ Vehículo vuelve a OPERATIVO

---

### 4. Modo Offline (Mobile)

**Importante**: Este es un requisito crítico del sistema

1. **En la app móvil**:
   - Abre la app
   - Inicia un DVIR
   - **Activa Modo Avión** en tu teléfono
   - Completa el DVIR normalmente
   - Enviar → Se guarda localmente

2. **Verificar cola de sincronización**:
   - App muestra "📴 Modo Offline"
   - DVIR queda en "Pendiente de sincronización"

3. **Recuperar conexión**:
   - Desactiva Modo Avión
   - App detecta conexión
   - **Auto-sincroniza** en background
   - Muestra "✅ Sincronizado"

**Requisito**: Debe funcionar offline por ≥24 horas

---

## 🔍 CÓMO VERIFICAR QUE TODO FUNCIONA

### Backend API

#### Método 1: Swagger UI (Recomendado)
1. Abrir: http://localhost:8000/api/docs
2. Ver todos los endpoints documentados
3. Probar endpoints directamente desde el navegador
4. Ver requests/responses en tiempo real

#### Método 2: Verificar servicios
```bash
cd backend

# Ver logs
docker-compose logs -f

# Ver estado de servicios
docker-compose ps

# Verificar PostgreSQL
docker-compose exec postgres psql -U postgres -d fleet_maintenance -c "\dt"

# Verificar Redis
docker-compose exec redis redis-cli ping
```

### Base de Datos

```bash
cd backend

# Conectar a PostgreSQL
docker-compose exec postgres psql -U postgres -d fleet_maintenance

# Ver tablas
\dt

# Ver usuarios de prueba
SELECT id, nombre, email, rol FROM usuarios;

# Ver vehículos de prueba
SELECT id, placa, modelo, estado_operativo FROM vehiculos;

# Salir
\q
```

### Frontend Web

```bash
cd frontend-web

# Ver errores en consola
npm run dev

# Build de producción (verificar que compila)
npm run build
```

### Mobile

```bash
cd mobile-app

# Ver logs
npm start

# Verificar TypeScript
npx tsc --noEmit

# Linter
npm run lint
```

---

## 🧪 CÓMO EJECUTAR TESTS (QA)

### Backend Tests

```bash
cd backend

# Ejecutar TODOS los tests
pytest tests/backend/ -v

# Solo tests unitarios
pytest tests/backend/unit/ -v

# Solo tests de integración
pytest tests/backend/integration/ -v

# Con coverage
pytest tests/backend/ --cov=app --cov-report=html

# Ver reporte HTML de coverage
# Abrir: htmlcov/index.html
```

### Linters

```bash
cd backend

# Flake8 (estilo de código)
flake8 app/

# Mypy (type checking)
mypy app/

# Bandit (seguridad)
bandit -r app/
```

---

## 📊 USUARIOS DE PRUEBA

El sistema viene con usuarios pre-configurados para testing:

| Rol | Email | Password | Acceso |
|-----|-------|----------|--------|
| **Conductor** | conductor@test.com | testpass123 | Mobile + Web |
| **Coordinador** | coordinador@test.com | testpass123 | Web |
| **Técnico** | tecnico@test.com | testpass123 | Mobile + Web |
| **Admin** | admin@test.com | admin123 | Web |

### Vehículos de Prueba

| Placa | Tipo | Modelo | Estado |
|-------|------|--------|--------|
| TEST123 | PICKUP | Toyota Hilux 4x4 | OPERATIVO |
| TURBO456 | TURBO | Ford Ranger Turbo | OPERATIVO |

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### "No se puede conectar al backend"
```bash
# Verificar que Docker esté corriendo
docker ps

# Reiniciar servicios
cd backend
docker-compose restart

# Ver logs de errores
docker-compose logs backend
```

### "Frontend no carga"
```bash
cd frontend-web

# Limpiar node_modules
rm -rf node_modules package-lock.json
npm install

# Reiniciar servidor
npm run dev
```

### "App móvil no conecta"
1. Verificar que estés en la misma red WiFi (PC y teléfono)
2. En `mobile-app/app.json`, verificar que la IP sea correcta
3. Verificar firewall no bloquee el puerto 8000

### "Base de datos vacía"
```bash
cd backend

# Ejecutar seed data
docker-compose exec backend python -m app.db.init_db

# O crear datos manualmente desde Swagger UI
```

---

## 📱 URLS IMPORTANTES

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **Frontend Web** | http://localhost:3000 | Aplicación web React |
| **Backend API** | http://localhost:8000 | API FastAPI |
| **API Docs (Swagger)** | http://localhost:8000/api/docs | Documentación interactiva API |
| **ReDoc** | http://localhost:8000/api/redoc | Documentación alternativa |
| **PostgreSQL** | localhost:5432 | Base de datos |
| **Redis** | localhost:6379 | Cache y jobs |

---

## 🎯 FLUJOS CRÍTICOS A PROBAR

### ⭐ PRIORIDAD MÁXIMA

1. **DVIR Conductor** (Mobile)
   - Tiempo: ≤ 5 minutos
   - Funciona offline
   - Genera alertas si hay defectos críticos

2. **Dashboard Coordinador** (Web)
   - Muestra alertas en tiempo real
   - Permite crear OT desde alertas

3. **Gestión OT Técnico** (Mobile + Web)
   - Actualiza estados
   - Registra repuestos
   - Cronómetro funciona

### ⭐ PRIORIDAD ALTA

4. **Offline Sync** (Mobile)
   - DVIR funciona sin conexión
   - Se sincroniza automáticamente

5. **Health Score** (Backend)
   - Se calcula automáticamente
   - Se actualiza con cada DVIR

6. **Alertas Predictivas** (Backend)
   - Se generan al 90% del PM
   - Aparecen en dashboard

---

## 📞 SOPORTE

Si encuentras problemas:

1. **Revisar logs**:
   ```bash
   cd backend && docker-compose logs -f
   ```

2. **Ver BUGS_TRACKER.md**:
   - Bugs conocidos están documentados
   - Soluciones propuestas incluidas

3. **Consultar con Agente 4 (Supervisor)**:
   - Todos los problemas deben reportarse
   - Se documentarán y resolverán

---

## ✅ CHECKLIST DE REVISIÓN

### Backend
- [ ] Docker services corriendo (postgres, redis, backend)
- [ ] API responde en http://localhost:8000
- [ ] Swagger UI carga http://localhost:8000/api/docs
- [ ] Base de datos tiene tablas creadas
- [ ] Usuarios de prueba existen

### Frontend Web
- [ ] Servidor dev corre en http://localhost:3000
- [ ] Login funciona
- [ ] Dashboard carga
- [ ] Navegación funciona

### Mobile
- [ ] Expo inicia sin errores
- [ ] App carga en teléfono/emulador
- [ ] Login funciona
- [ ] DVIR screen completo está accesible
- [ ] Modo offline funciona

### Testing
- [ ] Tests backend pasan (pytest)
- [ ] Linters pasan (flake8, mypy)
- [ ] TypeScript compila sin errores

---

**Documento preparado por**: Agente 4 - Technical Lead & Supervisor  
**Fecha**: 2025-11-14  
**Versión**: 1.0


# 🧪 CÓMO PROBAR LA APLICACIÓN - GUÍA COMPLETA

**Estado**: ✅ App lista y funcionando

---

## 🌐 URLs

- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/api/docs

---

## 🔑 USUARIOS DE PRUEBA

| Email | Password | Rol | Qué verá |
|-------|----------|-----|----------|
| coordinador@test.com | testpass123 | COORDINADOR | Dashboard, Alertas, Vehículos, OT |
| conductor@test.com | testpass123 | CONDUCTOR | DVIR, Mis Vehículos, Reportar |
| tecnico@test.com | testpass123 | TÉCNICO | Mis Órdenes, Inventario |
| admin@test.com | testpass123 | ADMIN | Dashboard Admin, Usuarios, Config |

---

## 🧪 PRUEBAS POR ROL

### 1️⃣ Probar COORDINADOR

1. Abre: http://localhost:3000
2. Login: `coordinador@test.com` / `testpass123`
3. **Verifica**:
   - ✅ Redirige automáticamente a `/dashboard`
   - ✅ Menú muestra: Dashboard, Alertas, Vehículos, Órdenes de Trabajo
   - ✅ Arriba derecha dice: "María González (COORDINADOR)"
4. **Navega a cada página**:
   - Clic en "Alertas" → Debe mostrar 3 tipos de alertas
   - Clic en "Vehículos" → Debe mostrar buscador
   - Clic en "Órdenes de Trabajo" → Debe mostrar botón "Nueva OT"
5. **Prueba restricción**:
   - Pega en URL: `http://localhost:3000/conductor/dvir`
   - ✅ Debe redirigir a `/dashboard` automáticamente

---

### 2️⃣ Probar CONDUCTOR

1. Haz clic en "Salir" (arriba derecha)
2. Login: `conductor@test.com` / `testpass123`
3. **Verifica**:
   - ✅ Redirige automáticamente a `/conductor/dvir`
   - ✅ Menú muestra SOLO: DVIR, Mis Vehículos, Reportar Defecto
   - ✅ NO ve opciones de coordinador
   - ✅ Arriba derecha dice: "Juan Pérez (CONDUCTOR)"
4. **Navega a cada página**:
   - Clic en "DVIR" → Debe mostrar formulario de inspección
   - Clic en "Mis Vehículos" → Debe mostrar vehículo TEST123
   - Clic en "Reportar Defecto" → Debe mostrar formulario de reporte
5. **Prueba restricción**:
   - Pega en URL: `http://localhost:3000/dashboard`
   - ✅ Debe redirigir a `/conductor/dvir` automáticamente

---

### 3️⃣ Probar TÉCNICO

1. Haz clic en "Salir"
2. Login: `tecnico@test.com` / `testpass123`
3. **Verifica**:
   - ✅ Redirige automáticamente a `/tecnico/ordenes`
   - ✅ Menú muestra SOLO: Mis Órdenes, Inventario
   - ✅ Arriba derecha dice: "Carlos Méndez (TÉCNICO)"
4. **Navega a cada página**:
   - Clic en "Mis Órdenes" → Debe mostrar OT-001 pendiente
   - Clic en "Inventario" → Debe mostrar tabla de repuestos
5. **Prueba restricción**:
   - Pega en URL: `http://localhost:3000/dashboard`
   - ✅ Debe redirigir a `/tecnico/ordenes` automáticamente

---

### 4️⃣ Probar ADMIN

1. Haz clic en "Salir"
2. Login: `admin@test.com` / `testpass123`
3. **Verifica**:
   - ✅ Redirige automáticamente a `/admin/dashboard`
   - ✅ Menú muestra: Dashboard, Usuarios, Configuración
   - ✅ Arriba derecha dice: "Admin User (ADMIN)"
4. **Navega a cada página**:
   - Clic en "Dashboard" → Debe mostrar KPIs (24 usuarios, 50 vehículos, etc)
   - Clic en "Usuarios" → Debe mostrar tabla con todos los usuarios
   - Clic en "Configuración" → Debe mostrar checklists y políticas PM
5. **Prueba permiso especial**:
   - Pega en URL: `http://localhost:3000/dashboard`
   - ✅ Admin SÍ puede acceder (permiso especial)

---

## ✅ CHECKLIST DE VALIDACIÓN

Marca cada ítem después de probarlo:

- [ ] Backend responde en http://localhost:8000
- [ ] Frontend carga en http://localhost:3000
- [ ] Coordinador ve 4 opciones de menú
- [ ] Conductor ve 3 opciones de menú
- [ ] Técnico ve 2 opciones de menú
- [ ] Admin ve 3 opciones de menú
- [ ] Cada rol redirige a su página por defecto
- [ ] Redirecciones de seguridad funcionan
- [ ] Navegación entre páginas funciona
- [ ] Botón "Salir" funciona
- [ ] No hay errores en consola del navegador (F12)

---

## 🐛 SI ALGO NO FUNCIONA

### Frontend no carga:
```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\man\frontend-web"
npm run dev
```

### Backend no responde:
```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man\man\backend"
docker-compose up -d
```

### Login da error:
- Verifica que usas las credenciales correctas
- Verifica que backend responde en http://localhost:8000/health

---

## 📊 RESULTADO ESPERADO

**Cada rol ve una interfaz completamente diferente:**

- **COORDINADOR**: Dashboard ejecutivo con KPIs y gestión de flota
- **CONDUCTOR**: Herramientas de inspección y reporte
- **TÉCNICO**: Órdenes de trabajo asignadas e inventario
- **ADMIN**: Panel administrativo con gestión de usuarios

**Todos los placeholders indican "🚧 En desarrollo"** - Esto es correcto, la funcionalidad completa se implementará después.

---

## ✅ ESTADO: LISTO PARA USAR

**Puedes proceder con:**
- ✅ Pruebas funcionales
- ✅ Demostración a stakeholders
- ✅ Desarrollo de funcionalidades adicionales
- ✅ Integración con backend real

---

**¡La aplicación está funcionando correctamente con control de acceso por roles!** 🚀


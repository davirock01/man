# Agente 2 - Pruebas Funcionales

## Test COORDINADOR

### Login
- Email: coordinador@test.com
- Password: testpass123
- Hora: [Usuario debe probar]

### Verificaciones:
- [ ] Al hacer login, ¿redirige automáticamente a /dashboard?
- [ ] ¿El menú muestra: Dashboard, Alertas, Vehículos, Órdenes de Trabajo?
- [ ] ¿Puedes hacer clic en "Alertas" y ve la página con 3 secciones?
- [ ] ¿Puedes hacer clic en "Vehículos" y ve el buscador?
- [ ] ¿Puedes hacer clic en "Órdenes de Trabajo" y ve el botón "Nueva OT"?
- [ ] Si pegas en la URL: http://localhost:3000/conductor/dvir ¿Redirige a /dashboard?

---

## Test CONDUCTOR

### Login
- Logout primero (botón Salir)
- Email: conductor@test.com
- Password: testpass123

### Verificaciones:
- [ ] Al hacer login, ¿redirige automáticamente a /conductor/dvir?
- [ ] ¿El menú muestra SOLO: DVIR, Mis Vehículos, Reportar Defecto?
- [ ] ¿NO ve opciones de coordinador (Dashboard, Alertas, etc)?
- [ ] ¿Puedes hacer clic en "DVIR" y ve el formulario con checklist?
- [ ] ¿Puedes hacer clic en "Mis Vehículos" y ve la tarjeta del vehículo TEST123?
- [ ] ¿Puedes hacer clic en "Reportar Defecto" y ve el formulario?
- [ ] Si pegas en la URL: http://localhost:3000/dashboard ¿Redirige a /conductor/dvir?

---

## INSTRUCCIONES PARA USUARIO

Por favor prueba lo siguiente en http://localhost:3000:

1. **Logout** si estás conectado
2. **Login** como coordinador@test.com / testpass123
3. Verifica el menú y navega a cada página
4. **Logout** 
5. **Login** como conductor@test.com / testpass123
6. Verifica que ves un menú diferente
7. Intenta acceder a /dashboard manualmente (debe redirigir)

**Reporta**: ¿Funciona correctamente? ¿Qué problemas ves?


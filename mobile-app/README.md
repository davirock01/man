# Fleet Maintenance System - Mobile App

App móvil React Native con Expo para conductores y técnicos.

## Features

- ✅ Autenticación JWT
- ✅ DVIR digital con checklist configurable
- ✅ Soporte offline con cola de sincronización
- ✅ Gestión de órdenes de trabajo (técnicos)
- ✅ Detección automática de conexión
- ✅ Sincronización automática al recuperar conexión

## Setup

### 1. Instalar dependencias

```bash
npm install
```

### 2. Iniciar Expo

```bash
npm start
```

### 3. Ejecutar en dispositivo

- Escanear QR code con Expo Go app (iOS/Android)
- O presionar 'a' para Android emulator
- O presionar 'i' para iOS simulator

## Estructura

```
src/
├── navigation/       # React Navigation setup
├── screens/          # Pantallas por rol
│   ├── conductor/    # DVIR, fin jornada
│   ├── tecnico/      # OT management
│   └── common/       # Sync, login
├── services/         # API y offline services
│   ├── api.ts
│   └── offline/
│       ├── storage.ts
│       └── syncQueue.ts
└── components/       # Componentes reutilizables
```

## Roles Soportados

### CONDUCTOR
- Login
- Ver vehículos asignados
- Realizar DVIR preoperativo
- Reportar defectos
- Fin de jornada
- Sincronización offline

### TECNICO
- Login
- Ver órdenes de trabajo asignadas
- Iniciar/pausar/completar OT
- Registrar repuestos usados
- Reportar defectos inesperados
- Sincronización offline

## Modo Offline

La app funciona completamente offline:

1. **Detección automática**: NetInfo detecta cambios de conexión
2. **Cola de sincronización**: AsyncStorage guarda operaciones pendientes
3. **Sincronización automática**: Al recuperar conexión, sincroniza automáticamente
4. **UI feedback**: Indicadores visuales de modo offline

### Datos guardados offline:
- DVIRs completos
- Reportes de defectos
- Actualizaciones de OT
- Eventos de conducción

## Tecnologías

- React Native con Expo
- TypeScript
- React Navigation (Stack + Tabs)
- React Native Paper (UI components)
- AsyncStorage (offline storage)
- TanStack Query (server state)
- Axios (HTTP client)
- NetInfo (network detection)

## Configuración API

Editar `src/services/api.ts`:

```typescript
const API_BASE_URL = 'https://your-api.com/api/v1';
```

## Build para Producción

### Android APK
```bash
expo build:android
```

### iOS IPA
```bash
expo build:ios
```

## TODO V2

- [ ] Captura de fotos con cámara
- [ ] Firma digital canvas
- [ ] Push notifications
- [ ] Geolocalización en background
- [ ] Biometric authentication
- [ ] Dark mode


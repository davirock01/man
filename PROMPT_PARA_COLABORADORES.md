# 🎯 PROMPT PARA COLABORADORES

## 📋 COPIA Y PEGA ESTE PROMPT EN TU LLM

---

```
Hola, necesito tu ayuda para configurar un proyecto colaborativo de mantenimiento de flota vehicular.

# CONTEXTO DEL PROYECTO

Soy parte de un equipo internacional trabajando en un sistema de gestión de mantenimiento vehicular. El proyecto ya está en GitHub y necesito configurar mi entorno local para colaborar efectivamente.

## INFORMACIÓN DEL REPOSITORIO

**URL del Repositorio**: https://github.com/davirock01/man

**Stack Tecnológico**:
- Backend: FastAPI (Python), PostgreSQL, Celery, Redis
- Frontend Web: React 18 + TypeScript, Vite, Tailwind CSS
- Mobile App: React Native + Expo

**Estructura del Proyecto**:
```
man/
├── backend/              # API FastAPI
├── frontend-web/         # Aplicación web React
├── mobile-app/          # App móvil React Native
├── docs/                # Documentación
└── [otros archivos de config y scripts]
```

## LO QUE NECESITO QUE ME AYUDES A HACER

### 1. CONFIGURACIÓN INICIAL

Por favor, ayúdame a:

a) **Clonar el repositorio** en mi computadora de forma correcta
b) **Verificar requisitos del sistema** (Python, Node.js, Docker, PostgreSQL, etc.)
c) **Instalar todas las dependencias** necesarias para:
   - Backend (Python/FastAPI)
   - Frontend Web (React/TypeScript)
   - Mobile App (React Native/Expo)
d) **Configurar variables de entorno** (.env files)
e) **Configurar la base de datos** (PostgreSQL)
f) **Iniciar todos los servicios** y verificar que funcionen

### 2. FLUJO DE TRABAJO GIT

Enséñame y configura:

a) **Comandos diarios** que debo usar para:
   - Descargar cambios del equipo (antes de trabajar)
   - Subir mis cambios (después de trabajar)
   - Ver el estado de mis cambios
   - Hacer commits descriptivos

b) **Manejo de conflictos**: Qué hacer si hay conflictos de merge

c) **Mejores prácticas**: Convenciones de commits, branches, etc.

### 3. DESARROLLO LOCAL

Ayúdame a:

a) **Ejecutar el backend** localmente y probar los endpoints
b) **Ejecutar el frontend web** y acceder a la interfaz
c) **Ejecutar la app móvil** en el emulador o mi dispositivo
d) **Configurar hot-reload** para desarrollo eficiente
e) **Acceder a la documentación de la API** (Swagger/OpenAPI)

### 4. TESTING Y DEBUGGING

Configura:

a) **Cómo ejecutar tests** (backend y frontend)
b) **Cómo ver logs** de los servicios
c) **Herramientas de debugging** recomendadas
d) **Linters y formatters** para mantener calidad de código

### 5. BASE DE DATOS

Ayúdame a:

a) **Conectar a PostgreSQL** localmente
b) **Ejecutar migraciones** (Alembic)
c) **Seed data** si es necesario para desarrollo
d) **Ver y modificar datos** de prueba

## REQUISITOS IMPORTANTES

- **Acceso Total**: Necesito poder leer, escribir, modificar y eliminar archivos
- **Sincronización en Tiempo Real**: Los cambios entre el equipo deben verse rápidamente
- **Offline First** (Mobile): La app móvil debe funcionar sin conexión
- **Documentación**: Explícame cada paso que hagamos

## CREDENCIALES Y CONFIGURACIÓN SENSIBLE

**CREDENCIALES COMPLETAS DEL PROYECTO** (Acceso total confiado):

**IMPORTANTE**: 
- El administrador te enviará un archivo llamado `CREDENCIALES_PARA_COMPARTIR.txt`
- Ese archivo contiene TODAS las credenciales necesarias (API keys, base de datos, JWT secrets)
- Copia EXACTAMENTE el contenido de ese archivo en un nuevo archivo llamado `.env` en la raíz del proyecto
- El archivo `.env` debe estar en la raíz del proyecto
- Estas credenciales te dan acceso total al sistema

**Estructura del archivo .env necesario**:
```env
DATABASE_URL=postgresql://...
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=...
POSTGRES_DB=fleet_maintenance
POSTGRES_PORT=5432

SECRET_KEY=...
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=...

OPENAI_API_KEY=sk-proj-...
CLAUDE_API_KEY=sk-ant-...
GEMINI_API_KEY=...

REDIS_URL=redis://localhost:6379/0
BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
# ... más configuraciones
```

**Solicita el archivo `CREDENCIALES_PARA_COMPARTIR.txt` al administrador si no lo has recibido.**

## MI SISTEMA OPERATIVO

[COMPLETAR AQUÍ TU SISTEMA]:
- Windows 11 / Windows 10 / macOS / Linux
- Versión de Python instalada: [si sabes]
- Versión de Node.js instalada: [si sabes]
- Docker instalado: Sí / No / No sé

## LO QUE ESPERO DE TI

Por favor:

1. **Guíame paso a paso** con comandos exactos que pueda copiar y pegar
2. **Crea scripts** si es necesario para automatizar tareas comunes
3. **Explica qué hace cada comando** para que aprenda
4. **Anticipa problemas comunes** y dame soluciones
5. **Verifica que todo funcione** antes de continuar al siguiente paso
6. **Dame un checklist** al final para confirmar que todo está configurado

## PREGUNTA INICIAL

¿Qué sistema operativo estás usando? (Windows / macOS / Linux)
```

---

## 📝 INSTRUCCIONES DE USO

### Para ti (Administrador):

1. **Copia** todo el contenido del prompt de arriba (desde "Hola, necesito tu ayuda..." hasta el final)

2. **Envía** este prompt a tus colaboradores por:
   - Email
   - Slack/Discord
   - WhatsApp/Signal
   - Cualquier canal de comunicación

3. **Ellos deben**:
   - Abrir Cursor (o su IDE con LLM)
   - Pegar el prompt completo
   - Seguir las instrucciones que el LLM les dé

4. **Tú debes compartir** (por canal seguro):
   - API keys (OpenAI, Claude, etc.)
   - Credenciales de base de datos
   - JWT secrets
   - Cualquier otra configuración sensible

   ⚠️ **NUNCA por GitHub, siempre por Signal/WhatsApp encriptado**

---

## 🔑 CREDENCIALES QUE NECESITARÁS COMPARTIR

Prepara esta información para enviarla **de forma segura** (NO por GitHub):

```env
# Base de datos
DATABASE_URL=postgresql://usuario:password@host:5432/fleet_maintenance
DB_USER=postgres
DB_PASSWORD=[TU_PASSWORD]
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fleet_maintenance

# API Keys
OPENAI_API_KEY=sk-proj-[TU_KEY]
CLAUDE_API_KEY=sk-ant-[TU_KEY]

# Seguridad
SECRET_KEY=[TU_SECRET_KEY]
JWT_SECRET_KEY=[TU_JWT_SECRET]
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# URLs
BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
```

**Envía esto por**: Signal, WhatsApp, o mensaje encriptado (ver `COMPARTIR_CREDENCIALES_SEGURO.md`)

---

## ✅ VENTAJAS DE ESTE PROMPT

✅ **Auto-contenido**: Tiene toda la información necesaria
✅ **Guía al LLM**: El LLM sabrá exactamente qué hacer
✅ **Paso a paso**: Configuración ordenada y lógica
✅ **Completo**: Cubre setup, desarrollo, testing, y flujo de trabajo
✅ **Educativo**: Explica el "por qué" de cada cosa
✅ **Profesional**: Sigue mejores prácticas

---

## 🎯 RESULTADO ESPERADO

Después de usar este prompt, tu colaborador tendrá:

✅ Repositorio clonado
✅ Todas las dependencias instaladas
✅ Base de datos configurada
✅ Servicios corriendo localmente
✅ Entendimiento del flujo de trabajo Git
✅ Scripts para tareas comunes
✅ Acceso total al proyecto
✅ Capacidad de colaborar efectivamente

---

## 📞 SOPORTE

Si tu colaborador tiene problemas:

1. Primero, que revise la documentación en `/docs`
2. Que consulte `COMO_REVISAR_EL_SISTEMA.md`
3. Que te contacte directamente
4. Que reporte bugs en GitHub Issues

---

## 🔄 FLUJO DE TRABAJO DIARIO

Una vez configurado, el flujo será:

**Antes de trabajar**:
```bash
git pull origin main
```

**Después de trabajar**:
```bash
git add .
git commit -m "Descripción clara de cambios"
git push origin main
```

**Para ver cambios**:
```bash
git status
git log --oneline -10
```

---

## 🎉 ¡LISTO!

Este prompt es todo lo que necesitan tus colaboradores para empezar.

**Simplemente**:
1. Compárteles este prompt
2. Compárteles las credenciales (por canal seguro)
3. Ellos lo pegan en su LLM
4. El LLM les ayudará con todo

**¡Eso es todo! 🚀**
```


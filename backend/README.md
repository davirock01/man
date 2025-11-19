# Fleet Maintenance System - Backend

Sistema de mantenimiento vehicular para flotas de transporte especial.

## Stack Tecnológico

- **Framework**: FastAPI
- **Base de datos**: PostgreSQL
- **ORM**: SQLAlchemy (async)
- **Autenticación**: JWT + MFA
- **Cache/Events**: Redis
- **Migraciones**: Alembic

## Estructura del Proyecto

```
backend/
├── app/
│   ├── api/v1/          # API endpoints
│   ├── core/            # Configuración y seguridad
│   ├── models/          # Modelos SQLAlchemy
│   ├── schemas/         # Esquemas Pydantic
│   ├── services/        # Lógica de negocio
│   ├── jobs/            # Tareas programadas
│   └── utils/           # Utilidades
├── alembic/             # Migraciones de BD
├── tests/               # Tests
└── docker-compose.yml   # Orquestación
```

## Instalación y Ejecución

### Con Docker (Recomendado)

```bash
# Copiar archivo de configuración
cp .env.example .env

# Editar .env con tus configuraciones
nano .env

# Levantar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f backend

# Ejecutar migraciones
docker-compose exec backend alembic upgrade head
```

### Sin Docker

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

## API Documentation

Una vez iniciado el servidor, la documentación interactiva está disponible en:

- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## Migraciones de Base de Datos

```bash
# Crear una nueva migración
alembic revision --autogenerate -m "descripción del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Ver historial
alembic history
```

## Testing

```bash
# Ejecutar todos los tests
pytest

# Con cobertura
pytest --cov=app tests/

# Tests específicos
pytest tests/unit/
pytest tests/integration/
```

## Módulos Principales

### Auth & Usuarios
- Autenticación JWT con refresh tokens
- RBAC: Conductor, Coordinador, Técnico, Admin
- MFA para administradores

### DVIR (Driver Vehicle Inspection Report)
- Checklist preoperativo digital
- Captura de fotos y firma
- Modo offline con sincronización

### Mantenimiento Predictivo
- Alertas basadas en km/tiempo
- Detección de patrones recurrentes
- Score de salud del vehículo

### Órdenes de Trabajo
- Creación automática desde alertas
- Cronómetro con alertas de sobretiempo
- Gestión de repuestos e inventario

## Variables de Entorno

Ver `.env.example` para la lista completa de variables configurables.

## Arquitectura

El sistema sigue una arquitectura modular basada en dominios:

1. **API Layer**: Endpoints REST organizados por rol
2. **Service Layer**: Lógica de negocio
3. **Data Layer**: Modelos y acceso a BD
4. **Event Layer**: Eventos asíncronos con Redis

## Contacto y Soporte

Para más información, consultar la documentación completa del proyecto.



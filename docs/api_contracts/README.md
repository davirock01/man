# API Contracts - Fleet Maintenance System

Esta carpeta contiene los contratos de API detallados para comunicación entre Frontend y Backend.

## Estructura

```
api_contracts/
├── auth_endpoints.md          # Login, logout, refresh
├── conductor_endpoints.md     # DVIR, reportes, sync
├── coordinador_endpoints.md   # Dashboard, alertas, OT
├── tecnico_endpoints.md       # OT management, inventario
└── admin_endpoints.md         # CRUD usuarios, vehículos, config
```

## Convenciones

Todos los endpoints siguen este formato:

```markdown
### [MÉTODO] /ruta/del/endpoint

**Descripción**: [Qué hace]

**Auth Required**: ✅/❌

**Roles permitidos**: CONDUCTOR, COORDINADOR, TECNICO, ADMIN

**Request Headers**:
```json
{
  "Authorization": "Bearer <access_token>",
  "Content-Type": "application/json"
}
```

**Request Body** (si aplica):
```json
{
  "campo": "valor"
}
```

**Response 200 Success**:
```json
{
  "data": {}
}
```

**Response 4xx/5xx Errors**:
```json
{
  "detail": "Mensaje de error"
}
```

**Ejemplos**:
```bash
curl -X GET http://localhost:8000/api/v1/endpoint \
  -H "Authorization: Bearer token"
```
```

## Base URL

- **Development**: `http://localhost:8000/api/v1`
- **Production**: `https://api.fleetmaintenance.com/api/v1`

## Autenticación

Todos los endpoints (excepto `/auth/login`) requieren JWT token en header:

```
Authorization: Bearer <access_token>
```

Tokens expires:
- Access: 30 minutos
- Refresh: 7 días

## Status Codes

- `200 OK`: Operación exitosa
- `201 Created`: Recurso creado
- `204 No Content`: Operación exitosa sin contenido
- `400 Bad Request`: Datos inválidos
- `401 Unauthorized`: No autenticado o token expirado
- `403 Forbidden`: No tiene permisos para este recurso
- `404 Not Found`: Recurso no existe
- `422 Unprocessable Entity`: Validación fallida
- `500 Internal Server Error`: Error del servidor

## Paginación

Endpoints de listado soportan paginación:

```
GET /endpoint?limit=50&offset=0
```

Response incluye metadata:
```json
{
  "items": [...],
  "total": 150,
  "limit": 50,
  "offset": 0
}
```

## Filtering

Muchos endpoints soportan filtros query params:

```
GET /alertas?estado=PENDIENTE&criticidad=ALTA
```

## OpenAPI/Swagger

Documentación interactiva disponible en:
- `http://localhost:8000/docs` (Swagger UI)
- `http://localhost:8000/redoc` (ReDoc)

---

Ver archivos individuales para detalles de cada módulo.


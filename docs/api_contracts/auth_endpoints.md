# Auth Endpoints

Base path: `/api/v1/auth`

---

## POST /auth/login

**Descripción**: Autenticar usuario y obtener tokens JWT

**Auth Required**: ❌

**Request Body**:
```json
{
  "email": "conductor@example.com",
  "password": "password123"
}
```

**Response 200 Success**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "conductor@example.com",
    "nombre": "Juan Pérez",
    "rol": "CONDUCTOR",
    "estado": "ACTIVO",
    "telefono": "+57 300 1234567"
  }
}
```

**Response 401 Unauthorized**:
```json
{
  "detail": "Email o contraseña incorrectos"
}
```

**Response 403 Forbidden**:
```json
{
  "detail": "Usuario inactivo"
}
```

**Ejemplo curl**:
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "conductor@example.com", "password": "password123"}'
```

---

## POST /auth/refresh

**Descripción**: Renovar access token usando refresh token

**Auth Required**: ❌ (usa refresh token)

**Request Body**:
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response 200 Success**:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Response 401 Unauthorized**:
```json
{
  "detail": "Token de actualización inválido"
}
```

---

## POST /auth/logout

**Descripción**: Cerrar sesión (cliente debe descartar tokens)

**Auth Required**: ✅

**Request Headers**:
```
Authorization: Bearer <access_token>
```

**Response 204 No Content**: (sin body)

**Ejemplo curl**:
```bash
curl -X POST http://localhost:8000/api/v1/auth/logout \
  -H "Authorization: Bearer <access_token>"
```

---

## Notas

- Access tokens expiran en 30 minutos
- Refresh tokens expiran en 7 días
- Implementar automatic token refresh en cliente
- Almacenar tokens de forma segura (no en localStorage plano para mobile)


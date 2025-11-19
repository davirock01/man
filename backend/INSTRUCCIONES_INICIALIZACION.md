# 🚀 INICIALIZACIÓN DEL BACKEND

## Paso 1: Iniciar servicios Docker

```bash
cd backend
docker-compose up -d
```

Esto inicia:
- PostgreSQL (puerto 5432)
- Redis (puerto 6379)
- Backend API (puerto 8000)

## Paso 2: Inicializar base de datos

### Opción A: Desde tu PC (Recomendado)

```bash
cd backend

# Conectar a PostgreSQL y ejecutar SQL
docker-compose exec postgres psql -U postgres -d fleet_maintenance -f /app/app/db/init_db.sql
```

### Opción B: Copiar SQL manualmente

```bash
# Conectar a PostgreSQL
docker-compose exec postgres psql -U postgres -d fleet_maintenance

# Dentro de psql, copiar y pegar el contenido de app/db/init_db.sql
```

## Paso 3: Verificar

```bash
# Verificar que las tablas se crearon
docker-compose exec postgres psql -U postgres -d fleet_maintenance -c "\dt"

# Ver usuarios de prueba
docker-compose exec postgres psql -U postgres -d fleet_maintenance -c "SELECT email, rol FROM usuarios;"

# Ver vehículos de prueba  
docker-compose exec postgres psql -U postgres -d fleet_maintenance -c "SELECT placa, modelo FROM vehiculos;"
```

## Paso 4: Verificar API

Abrir en navegador: http://localhost:8000

Debe mostrar:
```json
{
  "message": "Fleet Maintenance System API",
  "docs": "/api/docs",
  "health": "/health"
}
```

## Paso 5: Ver documentación API

Abrir: http://localhost:8000/api/docs

Aquí verás todos los endpoints (cuando estén implementados).

---

## Usuarios de Prueba Creados

| Email | Password | Rol |
|-------|----------|-----|
| admin@test.com | testpass123 | ADMIN |
| coordinador@test.com | testpass123 | COORDINADOR |
| conductor@test.com | testpass123 | CONDUCTOR |
| tecnico@test.com | testpass123 | TECNICO |

## Vehículos de Prueba Creados

| Placa | Modelo | Tipo | Odómetro |
|-------|--------|------|----------|
| TEST123 | Toyota Hilux 4x4 | PICKUP | 50,000 km |
| TURBO456 | Ford Ranger Turbo | TURBO | 75,000 km |


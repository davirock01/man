#!/bin/bash
# ================================================================
# FLEET MAINTENANCE SYSTEM - INICIO RÁPIDO
# Script para Linux/Mac
# ================================================================

echo ""
echo "================================================================"
echo "  FLEET MAINTENANCE SYSTEM - INICIANDO..."
echo "================================================================"
echo ""

# Verificar Docker
echo "[1/5] Verificando Docker..."
if ! command -v docker &> /dev/null; then
    echo "❌ ERROR: Docker no está instalado"
    echo "Por favor instala Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ ERROR: Docker Compose no está instalado"
    echo "Por favor instala Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

# Iniciar servicios backend (PostgreSQL + Redis + API)
echo ""
echo "[2/5] Iniciando servicios backend (PostgreSQL + Redis + FastAPI)..."
cd backend
docker-compose up -d

if [ $? -ne 0 ]; then
    echo "❌ ERROR: No se pudo iniciar Docker Compose"
    exit 1
fi

# Esperar a que los servicios estén listos
echo ""
echo "[3/5] Esperando a que los servicios estén listos (10 segundos)..."
sleep 10

# Ejecutar migraciones (si existen)
echo ""
echo "[4/5] Ejecutando migraciones de base de datos..."
docker-compose exec -T backend alembic upgrade head 2>/dev/null || echo "⚠️  ADVERTENCIA: No se pudieron ejecutar migraciones (puede ser primera vez)"

# Abrir navegador con frontend
echo ""
echo "[5/5] Intentando abrir aplicación web..."
sleep 2

# Verificar si el frontend está corriendo
if curl -s http://localhost:3000 > /dev/null 2>&1; then
    # Abrir navegador según el sistema operativo
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open http://localhost:3000
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open http://localhost:3000 2>/dev/null || sensible-browser http://localhost:3000 2>/dev/null
    fi
else
    echo ""
    echo "📝 NOTA: El frontend web aún no está corriendo."
    echo ""
    echo "Para iniciar el frontend web:"
    echo "  1. Abre una nueva terminal"
    echo "  2. cd frontend-web"
    echo "  3. npm install (solo primera vez)"
    echo "  4. npm run dev"
    echo ""
    echo "Luego el navegador se abrirá automáticamente en http://localhost:3000"
    echo ""
fi

echo ""
echo "================================================================"
echo "  ✅ SERVICIOS INICIADOS"
echo "================================================================"
echo ""
echo "  🌐 Backend API:      http://localhost:8000"
echo "  📚 API Docs:         http://localhost:8000/api/docs"
echo "  💻 Frontend Web:     http://localhost:3000"
echo "  🗄️  PostgreSQL:       localhost:5432"
echo "  🔴 Redis:            localhost:6379"
echo ""
echo "================================================================"
echo "  📋 COMANDOS ÚTILES"
echo "================================================================"
echo ""
echo "  Ver logs backend:     cd backend && docker-compose logs -f"
echo "  Detener servicios:    cd backend && docker-compose down"
echo "  Reiniciar servicios:  cd backend && docker-compose restart"
echo "  Ver estado:           cd backend && docker-compose ps"
echo ""
echo "================================================================"
echo ""
echo "Presiona Ctrl+C para salir de los logs..."
echo ""

# Mostrar logs
cd backend
docker-compose logs -f


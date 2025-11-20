@echo off
REM ================================================================
REM FLEET MAINTENANCE SYSTEM - INICIO RÁPIDO
REM Script para Windows
REM ================================================================

echo.
echo ================================================================
echo  FLEET MAINTENANCE SYSTEM - INICIANDO...
echo ================================================================
echo.

REM Verificar que existe la carpeta backend
if not exist "backend\" (
    echo.
    echo ================================================================
    echo  ERROR: LA CARPETA backend/ NO EXISTE
    echo ================================================================
    echo.
    echo El codigo del proyecto aun no ha sido creado.
    echo.
    echo Por favor:
    echo   1. Ejecuta: VERIFICAR_PROYECTO.bat
    echo   2. Consulta con el equipo de desarrollo
    echo.
    pause
    exit /b 1
)

REM Verificar Docker
echo [1/5] Verificando Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker no esta instalado o no esta en el PATH
    echo Por favor instala Docker Desktop: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

REM Iniciar servicios backend (PostgreSQL + Redis + API)
echo.
echo [2/5] Iniciando servicios backend (PostgreSQL + Redis + FastAPI)...
cd backend
docker-compose up -d
if errorlevel 1 (
    echo ERROR: No se pudo iniciar Docker Compose
    pause
    exit /b 1
)

REM Esperar a que los servicios estén listos
echo.
echo [3/5] Esperando a que los servicios estén listos (10 segundos)...
timeout /t 10 /nobreak >nul

REM Ejecutar migraciones (si existen)
echo.
echo [4/5] Ejecutando migraciones de base de datos...
docker-compose exec -T backend alembic upgrade head
if errorlevel 1 (
    echo ADVERTENCIA: No se pudieron ejecutar migraciones (puede ser primera vez)
)

REM Abrir navegador con frontend
echo.
echo [5/5] Abriendo aplicacion web en el navegador...
timeout /t 2 /nobreak >nul

REM Verificar si el frontend está corriendo en el puerto
curl -s http://localhost:3000 >nul 2>&1
if errorlevel 1 (
    echo.
    echo NOTA: El frontend web aun no esta corriendo.
    echo.
    echo Para iniciar el frontend web:
    echo   1. Abre una nueva terminal
    echo   2. cd frontend-web
    echo   3. npm install (solo primera vez)
    echo   4. npm run dev
    echo.
    echo Luego el navegador se abrira automaticamente en http://localhost:3000
    echo.
) else (
    start http://localhost:3000
)

echo.
echo ================================================================
echo  SERVICIOS INICIADOS
echo ================================================================
echo.
echo  Backend API:      http://localhost:8000
echo  API Docs:         http://localhost:8000/api/docs
echo  Frontend Web:     http://localhost:3000
echo  PostgreSQL:       localhost:5432
echo  Redis:            localhost:6379
echo.
echo ================================================================
echo  COMANDOS UTILES
echo ================================================================
echo.
echo  Ver logs backend:     cd backend ^&^& docker-compose logs -f
echo  Detener servicios:    cd backend ^&^& docker-compose down
echo  Reiniciar servicios:  cd backend ^&^& docker-compose restart
echo  Ver estado:           cd backend ^&^& docker-compose ps
echo.
echo ================================================================
echo.
echo Presiona cualquier tecla para ver los logs del backend...
pause >nul

cd backend
docker-compose logs -f


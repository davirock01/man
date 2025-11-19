@echo off
REM ================================================================
REM ARREGLAR DOCKER Y ABRIR APP (PRIMERA VEZ)
REM 
REM USA ESTE SCRIPT LA PRIMERA VEZ o si hay problemas
REM 
REM Este script:
REM - Descarga la imagen Python si no existe
REM - Construye la imagen del backend
REM - Inicia todo con Docker
REM 
REM Despues de ejecutar este, usa: ABRIR_APP.bat
REM ================================================================

color 0A
title Fleet Maintenance System - Descargando e Iniciando
echo.
echo ================================================================
echo   FLEET MAINTENANCE SYSTEM
echo   Paso 1: Descargar imagen Python
echo   Paso 2: Iniciar todo con Docker
echo ================================================================
echo.

cd /d "%~dp0backend"

REM Verificar Docker
echo [1/8] Verificando Docker Desktop...
docker ps >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Docker Desktop no esta corriendo
    echo.
    echo Inicia Docker Desktop y ejecuta este script nuevamente.
    pause
    exit /b 1
)
echo [OK] Docker Desktop corriendo
echo.

REM Descargar imagen Python si no existe
echo [2/8] Verificando imagen Python...
docker images python:3.11-slim -q >nul 2>&1
if errorlevel 1 (
    echo [!] Imagen Python no encontrada. Descargando...
    echo    (Esto puede tardar 2-3 minutos)
    echo.
    docker pull python:3.11-slim
    if errorlevel 1 (
        echo.
        echo ================================================================
        echo [X] ERROR: No se pudo descargar la imagen Python
        echo ================================================================
        echo.
        echo SOLUCION:
        echo.
        echo 1. Verifica tu conexion a internet
        echo 2. Configura DNS en Docker Desktop:
        echo    - Abre Docker Desktop
        echo    - Settings ^> Docker Engine
        echo    - Agrega: "dns": ["8.8.8.8", "8.8.4.4"]
        echo    - Apply ^& Restart
        echo.
        echo 3. Si estas en red corporativa, configura proxy en Docker Desktop
        echo.
        echo O usa: ABRIR_APP_SIN_DOCKER.bat (no necesita descargar nada)
        echo.
        pause
        exit /b 1
    )
    echo [OK] Imagen Python descargada
) else (
    echo [OK] Imagen Python ya existe localmente
)
echo.

REM Iniciar PostgreSQL y Redis
echo [3/8] Iniciando PostgreSQL y Redis...
docker-compose up -d postgres redis
if errorlevel 1 (
    echo [X] ERROR al iniciar servicios base
    pause
    exit /b 1
)
echo [OK] PostgreSQL y Redis iniciados
echo.

REM Esperar a que PostgreSQL esté listo
echo [4/8] Esperando a que PostgreSQL este listo (15 segundos)...
timeout /t 15 /nobreak >nul
echo [OK] PostgreSQL listo
echo.

REM Construir imagen del backend
echo [5/8] Construyendo imagen del Backend...
docker-compose build backend
if errorlevel 1 (
    echo [X] ERROR al construir imagen del Backend
    echo.
    echo Revisa los logs arriba para ver el error especifico.
    pause
    exit /b 1
)
echo [OK] Imagen del Backend construida
echo.

REM Iniciar backend
echo [6/8] Iniciando Backend API...
docker-compose up -d backend
if errorlevel 1 (
    echo [X] ERROR al iniciar Backend
    pause
    exit /b 1
)
echo [OK] Backend iniciado
echo.

REM Esperar a que backend esté listo
echo Esperando a que Backend este listo (10 segundos)...
timeout /t 10 /nobreak >nul

REM Verificar backend
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo [!] ADVERTENCIA: Backend aun no responde
    echo.
    echo Verificando logs del backend...
    docker-compose logs --tail=20 backend
    echo.
) else (
    echo [OK] Backend respondiendo correctamente
)
echo.

cd ..

REM Verificar frontend
echo [7/8] Verificando Frontend Web...
if not exist "frontend-web\node_modules\" (
    echo [!] Instalando dependencias del frontend...
    cd frontend-web
    call npm install
    if errorlevel 1 (
        echo [X] ERROR al instalar dependencias
        pause
        exit /b 1
    )
    cd ..
    echo [OK] Dependencias instaladas
) else (
    echo [OK] Frontend listo
)
echo.

REM Iniciar frontend
echo [8/8] Iniciando Frontend...
echo.

REM Abrir navegador
start http://localhost:8000
timeout /t 1 /nobreak >nul
start http://localhost:8000/api/docs
timeout /t 1 /nobreak >nul

REM Iniciar frontend en nueva ventana
cd frontend-web
start "Fleet Maintenance Frontend" cmd /k "npm run dev"
cd ..

echo.
echo ================================================================
echo   SISTEMA INICIADO CON DOCKER CORRECTAMENTE
echo ================================================================
echo.
echo   Backend API:       http://localhost:8000
echo   API Docs:          http://localhost:8000/api/docs
echo   Frontend Web:      http://localhost:3000
echo.
echo   Contenedores Docker activos:
echo   - fleet_postgres (Puerto 5435)
echo   - fleet_redis (Puerto 6380)
echo   - fleet_backend (Puerto 8000)
echo.
echo ================================================================
echo   CREDENCIALES:
echo ================================================================
echo.
echo   coordinador@test.com / testpass123
echo.
echo ================================================================
echo.
echo Presiona cualquier tecla para cerrar...
pause >nul


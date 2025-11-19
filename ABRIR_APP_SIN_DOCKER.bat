@echo off
REM ================================================================
REM FLEET MAINTENANCE SYSTEM - INICIAR SIN CONTENEDOR DOCKER BACKEND
REM Solo usa Docker para PostgreSQL y Redis, Backend corre local
REM ================================================================

color 0A
title Fleet Maintenance System - Iniciando (Sin Docker Backend)
echo.
echo ================================================================
echo   FLEET MAINTENANCE SYSTEM - INICIANDO
echo   (PostgreSQL/Redis en Docker, Backend local)
echo ================================================================
echo.

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Verificar Python instalado
echo [1/7] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Python no esta instalado
    echo.
    echo Descarga Python 3.11+ de: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [OK] Python instalado
echo.

REM Verificar Docker instalado
echo [2/7] Verificando Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Docker no esta instalado
    echo.
    echo Descarga Docker Desktop de: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo [OK] Docker instalado
echo.

REM Verificar Docker corriendo
echo [3/7] Verificando que Docker Desktop este corriendo...
docker ps >nul 2>&1
if errorlevel 1 (
    echo.
    echo ================================================================
    echo [X] ERROR: DOCKER DESKTOP NO ESTA CORRIENDO
    echo ================================================================
    echo.
    echo SOLUCION:
    echo   1. Busca "Docker Desktop" en Windows
    echo   2. Haz clic para iniciarlo
    echo   3. ESPERA 1-2 MINUTOS hasta que este listo
    echo   4. Ejecuta este script nuevamente
    echo.
    pause
    exit /b 1
)
echo [OK] Docker Desktop corriendo
echo.

REM Iniciar servicios base (PostgreSQL + Redis) SOLO
echo [4/7] Iniciando PostgreSQL y Redis...
cd backend
docker-compose up -d postgres redis
if errorlevel 1 (
    echo [X] ERROR al iniciar PostgreSQL o Redis
    pause
    exit /b 1
)
echo [OK] PostgreSQL y Redis iniciados
echo.

REM Esperar a que PostgreSQL esté listo
echo [5/7] Esperando a que PostgreSQL este listo (15 segundos)...
timeout /t 15 /nobreak >nul
echo [OK] PostgreSQL listo
echo.

REM Instalar dependencias Python si no existen
echo [6/7] Verificando dependencias del Backend...
if not exist "venv\" (
    echo [!] Creando entorno virtual Python (solo primera vez)...
    python -m venv venv
    if errorlevel 1 (
        echo [X] ERROR al crear entorno virtual
        pause
        exit /b 1
    )
    echo [OK] Entorno virtual creado
)

echo [!] Instalando dependencias Python (puede tardar 1-2 min la primera vez)...
call venv\Scripts\activate.bat
pip install -r requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [!] ADVERTENCIA: Algunas dependencias pueden tener conflictos, pero continuamos...
)
echo [OK] Dependencias instaladas
echo.

REM Iniciar backend en nueva ventana
echo Iniciando Backend API en nueva ventana...
start "Fleet Maintenance Backend" cmd /k "cd /d %CD% && venv\Scripts\activate && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

echo Esperando a que Backend este listo (10 segundos)...
timeout /t 10 /nobreak >nul

REM Verificar backend
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo [!] ADVERTENCIA: Backend aun no responde (puede tardar unos segundos mas)
) else (
    echo [OK] Backend respondiendo correctamente
)
echo.

REM Volver a raíz
cd ..

REM Verificar si frontend tiene node_modules
echo [7/7] Verificando Frontend Web...
if not exist "frontend-web\node_modules\" (
    echo [!] Instalando dependencias del frontend (solo primera vez, puede tardar 2-3 min)...
    cd frontend-web
    call npm install
    if errorlevel 1 (
        echo [X] ERROR al instalar dependencias del frontend
        pause
        exit /b 1
    )
    cd ..
    echo [OK] Dependencias instaladas
) else (
    echo [OK] Frontend ya tiene dependencias
)
echo.

REM Abrir URLs en navegador
echo Abriendo aplicacion en navegador...
timeout /t 2 /nobreak >nul
start http://localhost:8000
timeout /t 1 /nobreak >nul
start http://localhost:8000/api/docs
timeout /t 1 /nobreak >nul

REM Iniciar frontend en nueva ventana
echo Iniciando Frontend Web en nueva ventana...
cd frontend-web
start "Fleet Maintenance Frontend" cmd /k "npm run dev"
cd ..

echo.
echo ================================================================
echo   SISTEMA INICIADO CORRECTAMENTE
echo ================================================================
echo.
echo   Backend API:       http://localhost:8000
echo   API Docs:          http://localhost:8000/api/docs
echo   Health Check:      http://localhost:8000/health
echo   Frontend Web:      http://localhost:3000 (se abrira automaticamente)
echo.
echo ================================================================
echo   CREDENCIALES DE PRUEBA:
echo ================================================================
echo.
echo   Coordinador:  coordinador@test.com / testpass123
echo   Conductor:    conductor@test.com / testpass123
echo   Tecnico:      tecnico@test.com / testpass123
echo   Admin:        admin@test.com / testpass123
echo.
echo ================================================================
echo   COMANDOS UTILES:
echo ================================================================
echo.
echo   Ver logs backend:      Revisa la ventana "Fleet Maintenance Backend"
echo   Reiniciar backend:     Cierra ventana Backend y ejecuta este script
echo   Detener servicios:     cd backend ^&^& docker-compose down
echo   Ver estado Docker:     cd backend ^&^& docker-compose ps
echo.
echo ================================================================
echo.
echo NOTA: Backend corre LOCAL (no en Docker) por problemas de conexion
echo El frontend se abrira automaticamente en http://localhost:3000
echo.
echo Presiona cualquier tecla para cerrar esta ventana...
echo (Los servicios seguiran corriendo en las ventanas abiertas)
pause >nul


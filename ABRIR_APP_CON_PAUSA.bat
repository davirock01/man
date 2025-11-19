@echo off
REM ================================================================
REM FLEET MAINTENANCE SYSTEM - VERSION CON PAUSA PARA VER ERRORES
REM ================================================================

color 0A
title Fleet Maintenance System - Iniciando...
echo.
echo ================================================================
echo   FLEET MAINTENANCE SYSTEM - INICIANDO TODO
echo ================================================================
echo.

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Verificar Docker instalado
echo [1/6] Verificando Docker...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Docker no esta instalado
    echo.
    echo Descarga Docker Desktop de: https://www.docker.com/products/docker-desktop
    echo.
    pause
    exit /b 1
)
echo [OK] Docker instalado
echo.

REM Verificar Docker corriendo
echo [2/6] Verificando que Docker Desktop este corriendo...
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
    echo.
    pause
    exit /b 1
)
echo [OK] Docker Desktop corriendo
echo.

REM Iniciar servicios base (PostgreSQL + Redis)
echo [3/6] Iniciando PostgreSQL y Redis...
cd backend
docker-compose up -d postgres redis 2>&1
if errorlevel 1 (
    echo [X] ERROR al iniciar PostgreSQL o Redis
    echo.
    echo Mostrando logs...
    docker-compose ps
    echo.
    pause
    exit /b 1
)
echo [OK] PostgreSQL y Redis iniciados
echo.

REM Esperar a que PostgreSQL esté listo
echo [4/6] Esperando a que PostgreSQL este listo (15 segundos)...
timeout /t 15 /nobreak >nul
echo [OK] PostgreSQL listo
echo.

REM Iniciar backend
echo [5/6] Iniciando Backend API...
echo.
echo Si falla aqui, es porque no tiene la imagen Python.
echo Usa: ARREGLAR_DOCKER_Y_ABRIR.bat para descargarla.
echo.
docker-compose up -d backend 2>&1
if errorlevel 1 (
    echo.
    echo [X] ERROR al iniciar Backend
    echo.
    echo CAUSA PROBABLE: Imagen Python no descargada
    echo.
    echo SOLUCION: Ejecuta ARREGLAR_DOCKER_Y_ABRIR.bat primero
    echo.
    echo Mostrando logs del error...
    docker-compose logs --tail=30 backend
    echo.
    pause
    exit /b 1
)
echo [OK] Backend iniciado
echo.

REM Esperar a que backend esté listo
echo Esperando a que Backend este listo (10 segundos)...
timeout /t 10 /nobreak >nul

REM Verificar backend
echo Verificando que backend responde...
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo [!] ADVERTENCIA: Backend aun no responde
    echo.
    echo Mostrando ultimos logs del backend...
    docker-compose logs --tail=30 backend
    echo.
    echo Si ves errores arriba, el backend crasheo.
    echo.
) else (
    echo [OK] Backend respondiendo correctamente
)
echo.

REM Volver a raíz
cd ..

REM Verificar si frontend tiene node_modules
echo [6/6] Verificando Frontend Web...
if not exist "frontend-web\node_modules\" (
    echo [!] Instalando dependencias del frontend (solo primera vez)...
    echo    (Esto puede tardar 2-3 minutos)
    echo.
    cd frontend-web
    call npm install
    if errorlevel 1 (
        echo [X] ERROR al instalar dependencias del frontend
        echo.
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
start http://localhost:8000 2>nul
timeout /t 1 /nobreak >nul
start http://localhost:8000/api/docs 2>nul
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
echo   Ver logs backend:      cd backend ^&^& docker-compose logs -f backend
echo   Reiniciar backend:     cd backend ^&^& docker-compose restart backend
echo   Detener servicios:     cd backend ^&^& docker-compose down
echo   Ver estado:            cd backend ^&^& docker-compose ps
echo.
echo ================================================================
echo.
echo El frontend se abrira automaticamente en http://localhost:3000
echo.
echo Presiona cualquier tecla para cerrar esta ventana...
echo (Los servicios seguiran corriendo en segundo plano)
echo.
pause


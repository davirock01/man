@echo off
REM ================================================================
REM INICIAR SOLO EL FRONTEND
REM (Cuando el backend ya está corriendo en Docker)
REM ================================================================

color 0B
title Fleet Maintenance - Iniciando Frontend
echo.
echo ================================================================
echo   INICIANDO FRONTEND WEB
echo   (Backend debe estar corriendo en Docker)
echo ================================================================
echo.

cd /d "%~dp0"

REM Buscar carpeta frontend-web
if exist "frontend-web" (
    cd frontend-web
) else if exist "man\frontend-web" (
    cd man\frontend-web
) else if exist "..\frontend-web" (
    cd ..\frontend-web
) else (
    echo [X] ERROR: No se encuentra carpeta frontend-web
    echo.
    echo Verifica que estas en la carpeta correcta del proyecto.
    pause
    exit /b 1
)

echo Carpeta frontend encontrada: %CD%
echo.

REM Verificar node_modules
if not exist "node_modules\" (
    echo [!] Instalando dependencias (solo primera vez)...
    echo     Esto puede tardar 2-3 minutos...
    echo.
    call npm install
    if errorlevel 1 (
        echo [X] ERROR al instalar dependencias
        pause
        exit /b 1
    )
    echo [OK] Dependencias instaladas
    echo.
)

REM Verificar que backend esté corriendo
echo Verificando que backend este corriendo...
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo.
    echo [!] ADVERTENCIA: Backend no responde en localhost:8000
    echo.
    echo Verifica que los contenedores Docker esten corriendo:
    echo     docker ps
    echo.
    echo Debes ver: fleet_backend, fleet_postgres, fleet_redis
    echo.
    echo Si no estan corriendo, ejecuta:
    echo     cd backend
    echo     docker-compose up -d
    echo.
    pause
)

echo.
echo ================================================================
echo   INICIANDO SERVIDOR DE DESARROLLO
echo ================================================================
echo.
echo El navegador se abrira automaticamente en:
echo   http://localhost:3000
echo.
echo Login:
echo   Email:    coordinador@test.com
echo   Password: testpass123
echo.
echo ================================================================
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

REM Iniciar frontend
npm run dev

pause


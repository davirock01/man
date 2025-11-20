@echo off
REM ================================================================
REM VERSION INTELIGENTE - INTENTA DOCKER, SI FALLA USA LOCAL
REM ================================================================

echo.
echo ================================================================
echo   FLEET MAINTENANCE - INICIO INTELIGENTE
echo ================================================================
echo.

REM Intentar con Docker primero
echo [OPCION 1] Intentando con Docker...
echo.

docker ps >nul 2>&1
if not errorlevel 1 (
    echo [OK] Docker esta corriendo! Usando version con Docker...
    echo.
    cd backend
    docker-compose up -d --build
    if not errorlevel 1 (
        echo.
        echo ================================================================
        echo   DOCKER VERSION INICIADA
        echo ================================================================
        echo.
        echo   Backend API:  http://localhost:8000
        echo   API Docs:     http://localhost:8000/api/docs
        echo.
        timeout /t 3 /nobreak >nul
        start http://localhost:8000/api/docs
        echo.
        echo Ver logs: cd backend ^&^& docker-compose logs -f backend
        echo.
        pause
        exit /b 0
    )
)

REM Si Docker falla, usar version local
echo.
echo [OPCION 2] Docker no disponible. Usando version local (Python)...
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Python tampoco esta instalado
    echo.
    echo Por favor instala Python: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python encontrado. Iniciando version local...
echo.

REM Ejecutar version sin Docker
call INICIAR_BACKEND_SIMPLE.bat


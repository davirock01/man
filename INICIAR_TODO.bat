@echo off
REM ================================================================
REM INICIAR TODO EL SISTEMA (Backend + Frontend)
REM ================================================================

echo.
echo ================================================================
echo   FLEET MAINTENANCE - INICIO COMPLETO
echo ================================================================
echo.

echo Este script iniciara:
echo   1. Backend API (Python/FastAPI)
echo   2. Frontend Web (React/Vite)
echo.
echo IMPORTANTE: Se abriran 2 ventanas (no las cierres)
echo.
pause

REM Iniciar backend en nueva ventana
echo.
echo [1/2] Iniciando Backend...
start "Fleet Backend" cmd /k INICIAR_BACKEND_SIMPLE.bat

echo [OK] Backend iniciando en nueva ventana
echo      Espera 20 segundos para que este listo...
timeout /t 20 /nobreak

REM Iniciar frontend en nueva ventana
echo.
echo [2/2] Iniciando Frontend...
start "Fleet Frontend" cmd /k INICIAR_FRONTEND.bat

echo [OK] Frontend iniciando en nueva ventana
echo.
echo ================================================================
echo   SISTEMA INICIADO
echo ================================================================
echo.
echo Se abrieron 2 ventanas:
echo   1. Backend:  http://localhost:8000
echo   2. Frontend: http://localhost:3000
echo.
echo Espera 30-40 segundos y luego:
echo   - Backend:  http://localhost:8000/api/docs
echo   - Frontend: http://localhost:3000
echo.
echo NO cierres las ventanas del backend y frontend.
echo.
echo ================================================================
echo.
pause


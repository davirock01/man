@echo off
REM ================================================================
REM SISTEMA COMPLETO - BACKEND + APLICACION WEB
REM TODO EN UN SOLO SCRIPT
REM ================================================================

color 0A
echo.
echo ================================================================
echo   FLEET MAINTENANCE SYSTEM - INICIO COMPLETO
echo ================================================================
echo.

REM Iniciar backend en nueva ventana
echo [1/2] Iniciando Backend API...
start "Fleet Maintenance Backend" /min cmd /k "cd /d %CD%\backend && python init_db_local.py && python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

echo [OK] Backend iniciando en nueva ventana (minimizada)
echo      Espera 15 segundos para que este listo...
echo.

REM Esperar a que el backend esté listo
timeout /t 15 /nobreak

REM Verificar que backend responde
echo Verificando backend...
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo [!] Backend aun no responde, esperando 10 segundos mas...
    timeout /t 10 /nobreak
)

echo.
echo [2/2] Abriendo aplicacion web...
echo.

REM Abrir aplicación
start "" "webapp\index.html"

echo.
echo ================================================================
echo   SISTEMA INICIADO CORRECTAMENTE
echo ================================================================
echo.
echo   Backend API:    http://localhost:8000 (minimizado)
echo   Aplicacion Web: Abierta en navegador
echo.
echo ================================================================
echo   USUARIOS DE PRUEBA (password: testpass123):
echo ================================================================
echo.
echo   - coordinador@test.com (Dashboard completo)
echo   - conductor@test.com (App movil futuro)
echo   - tecnico@test.com (App movil futuro)
echo   - admin@test.com (Administracion)
echo.
echo ================================================================
echo   IMPORTANTE:
echo ================================================================
echo.
echo   El backend esta corriendo en una ventana minimizada.
echo   NO la cierres o la aplicacion dejara de funcionar.
echo.
echo   Para detener el sistema:
echo     - Busca la ventana "Fleet Maintenance Backend"
echo     - Presiona Ctrl+C
echo.
echo ================================================================
echo.
echo Disfruta el sistema!
echo.
pause


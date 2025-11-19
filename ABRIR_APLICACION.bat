@echo off
REM ================================================================
REM ABRIR APLICACION WEB - UN SOLO CLIC
REM ================================================================

echo.
echo ================================================================
echo   ABRIENDO FLEET MAINTENANCE SYSTEM
echo ================================================================
echo.

echo [1/2] Verificando que el backend este corriendo...
echo.

REM Verificar si backend está corriendo
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo [!] BACKEND NO ESTA CORRIENDO
    echo.
    echo Necesitas iniciar el backend primero:
    echo   1. Abre otra ventana
    echo   2. Ejecuta: INICIAR_BACKEND_SIMPLE.bat
    echo   3. Espera que diga "Application startup complete"
    echo   4. Luego ejecuta este script de nuevo
    echo.
    pause
    exit /b 1
)

echo [OK] Backend esta corriendo en http://localhost:8000
echo.

echo [2/2] Abriendo aplicacion web...
echo.

REM Abrir aplicación en navegador predeterminado
start "" "webapp\index.html"

echo.
echo ================================================================
echo   APLICACION ABIERTA
echo ================================================================
echo.
echo La aplicacion se abrio en tu navegador.
echo.
echo Si no se abrio automaticamente, abre manualmente:
echo   Ruta: %CD%\webapp\index.html
echo.
echo ================================================================
echo   USUARIOS DE PRUEBA:
echo ================================================================
echo.
echo   Coordinador:  coordinador@test.com / testpass123
echo   Conductor:    conductor@test.com / testpass123
echo   Tecnico:      tecnico@test.com / testpass123
echo   Admin:        admin@test.com / testpass123
echo.
echo ================================================================
echo.
pause


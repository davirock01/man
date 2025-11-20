@echo off
REM ================================================================
REM VERIFICADOR DE ESTRUCTURA DEL PROYECTO
REM ================================================================

echo.
echo ================================================================
echo  VERIFICANDO ESTRUCTURA DEL PROYECTO...
echo ================================================================
echo.

set ERROR=0

REM Verificar backend
if exist "backend\" (
    echo [OK] Carpeta backend/ existe
) else (
    echo [X] FALTA: Carpeta backend/
    set ERROR=1
)

REM Verificar frontend
if exist "frontend-web\" (
    echo [OK] Carpeta frontend-web/ existe
) else (
    echo [X] FALTA: Carpeta frontend-web/
    set ERROR=1
)

REM Verificar mobile
if exist "mobile-app\" (
    echo [OK] Carpeta mobile-app/ existe
) else (
    echo [X] FALTA: Carpeta mobile-app/
    set ERROR=1
)

REM Verificar docker-compose
if exist "backend\docker-compose.yml" (
    echo [OK] Archivo backend/docker-compose.yml existe
) else (
    echo [X] FALTA: Archivo backend/docker-compose.yml
    set ERROR=1
)

echo.
echo ================================================================

if %ERROR%==1 (
    echo.
    echo ERROR: EL CODIGO NO HA SIDO CREADO AUN
    echo.
    echo SITUACION:
    echo   Los agentes reportaron haber completado el codigo,
    echo   pero NO lo crearon fisicamente en el proyecto.
    echo.
    echo   Solo existe la DOCUMENTACION, no el codigo.
    echo.
    echo SOLUCION:
    echo   1. Los agentes deben CREAR el codigo fisicamente
    echo   2. Agente 1: Crear carpeta backend/ con el codigo
    echo   3. Agente 2: Crear carpetas frontend-web/ y mobile-app/
    echo   4. Ejecutar este script nuevamente para verificar
    echo.
    echo Para mas informacion, consulta: docs/PROJECT_STATUS.md
    echo.
) else (
    echo.
    echo [OK] PROYECTO COMPLETO - Todas las carpetas existen
    echo.
    echo Puedes ejecutar: MANTENIMIENTO.bat
    echo.
)

echo ================================================================
echo.
pause


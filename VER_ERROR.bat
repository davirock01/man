@echo off
REM Este script NO se cierra solo - se queda abierto mostrando el error

title CAPTURANDO ERROR - NO CIERRES ESTA VENTANA
color 0C

echo.
echo ================================================================
echo   CAPTURANDO ERROR DEL SCRIPT
echo ================================================================
echo.

cd /d "%~dp0"

echo Directorio actual:
cd
echo.

echo Verificando archivos...
if exist "backend" (
    echo [OK] Carpeta backend existe
) else (
    echo [X] ERROR: No existe carpeta backend
    echo.
    echo Estas en la carpeta incorrecta.
    echo Debes estar en: C:\Users\User-PC\Desktop\software engineering\app\man
    echo.
    goto FIN
)

if exist "frontend-web" (
    echo [OK] Carpeta frontend-web existe
) else (
    echo [X] ERROR: No existe carpeta frontend-web
    goto FIN
)

echo.
echo Verificando Docker...
docker --version
if errorlevel 1 (
    echo [X] ERROR: Docker no esta instalado
    goto FIN
)
echo [OK] Docker instalado
echo.

echo Verificando Docker Desktop corriendo...
docker ps
if errorlevel 1 (
    echo [X] ERROR: Docker Desktop no esta corriendo
    echo.
    echo SOLUCION: Inicia Docker Desktop y espera 2 minutos
    goto FIN
)
echo [OK] Docker Desktop corriendo
echo.

echo Entrando a carpeta backend...
cd backend
echo.

echo Verificando docker-compose.yml...
if exist "docker-compose.yml" (
    echo [OK] docker-compose.yml existe
) else (
    echo [X] ERROR: No existe docker-compose.yml
    goto FIN
)
echo.

echo Contenido de docker-compose.yml:
type docker-compose.yml
echo.
echo ================================================================
echo.

echo Contenedores Docker actuales:
docker ps -a
echo.
echo ================================================================
echo.

echo Imagenes Docker disponibles:
docker images
echo.
echo ================================================================
echo.

echo Intentando iniciar PostgreSQL y Redis...
docker-compose up -d postgres redis
echo.
echo ================================================================
echo.

:FIN
echo.
echo ================================================================
echo   FIN DEL DIAGNOSTICO
echo ================================================================
echo.
echo Esta ventana NO se cerrara automaticamente.
echo Lee los mensajes arriba para encontrar el error.
echo.
echo Presiona Ctrl+C o cierra esta ventana manualmente.
echo.
pause


@echo off
REM ================================================================
REM DIAGNOSTICO COMPLETO - ENCONTRAR EL PROBLEMA REAL
REM ================================================================

color 0E
echo.
echo ================================================================
echo   DIAGNOSTICO COMPLETO DEL PROBLEMA
echo ================================================================
echo.

cd /d "%~dp0backend"

echo [1] Probando conexion a Docker Hub...
echo.
curl -I https://registry-1.docker.io 2>&1 | findstr "HTTP"
if errorlevel 1 (
    echo [X] No se puede conectar a Docker Hub
    echo.
    echo Probando DNS...
    nslookup registry-1.docker.io
) else (
    echo [OK] Conexion a Docker Hub funciona
)
echo.
echo ================================================================
echo.

echo [2] Verificando proxy de Docker Desktop...
echo.
docker info | findstr -i "proxy"
echo.
echo ================================================================
echo.

echo [3] Imagenes Docker locales:
echo.
docker images | findstr -i "python postgres redis"
echo.
echo Si NO ves "python:3.11-slim", necesitas descargarlo.
echo.
echo ================================================================
echo.

echo [4] Intentando descargar imagen Python...
echo.
docker pull python:3.11-slim
if errorlevel 1 (
    echo.
    echo [X] ERROR al descargar imagen Python
    echo.
    echo POSIBLES CAUSAS:
    echo 1. Proxy corporativo bloqueando Docker Hub
    echo 2. Firewall bloqueando puerto 443
    echo 3. DNS no resuelve registry-1.docker.io
    echo 4. Docker Desktop necesita configuracion de proxy
    echo.
) else (
    echo.
    echo [OK] Imagen Python descargada correctamente
    echo.
    echo Ahora puedes ejecutar ABRIR_APP.bat
)
echo.
echo ================================================================
echo.
pause


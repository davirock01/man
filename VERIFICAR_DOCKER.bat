@echo off
REM ================================================================
REM VERIFICAR QUE DOCKER SE ESTA USANDO CORRECTAMENTE
REM ================================================================

color 0E
echo.
echo ================================================================
echo   VERIFICACION DE DOCKER
echo ================================================================
echo.

echo [1] Contextos de Docker disponibles:
echo.
docker context ls
echo.
echo ================================================================
echo.

echo [2] Docker que estas usando:
echo.
where docker
echo.
echo ================================================================
echo.

echo [3] Version de Docker:
echo.
docker --version
echo.
echo ================================================================
echo.

echo [4] Imagenes Docker disponibles localmente:
echo.
docker images
echo.
echo ================================================================
echo.

echo [5] Contenedores Docker corriendo:
echo.
docker ps
echo.
echo ================================================================
echo.

echo [6] Todos los contenedores (incluyendo detenidos):
echo.
docker ps -a
echo.
echo ================================================================
echo.

echo INTERPRETACION DE RESULTADOS:
echo.
echo - Si ves "desktop-linux *" en contextos: Estas usando Docker Desktop (CORRECTO)
echo - Si ves imagenes "postgres" y "redis": Ya tienes las imagenes base (BIEN)
echo - Si ves "python" en imagenes: Tienes la imagen del backend (PERFECTO)
echo - Si ves contenedores "fleet_postgres", "fleet_redis": Ya existen (BIEN)
echo.
echo ================================================================
echo.
echo PROBLEMA DEL DOCKER DE VS CODE:
echo.
echo El Docker de VS Code es solo una extension para VISUALIZAR.
echo NO es un Docker diferente. Todos usan el mismo Docker Desktop.
echo.
echo El error "no such host" es por FALTA DE INTERNET o problema DNS,
echo NO por usar Docker incorrecto.
echo.
echo ================================================================
echo.
pause


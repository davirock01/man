@echo off
REM ================================================================
REM DIAGNÓSTICO RÁPIDO: BACKEND NO RESPONDE
REM ================================================================

color 0C
echo.
echo ================================================================
echo   DIAGNOSTICANDO PROBLEMA: BACKEND NO RESPONDE EN PUERTO 8000
echo ================================================================
echo.

cd /d "%~dp0backend"

echo [1/6] Verificando estado de contenedores Docker...
echo.
docker-compose ps
echo.
echo ================================================================
echo.

echo [2/6] Verificando si contenedor backend esta corriendo...
docker ps --filter "name=fleet_backend" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo.
echo ================================================================
echo.

echo [3/6] Verificando ultimos 30 logs del backend...
echo.
docker-compose logs --tail=30 backend
echo.
echo ================================================================
echo.

echo [4/6] Verificando si puerto 8000 esta ocupado...
echo.
netstat -ano | findstr :8000
if errorlevel 1 (
    echo [OK] Puerto 8000 esta libre
) else (
    echo [X] ADVERTENCIA: Puerto 8000 esta en uso
    echo     Revisa el proceso arriba
)
echo.
echo ================================================================
echo.

echo [5/6] Intentando conectar al backend...
echo.
curl -s http://localhost:8000/health
if errorlevel 1 (
    echo [X] ERROR: No se puede conectar al backend
    echo.
    echo Posibles causas:
    echo   1. Contenedor backend no esta corriendo
    echo   2. Contenedor crasheo (revisa logs arriba)
    echo   3. Puerto 8000 bloqueado por firewall
    echo   4. Error en el codigo que impide iniciar
) else (
    echo [OK] Backend responde correctamente
)
echo.
echo ================================================================
echo.

echo [6/6] Verificando servicios dependientes...
echo.
echo PostgreSQL:
docker ps --filter "name=fleet_postgres" --format "table {{.Names}}\t{{.Status}}"
echo.
echo Redis:
docker ps --filter "name=fleet_redis" --format "table {{.Names}}\t{{.Status}}"
echo.
echo ================================================================
echo.

echo DIAGNOSTICO COMPLETO
echo.
echo Si el backend no responde, revisa:
echo   1. Los logs arriba para ver errores
echo   2. El documento: docs\DIRECTIVA_URGENTE_BACKEND_NO_RESPONDE.md
echo   3. Intenta reiniciar: docker-compose restart backend
echo.
echo ================================================================
pause


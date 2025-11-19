@echo off
REM ================================================================
REM CREAR USUARIOS DE PRUEBA EN LA BASE DE DATOS
REM ================================================================

title Creando Usuarios
color 0E

echo.
echo ================================================================
echo   CREANDO USUARIOS DE PRUEBA
echo ================================================================
echo.

cd /d "C:\Users\User-PC\Desktop\software engineering\app\man\man\backend"

echo Ejecutando script SQL...
echo.

docker exec -i fleet_postgres psql -U postgres -d fleet_maintenance < app\db\init_db.sql

if errorlevel 1 (
    echo.
    echo [X] ERROR al ejecutar el script
    echo.
    pause
    exit /b 1
)

echo.
echo ================================================================
echo   USUARIOS CREADOS CORRECTAMENTE
echo ================================================================
echo.
echo Ahora puedes hacer login con:
echo.
echo   Email:    coordinador@test.com
echo   Password: testpass123
echo.
echo Otros usuarios disponibles:
echo   - admin@test.com / testpass123
echo   - conductor@test.com / testpass123
echo   - tecnico@test.com / testpass123
echo.
echo ================================================================
echo.
pause


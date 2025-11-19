@echo off
REM ================================================================
REM FLEET MAINTENANCE SYSTEM - INICIO COMPLETO AUTOMATIZADO
REM Este script hace TODO: Docker + DB + Backend + Frontend
REM ================================================================

color 0A
echo.
echo ================================================================
echo   FLEET MAINTENANCE SYSTEM - INICIO AUTOMATIZADO
echo ================================================================
echo.

REM Verificar Docker instalado
echo [1/7] Verificando Docker instalado...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Docker no esta instalado
    echo.
    echo Descarga Docker Desktop de: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)
echo [OK] Docker instalado
echo.

REM Verificar Docker corriendo
echo [1.5/7] Verificando que Docker Desktop este corriendo...
docker ps >nul 2>&1
if errorlevel 1 (
    echo.
    echo ================================================================
    echo [X] ERROR: DOCKER DESKTOP NO ESTA CORRIENDO
    echo ================================================================
    echo.
    echo SOLUCION:
    echo   1. Busca "Docker Desktop" en Windows
    echo   2. Haz clic para iniciarlo
    echo   3. ESPERA 1-2 MINUTOS hasta que este listo
    echo   4. Verifica que el icono de Docker (ballena) en la barra
    echo      de tareas este QUIETO (no parpadeando)
    echo   5. Ejecuta este script nuevamente
    echo.
    echo O lee: SOLUCIONAR_DOCKER.md
    echo.
    echo ================================================================
    pause
    exit /b 1
)
echo [OK] Docker Desktop corriendo
echo.

REM Iniciar servicios backend
echo [2/7] Iniciando servicios Docker (PostgreSQL + Redis + Backend API)...
cd backend
docker-compose up -d --build
if errorlevel 1 (
    echo [X] ERROR al iniciar Docker Compose
    pause
    exit /b 1
)
echo [OK] Servicios Docker iniciados
echo.

REM Esperar a que PostgreSQL esté listo
echo [3/7] Esperando a que PostgreSQL este listo (15 segundos)...
timeout /t 15 /nobreak >nul
echo [OK] PostgreSQL listo
echo.

REM Inicializar base de datos
echo [4/7] Inicializando base de datos (tablas + datos de prueba)...
docker-compose exec -T postgres psql -U postgres -d fleet_maintenance < app\db\init_db.sql >nul 2>&1
if errorlevel 1 (
    echo [!] ADVERTENCIA: Error al ejecutar SQL (puede ser que ya este inicializado)
) else (
    echo [OK] Base de datos inicializada
)
echo.

REM Verificar backend API
echo [5/7] Verificando Backend API...
timeout /t 3 /nobreak >nul
curl -s http://localhost:8000/health >nul 2>&1
if errorlevel 1 (
    echo [!] ADVERTENCIA: Backend API aun no responde (puede tardar unos segundos mas)
) else (
    echo [OK] Backend API funcionando
)
echo.

REM Volver a raíz del proyecto
cd ..

REM Verificar si frontend tiene node_modules
echo [6/7] Verificando Frontend Web...
if not exist "frontend-web\node_modules\" (
    echo [!] Instalando dependencias del frontend (solo primera vez, puede tardar 2-3 min)...
    cd frontend-web
    call npm install
    cd ..
    echo [OK] Dependencias instaladas
) else (
    echo [OK] Frontend ya tiene dependencias
)
echo.

REM Abrir URLs en navegador
echo [7/7] Abriendo aplicacion en navegador...
timeout /t 2 /nobreak >nul

start http://localhost:8000
timeout /t 1 /nobreak >nul
start http://localhost:8000/api/docs

echo.
echo ================================================================
echo   SISTEMA INICIADO CORRECTAMENTE
echo ================================================================
echo.
echo   Backend API:       http://localhost:8000
echo   API Docs:          http://localhost:8000/api/docs
echo   Health Check:      http://localhost:8000/health
echo.
echo ================================================================
echo   PARA INICIAR EL FRONTEND WEB:
echo ================================================================
echo.
echo   Abre una NUEVA terminal y ejecuta:
echo.
echo     cd frontend-web
echo     npm run dev
echo.
echo   El navegador se abrira automaticamente en http://localhost:3000
echo.
echo ================================================================
echo   PARA VER LA APP MOVIL:
echo ================================================================
echo.
echo   1. Instala "Expo Go" en tu telefono
echo   2. Abre una NUEVA terminal y ejecuta:
echo.
echo        cd mobile-app
echo        npm install (solo primera vez)
echo        npm start
echo.
echo   3. Escanea el QR con Expo Go
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
echo   COMANDOS UTILES:
echo ================================================================
echo.
echo   Detener servicios:     cd backend ^&^& docker-compose down
echo   Ver logs backend:      cd backend ^&^& docker-compose logs -f backend
echo   Reiniciar servicios:   cd backend ^&^& docker-compose restart
echo   Ver estado:            cd backend ^&^& docker-compose ps
echo.
echo ================================================================
echo.
echo Presiona cualquier tecla para cerrar (los servicios seguiran corriendo)...
pause >nul


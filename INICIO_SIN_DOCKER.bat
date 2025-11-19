@echo off
REM ================================================================
REM FLEET MAINTENANCE SYSTEM - INICIO SIN DOCKER (MAS SIMPLE)
REM ================================================================

color 0A
echo.
echo ================================================================
echo   FLEET MAINTENANCE - INICIO SIMPLE (SIN DOCKER)
echo ================================================================
echo.

REM Verificar Python
echo [1/4] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Python no esta instalado
    echo.
    echo Descarga Python de: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [OK] Python encontrado
echo.

REM Instalar dependencias
echo [2/4] Instalando dependencias Python (puede tardar 1-2 min la primera vez)...
cd backend
pip install -q -r requirements.txt
if errorlevel 1 (
    echo [!] Advertencia: Algunas dependencias pueden haber fallado
)
echo [OK] Dependencias instaladas
echo.

REM Inicializar base de datos
echo [3/4] Inicializando base de datos SQLite (usuarios + vehiculos)...
python init_db_local.py
echo [OK] Base de datos lista
echo.

REM Iniciar servidor
echo [4/4] Iniciando servidor Backend API...
echo.
echo ================================================================
echo   SERVIDOR INICIANDO EN http://localhost:8000
echo ================================================================
echo.
echo   API Docs:      http://localhost:8000/api/docs
echo   Health Check:  http://localhost:8000/health
echo.
echo   Usuarios de prueba (password: testpass123):
echo     - admin@test.com
echo     - coordinador@test.com
echo     - conductor@test.com
echo     - tecnico@test.com
echo.
echo   Presiona Ctrl+C para detener el servidor
echo.
echo ================================================================
echo.

REM Abrir navegador
timeout /t 3 /nobreak >nul
start http://localhost:8000/api/docs

REM Iniciar servidor
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


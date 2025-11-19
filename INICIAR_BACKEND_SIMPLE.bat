@echo off
REM ================================================================
REM VERSION ULTRA SIMPLE - BACKEND SIN DOCKER
REM ================================================================

echo.
echo ================================================================
echo   FLEET MAINTENANCE - BACKEND SIMPLE
echo ================================================================
echo.

cd backend

REM Limpiar instalaciones anteriores problemáticas
echo [1/5] Limpiando instalaciones antiguas...
pip uninstall -y bcrypt passlib >nul 2>&1
echo [OK] Limpieza completada
echo.

REM Instalar dependencias básicas
echo [2/5] Instalando dependencias (2-3 min)...
pip install --upgrade pip >nul 2>&1
pip install fastapi uvicorn[standard] sqlalchemy pydantic pydantic-settings python-jose cryptography passlib bcrypt==4.1.2 python-multipart email-validator
if errorlevel 1 (
    echo [X] Error instalando dependencias
    echo.
    echo Intenta manualmente:
    echo   cd backend
    echo   pip install fastapi uvicorn sqlalchemy pydantic passlib bcrypt
    pause
    exit /b 1
)
echo [OK] Dependencias instaladas
echo.

REM Inicializar DB
echo [3/5] Inicializando base de datos...
python init_db_local.py
echo [OK] Base de datos lista
echo.

REM Abrir navegador
echo [4/5] Abriendo navegador...
timeout /t 2 /nobreak >nul
start http://localhost:8000/api/docs
echo.

REM Iniciar servidor
echo [5/5] Iniciando servidor...
echo.
echo ================================================================
echo   SERVIDOR CORRIENDO EN: http://localhost:8000
echo ================================================================
echo.
echo   Swagger UI:  http://localhost:8000/api/docs
echo.
echo   Usuarios (password: testpass123):
echo     - coordinador@test.com
echo     - conductor@test.com
echo.
echo   Presiona Ctrl+C para detener
echo.
echo ================================================================
echo.

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000


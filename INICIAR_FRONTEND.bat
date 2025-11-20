@echo off
REM ================================================================
REM INICIAR FRONTEND WEB
REM ================================================================

echo.
echo ================================================================
echo   INICIANDO FRONTEND WEB (React + Vite)
echo ================================================================
echo.

cd frontend-web

REM Verificar si node_modules existe
if not exist "node_modules\" (
    echo [1/2] Instalando dependencias npm (3-5 min la primera vez)...
    echo.
    call npm install
    if errorlevel 1 (
        echo [X] Error instalando dependencias
        pause
        exit /b 1
    )
    echo [OK] Dependencias instaladas
    echo.
) else (
    echo [1/2] Dependencias ya instaladas
    echo.
)

echo [2/2] Iniciando servidor de desarrollo...
echo.
echo ================================================================
echo   FRONTEND INICIANDO EN: http://localhost:3000
echo ================================================================
echo.
echo   Espera 10-15 segundos...
echo   El navegador se abrira automaticamente
echo.
echo   Presiona Ctrl+C para detener
echo.
echo ================================================================
echo.

REM Iniciar servidor
call npm run dev


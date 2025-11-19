@echo off
REM ================================================================
REM INICIAR FRONTEND - VERSION SIMPLE QUE FUNCIONA
REM ================================================================

title Fleet Maintenance - Frontend
color 0B

echo.
echo ================================================================
echo   INICIANDO FRONTEND WEB
echo ================================================================
echo.

REM Ir directamente a la carpeta correcta
cd /d "C:\Users\User-PC\Desktop\software engineering\app\man\man\frontend-web"

echo Carpeta actual: %CD%
echo.

REM Verificar node_modules
if not exist "node_modules\" (
    echo [!] Instalando dependencias (primera vez, 2-3 min)...
    call npm install
    if errorlevel 1 (
        echo [X] ERROR al instalar dependencias
        echo.
        echo Verifica que Node.js este instalado: node --version
        pause
        exit /b 1
    )
    echo [OK] Dependencias instaladas
    echo.
)

echo.
echo ================================================================
echo   FRONTEND INICIANDO...
echo ================================================================
echo.
echo Se abrira automaticamente en: http://localhost:3000
echo.
echo Login:
echo   Email:    coordinador@test.com
echo   Password: testpass123
echo.
echo Backend debe estar en: http://localhost:8000
echo.
echo ================================================================
echo.
echo Presiona Ctrl+C para detener
echo.

npm run dev

pause


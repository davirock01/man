@echo off
echo.
echo ================================================================
echo   DIAGNOSTICO FRONTEND
echo ================================================================
echo.

REM Verificar Node.js
echo [1/5] Verificando Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [X] Node.js NO esta instalado
    echo.
    echo SOLUCION: Instala Node.js desde https://nodejs.org/
    pause
    exit /b 1
)
node --version
echo [OK] Node.js instalado
echo.

REM Verificar npm
echo [2/5] Verificando npm...
npm --version
echo [OK] npm instalado
echo.

REM Verificar carpeta frontend-web
echo [3/5] Verificando carpeta frontend-web...
if not exist "frontend-web\" (
    echo [X] Carpeta frontend-web NO existe
    pause
    exit /b 1
)
echo [OK] Carpeta frontend-web existe
echo.

REM Verificar archivos principales
echo [4/5] Verificando archivos principales...
if exist "frontend-web\package.json" (
    echo [OK] package.json existe
) else (
    echo [X] package.json NO existe
)

if exist "frontend-web\src\App.tsx" (
    echo [OK] App.tsx existe
) else (
    echo [X] App.tsx NO existe
)

if exist "frontend-web\src\main.tsx" (
    echo [OK] main.tsx existe
) else (
    echo [X] main.tsx NO existe
)
echo.

REM Verificar node_modules
echo [5/5] Verificando dependencias...
if exist "frontend-web\node_modules\" (
    echo [OK] node_modules existe (dependencias instaladas)
) else (
    echo [!] node_modules NO existe
    echo.
    echo Necesitas instalar dependencias primero:
    echo   cd frontend-web
    echo   npm install
)
echo.

echo ================================================================
echo   DIAGNOSTICO COMPLETADO
echo ================================================================
echo.

pause


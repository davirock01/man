@echo off
REM ================================================================
REM SUBIR PROYECTO A GITHUB - AUTOMATICO
REM ================================================================

color 0A
title Subiendo a GitHub

echo.
echo ================================================================
echo   SUBIR PROYECTO A GITHUB
echo ================================================================
echo.

cd /d "%~dp0.."

echo Directorio actual: %CD%
echo.

echo [1/5] Verificando Git...
git --version
if errorlevel 1 (
    echo [X] ERROR: Git no esta instalado
    echo.
    echo Descarga Git de: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo [OK] Git instalado
echo.

echo [2/5] Verificando estado del repositorio...
git status
echo.
echo ================================================================
echo.

echo [3/5] Agregando TODOS los archivos...
git add .
if errorlevel 1 (
    echo [X] ERROR al agregar archivos
    pause
    exit /b 1
)
echo [OK] Archivos agregados
echo.

echo Archivos que se van a subir:
git status --short
echo.
echo ================================================================
echo.

echo [4/5] Haciendo commit...
git commit -m "Implementacion completa: Backend + Frontend + Control de roles por usuario"
if errorlevel 1 (
    echo [!] NOTA: Puede que no haya cambios nuevos o ya este commiteado
)
echo.
echo ================================================================
echo.

echo [5/5] Subiendo a GitHub...
echo.
echo IMPORTANTE: Si pide password, usa tu TOKEN de GitHub (no tu password)
echo.
echo Para crear token: https://github.com/settings/tokens
echo.
git push origin main
if errorlevel 1 (
    echo.
    echo [X] ERROR al subir a GitHub
    echo.
    echo Posibles causas:
    echo   1. No tienes token de GitHub configurado
    echo   2. Credenciales incorrectas
    echo   3. No tienes permisos en el repositorio
    echo.
    echo SOLUCION:
    echo   1. Ve a: https://github.com/settings/tokens
    echo   2. Crea un nuevo token (classic)
    echo   3. Selecciona permisos: repo (todos)
    echo   4. Copia el token
    echo   5. Usa el token como password cuando Git lo pida
    echo.
    pause
    exit /b 1
)
echo.
echo ================================================================
echo.

echo [OK] PROYECTO SUBIDO EXITOSAMENTE
echo.
echo Verifica en: https://github.com/davirock01/man
echo.
echo ================================================================
echo.
pause


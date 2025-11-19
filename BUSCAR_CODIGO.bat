@echo off
REM ================================================================
REM BUSCAR CODIGO EN TODOS LOS WORKTREES DE CURSOR
REM ================================================================

echo.
echo ================================================================
echo  BUSCANDO CODIGO EN TODOS LOS WORKTREES...
echo ================================================================
echo.

set WORKTREES_PATH=c:\Users\User-PC\.cursor\worktrees\man

echo Buscando en: %WORKTREES_PATH%
echo.

REM Verificar si la ruta existe
if not exist "%WORKTREES_PATH%" (
    echo ERROR: No se encuentra la carpeta de worktrees
    echo Ruta: %WORKTREES_PATH%
    pause
    exit /b 1
)

echo CARPETAS ENCONTRADAS:
echo ================================================================
dir /b /ad "%WORKTREES_PATH%"
echo ================================================================
echo.

echo Verificando cada carpeta por codigo...
echo.

for /d %%i in ("%WORKTREES_PATH%\*") do (
    echo.
    echo [Verificando] %%~ni
    echo ----------------------------------------------------------------
    
    REM Verificar backend
    if exist "%%i\backend\" (
        echo   [OK] ENCONTRADO: backend/
        if exist "%%i\backend\docker-compose.yml" (
            echo   [OK] ENCONTRADO: backend/docker-compose.yml
        )
        if exist "%%i\backend\app\" (
            echo   [OK] ENCONTRADO: backend/app/
        )
    ) else (
        echo   [X] NO EXISTE: backend/
    )
    
    REM Verificar frontend
    if exist "%%i\frontend-web\" (
        echo   [OK] ENCONTRADO: frontend-web/
        if exist "%%i\frontend-web\package.json" (
            echo   [OK] ENCONTRADO: frontend-web/package.json
        )
    ) else (
        echo   [X] NO EXISTE: frontend-web/
    )
    
    REM Verificar mobile
    if exist "%%i\mobile-app\" (
        echo   [OK] ENCONTRADO: mobile-app/
        if exist "%%i\mobile-app\package.json" (
            echo   [OK] ENCONTRADO: mobile-app/package.json
        )
    ) else (
        echo   [X] NO EXISTE: mobile-app/
    )
    
    echo ----------------------------------------------------------------
)

echo.
echo ================================================================
echo  BUSQUEDA COMPLETADA
echo ================================================================
echo.
echo Si encontraste codigo en otra carpeta:
echo   1. Anota el nombre de la carpeta
echo   2. Abre esa carpeta en Windows Explorer
echo   3. Copia las carpetas backend, frontend-web, mobile-app
echo   4. Pegalas en el workspace actual (6e9eC)
echo.
echo Workspace actual: %CD%
echo.
pause


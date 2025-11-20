@echo off
chcp 65001 >nul
echo ============================================
echo  🔄 ACTUALIZAR PROYECTO - SINCRONIZACIÓN
echo ============================================
echo.

REM Verificar si estamos en un repositorio Git
git status >nul 2>&1
if errorlevel 1 (
    echo ❌ Este no es un repositorio Git
    echo 💡 Primero ejecuta: SUBIR_A_GITHUB_FACIL.bat
    pause
    exit /b 1
)

echo 📥 Descargando cambios del equipo...
git pull

if errorlevel 1 (
    echo.
    echo ⚠️  Hay conflictos que resolver manualmente
    echo.
    echo 🔧 PASOS PARA RESOLVER:
    echo 1. Abre los archivos con conflictos
    echo 2. Busca las marcas: ^<^<^<^<^<^<^<, =======, ^>^>^>^>^>^>^>
    echo 3. Decide qué código mantener
    echo 4. Guarda los archivos
    echo 5. Ejecuta:
    echo    git add .
    echo    git commit -m "Resolver conflictos"
    echo    git push
    echo.
    pause
    exit /b 1
)

echo ✅ Proyecto actualizado
echo.

set /p CAMBIOS="¿Hiciste cambios que quieras subir? (S/N): "
if /i "%CAMBIOS%"=="S" (
    echo.
    echo 📝 Archivos modificados:
    git status -s
    echo.
    
    set /p MENSAJE="Describe tus cambios: "
    
    echo.
    echo 📦 Agregando archivos...
    git add .
    
    echo 💾 Guardando cambios...
    git commit -m "%MENSAJE%"
    
    echo 🚀 Subiendo a GitHub...
    git push
    
    if errorlevel 1 (
        echo ❌ Error al subir cambios
        echo 💡 Intenta hacer git pull primero
        pause
        exit /b 1
    )
    
    echo ✅ Cambios subidos correctamente
) else (
    echo ℹ️  No hay cambios para subir
)

echo.
echo ============================================
echo  ✅ SINCRONIZACIÓN COMPLETA
echo ============================================
echo.
echo 💡 TIP: Ejecuta este script al iniciar y terminar tu jornada
echo.

pause


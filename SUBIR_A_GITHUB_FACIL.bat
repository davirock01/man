@echo off
chcp 65001 >nul
echo ============================================
echo  🚀 SUBIR PROYECTO A GITHUB - AUTOMÁTICO
echo ============================================
echo.

REM Verificar si Git está instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git no está instalado
    echo 📥 Descárgalo de: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo ✅ Git detectado
echo.

REM Verificar si ya existe un remote
git remote get-url origin >nul 2>&1
if not errorlevel 1 (
    echo ⚠️  Ya existe una conexión a GitHub
    echo 📍 URL actual:
    git remote get-url origin
    echo.
    set /p CONTINUAR="¿Quieres continuar de todas formas? (S/N): "
    if /i not "%CONTINUAR%"=="S" (
        echo ❌ Operación cancelada
        pause
        exit /b 0
    )
)

echo.
echo ============================================
echo  PASO 1: CONFIGURAR GIT (SI NO LO HAS HECHO)
echo ============================================
echo.

set /p CONFIGURAR="¿Ya configuraste tu nombre y email en Git? (S/N): "
if /i "%CONFIGURAR%"=="N" (
    echo.
    set /p NOMBRE="Ingresa tu nombre: "
    set /p EMAIL="Ingresa tu email: "
    
    git config --global user.name "%NOMBRE%"
    git config --global user.email "%EMAIL%"
    
    echo ✅ Git configurado correctamente
)

echo.
echo ============================================
echo  PASO 2: HACER PRIMER COMMIT
echo ============================================
echo.

echo 📦 Agregando archivos al repositorio...
git add .

echo 💾 Creando commit inicial...
git commit -m "Primer commit - Proyecto completo con backend, frontend y mobile"

if errorlevel 1 (
    echo ⚠️  No hay cambios para hacer commit o ya se hizo el commit inicial
)

echo.
echo ============================================
echo  PASO 3: CREAR REPOSITORIO EN GITHUB
echo ============================================
echo.
echo 📝 INSTRUCCIONES:
echo.
echo 1. Ve a: https://github.com/new
echo 2. Nombre del repositorio: nombre-de-tu-app
echo 3. Marca como PRIVADO
echo 4. NO marques "Add a README"
echo 5. Click en "Create repository"
echo.
echo 6. COPIA el comando que dice:
echo    git remote add origin https://github.com/TU-USUARIO/tu-repo.git
echo.

pause

echo.
set /p REPO_URL="Pega aquí la URL del repositorio (https://github.com/...): "

REM Eliminar remote anterior si existe
git remote remove origin >nul 2>&1

echo 🔗 Conectando con GitHub...
git remote add origin %REPO_URL%

if errorlevel 1 (
    echo ❌ Error al conectar con GitHub
    echo ⚠️  Verifica que la URL sea correcta
    pause
    exit /b 1
)

echo.
echo ============================================
echo  PASO 4: SUBIR CÓDIGO A GITHUB
echo ============================================
echo.

echo 🚀 Subiendo código...
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ Error al subir el código
    echo.
    echo 🔧 POSIBLES SOLUCIONES:
    echo 1. Verifica tu conexión a internet
    echo 2. Asegúrate de estar autenticado en GitHub
    echo 3. Usa un Personal Access Token en lugar de contraseña
    echo    Crear token: https://github.com/settings/tokens
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo  ✅ ¡PROYECTO SUBIDO EXITOSAMENTE!
echo ============================================
echo.
echo 📍 Tu repositorio está en: %REPO_URL%
echo.
echo 👥 SIGUIENTE PASO: INVITAR COLABORADORES
echo.
echo 1. Ve a tu repositorio en GitHub
echo 2. Click en "Settings"
echo 3. Click en "Collaborators"
echo 4. Click en "Add people"
echo 5. Ingresa el usuario o email de tus colaboradores
echo 6. Dales permiso "Admin" o "Write"
echo.
echo 📧 Ellos recibirán un email de invitación
echo.
echo 📖 Comparte con ellos el archivo:
echo    GUIA_COLABORACION_COMPLETA.md
echo.

pause


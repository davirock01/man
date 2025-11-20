@echo off
chcp 65001 >nul
echo ============================================
echo  VERIFICACIÓN DE COLABORADORES
echo ============================================
echo.
echo 📥 Descargando últimos cambios...
git pull
echo.
echo ============================================
echo  REVISANDO ARCHIVOS DE ACCESO
echo ============================================
echo.

echo 🔍 Buscando colaboradores...
echo.

REM Colaborador 1 (USA)
if exist PRUEBA_USA.txt (
    echo ✅ COLABORADOR 1 (USA): CONFIRMADO
    echo    Archivo: PRUEBA_USA.txt
) else (
    echo ❌ COLABORADOR 1 (USA): NO ENCONTRADO
)
echo.

REM Colaborador 2
if exist ACCESO_COLABORADOR_2.txt (
    echo ✅ COLABORADOR 2: CONFIRMADO
    echo    Archivo: ACCESO_COLABORADOR_2.txt
    echo    Contenido:
    type ACCESO_COLABORADOR_2.txt
) else (
    echo ⏳ COLABORADOR 2: AÚN NO HA SUBIDO SU ARCHIVO
)
echo.

REM Colaborador 3
if exist ACCESO_COLABORADOR_3.txt (
    echo ✅ COLABORADOR 3: CONFIRMADO
    echo    Archivo: ACCESO_COLABORADOR_3.txt
    echo    Contenido:
    type ACCESO_COLABORADOR_3.txt
) else (
    echo ⏳ COLABORADOR 3: AÚN NO HA SUBIDO SU ARCHIVO
)
echo.

echo ============================================
echo  RESUMEN
echo ============================================
echo.

set count=0
if exist PRUEBA_USA.txt set /a count+=1
if exist ACCESO_COLABORADOR_2.txt set /a count+=1
if exist ACCESO_COLABORADOR_3.txt set /a count+=1

echo Total de colaboradores verificados: %count% de 3
echo.

if %count%==3 (
    echo 🎉 ¡TODOS LOS COLABORADORES CONFIRMADOS!
    echo 🚀 Listos para trabajar en equipo
) else (
    echo ⏳ Esperando confirmación de algunos colaboradores
    echo 💡 Ejecuta este script nuevamente después de que respondan
)

echo.
echo ============================================
pause


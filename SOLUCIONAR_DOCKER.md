# 🔧 SOLUCIÓN: Docker Desktop No Está Corriendo

**Error**: `The system cannot find the file specified` en la pipe de Docker

---

## 🎯 SOLUCIÓN (3 PASOS)

### PASO 1: Iniciar Docker Desktop

1. Busca en Windows "Docker Desktop"
2. Haz clic para abrirlo
3. **ESPERA 30-60 segundos** hasta que el ícono de Docker en la barra de tareas deje de parpadear
4. El ícono debe estar **QUIETO** (sin animación)

### PASO 2: Verificar que Docker está listo

Abre CMD o PowerShell y ejecuta:

```bash
docker ps
```

**Resultado esperado**:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
(vacío está bien)
```

**SI DA ERROR**: Docker Desktop todavía no está listo. Espera 1-2 minutos más.

### PASO 3: Reintentar el script

```
Doble clic en: INICIO_RAPIDO.bat
```

Ahora debería funcionar.

---

## 🔄 SI DOCKER DESKTOP NO INICIA

### Opción A: Reinstalar Docker Desktop

1. Desinstalar Docker Desktop
2. Descargar de: https://www.docker.com/products/docker-desktop
3. Instalar
4. Reiniciar PC
5. Iniciar Docker Desktop

### Opción B: Iniciar servicios manualmente (Sin Docker)

Si Docker da problemas, puedes instalar PostgreSQL local:

1. Descargar PostgreSQL: https://www.postgresql.org/download/windows/
2. Instalar con password: `postgres`
3. Crear base de datos `fleet_maintenance`
4. Ejecutar el SQL: `backend/app/db/init_db.sql`
5. Iniciar backend manualmente:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

---

## ✅ VERIFICACIÓN RÁPIDA

### ¿Está Docker Desktop corriendo?

Mira la barra de tareas de Windows (abajo derecha):
- ✅ Icono de ballena (Docker) **quieto** = Docker listo
- ⏳ Icono de ballena **parpadeando** = Docker iniciando
- ❌ No hay ícono = Docker no está corriendo

---

## 📞 PRÓXIMO PASO

1. **Inicia Docker Desktop**
2. **Espera que esté listo** (1-2 minutos)
3. **Ejecuta**: `INICIO_RAPIDO.bat` otra vez

**Debería funcionar** ✅

---

**Agente 4 - Technical Lead & Supervisor**


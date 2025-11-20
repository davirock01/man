# 📤 GUÍA PASO A PASO - SUBIR PROYECTO A GITHUB

**Repositorio**: https://github.com/davirock01/man.git  
**Estado actual**: Git configurado pero archivos sin subir

---

## ✅ PASO 1: Verificar Estado Actual

Abre PowerShell o CMD:

```powershell
cd "C:\Users\User-PC\Desktop\software engineering\app\man"
git status
```

Esto muestra qué archivos faltan por subir.

---

## ✅ PASO 2: Agregar TODOS los Archivos

Ejecuta:

```powershell
git add .
```

Este comando agrega **TODOS** los archivos del proyecto al staging area.

**Verifica que se agregaron**:
```powershell
git status
```

Deberías ver muchos archivos en verde con "Changes to be committed".

---

## ✅ PASO 3: Hacer Commit

Ejecuta:

```powershell
git commit -m "Implementación completa: Backend + Frontend + Control de roles"
```

Esto guarda los cambios localmente con un mensaje descriptivo.

**Verifica el commit**:
```powershell
git log --oneline
```

Deberías ver tu commit.

---

## ✅ PASO 4: Subir a GitHub

Ejecuta:

```powershell
git push origin main
```

Esto sube TODOS los archivos a GitHub.

**Si pide credenciales**:
- Usuario: `davirock01`
- Password: Tu token de GitHub (no tu password normal)

---

## ✅ PASO 5: Verificar en GitHub

1. Abre tu navegador
2. Ve a: https://github.com/davirock01/man
3. Deberías ver todos tus archivos subidos

---

## 🔐 SI PIDE TOKEN DE GITHUB

Si Git pide password y no funciona, necesitas un **Personal Access Token**:

### Crear Token:
1. Ve a: https://github.com/settings/tokens
2. Clic en "Generate new token" → "Generate new token (classic)"
3. Dale un nombre: "Fleet Maintenance App"
4. Selecciona permisos: 
   - ✅ `repo` (todos los sub-items)
5. Clic en "Generate token"
6. **COPIA EL TOKEN** (solo se muestra una vez)
7. Úsalo como password cuando Git lo pida

---

## 🚨 SI HAY ERROR "Authentication failed"

**Solución**:

```powershell
# Verificar credenciales configuradas
git config user.name
git config user.email

# Si están vacías, configúralas:
git config user.name "davirock01"
git config user.email "tu-email@example.com"

# Intentar push de nuevo
git push origin main
```

---

## 📋 RESUMEN DE COMANDOS (COPY-PASTE)

```powershell
# 1. Navegar al proyecto
cd "C:\Users\User-PC\Desktop\software engineering\app\man"

# 2. Agregar todos los archivos
git add .

# 3. Verificar
git status

# 4. Hacer commit
git commit -m "Implementación completa: Backend + Frontend + Control de roles"

# 5. Subir a GitHub
git push origin main

# 6. Verificar
git log --oneline
```

---

## ✅ VERIFICACIÓN FINAL

Después de hacer push, verifica en:
https://github.com/davirock01/man

Deberías ver:
- ✅ Carpeta `man/` con todos los archivos
- ✅ Carpeta `backend/` 
- ✅ Carpeta `frontend-web/`
- ✅ Carpeta `docs/`
- ✅ Tu commit más reciente

---

## 📝 DESCRIPCIÓN SUGERIDA PARA GITHUB

Agrega un README.md en la raíz si no existe:

```markdown
# Fleet Maintenance System

Sistema de mantenimiento preventivo y correctivo para flotas vehiculares.

## Tecnologías
- Backend: FastAPI + PostgreSQL + Redis
- Frontend: React + TypeScript + Vite
- Contenedores: Docker

## Inicio Rápido

Ver: `man/GUIA_DEFINITIVA_ABRIR_APP.md`

## Credenciales de Prueba
- Coordinador: coordinador@test.com / testpass123
- Conductor: conductor@test.com / testpass123
- Técnico: tecnico@test.com / testpass123
- Admin: admin@test.com / testpass123
```

---

**Ejecuta los comandos del "Resumen de Comandos" y listo.** 🚀


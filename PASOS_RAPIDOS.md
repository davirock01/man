# ⚡ PASOS RÁPIDOS - CONFIGURACIÓN COLABORATIVA

## 🎯 PARA TI (Administrador - México)

### **CONFIGURACIÓN INICIAL (Solo 1 vez)**

1. **Ejecuta el script automático:**
   ```
   Doble click en: SUBIR_A_GITHUB_FACIL.bat
   ```
   
   El script te guiará para:
   - ✅ Configurar Git
   - ✅ Crear primer commit
   - ✅ Conectar con GitHub
   - ✅ Subir el código

2. **Invitar colaboradores en GitHub:**
   - Ve a tu repositorio en GitHub
   - Settings → Collaborators → Add people
   - Ingresa el usuario/email de cada colaborador
   - Dales permiso **"Admin"** o **"Write"**

3. **Compartir con tus colaboradores:**
   - 📧 Envíales el archivo: `INSTRUCCIONES_PARA_USA.md`
   - 🔑 Envíales las API keys de forma segura (NO por Git)
   - 🔗 Envíales el link del repositorio

---

### **USO DIARIO**

**Cada vez que trabajes en el proyecto:**

```
Doble click en: ACTUALIZAR_PROYECTO.bat
```

Este script:
- ⬇️ Descarga cambios del equipo
- ⬆️ Sube tus cambios
- 🔄 Mantiene todo sincronizado

---

## 🇺🇸 PARA COLABORADORES (USA)

### **CONFIGURACIÓN INICIAL (Solo 1 vez)**

1. **Aceptar invitación:**
   - Revisar email de GitHub
   - Click en "Accept invitation"

2. **Clonar el proyecto:**
   ```bash
   git clone https://github.com/USUARIO/REPO.git
   cd REPO
   ```

3. **Instalar dependencias:**
   ```bash
   # Backend
   cd backend
   pip install -r requirements.txt
   
   # Frontend
   cd frontend-web
   npm install
   ```

4. **Configurar .env:**
   - Solicitar API keys al administrador
   - Crear archivo `.env` con las credenciales

5. **Iniciar aplicación:**
   ```bash
   docker-compose up -d
   ```

---

### **USO DIARIO**

**Antes de trabajar:**
```bash
git pull
```

**Después de trabajar:**
```bash
git add .
git commit -m "Descripción de cambios"
git push
```

---

## 🚨 COMANDOS DE EMERGENCIA

### **Si algo sale mal:**

```bash
# Ver estado actual
git status

# Descartar cambios locales
git reset --hard HEAD

# Forzar actualización desde GitHub
git fetch origin
git reset --hard origin/main

# Ver historial de commits
git log --oneline

# Volver a un commit anterior (cuidado!)
git reset --hard COMMIT_ID
```

---

## ✅ CHECKLIST DE ÉXITO

### Administrador (México):
- [ ] ✅ Git configurado
- [ ] ✅ Proyecto subido a GitHub
- [ ] ✅ Colaboradores invitados
- [ ] ✅ API keys compartidas (de forma segura)
- [ ] ✅ Scripts funcionando correctamente

### Colaboradores (USA):
- [ ] ✅ Invitación aceptada
- [ ] ✅ Proyecto clonado
- [ ] ✅ Dependencias instaladas
- [ ] ✅ Aplicación corriendo
- [ ] ✅ Primer commit exitoso

---

## 📚 DOCUMENTACIÓN COMPLETA

- **GUIA_COLABORACION_COMPLETA.md** - Guía detallada en español
- **INSTRUCCIONES_PARA_USA.md** - Quick guide in English
- **SUBIR_A_GITHUB_FACIL.bat** - Script de configuración inicial
- **ACTUALIZAR_PROYECTO.bat** - Script de sincronización diaria

---

## 🎉 ¡TODO LISTO!

Con estos pasos, tu equipo tendrá acceso total al proyecto y podrán colaborar sin problemas.

**¿Preguntas? Revisa la guía completa o consulta con el administrador.**


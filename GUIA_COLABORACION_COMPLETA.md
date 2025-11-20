# 🌎 GUÍA COMPLETA DE COLABORACIÓN - USA 🇺🇸

## 📌 INSTRUCCIONES PARA COMPARTIR EL WORKSPACE CON ACCESO TOTAL

---

## 👤 PARA TI (Administrador - México)

### **1️⃣ INICIALIZAR GIT** (Primera vez solamente)

Abre PowerShell en la carpeta del proyecto (`C:\Users\User-PC\Desktop\app`) y ejecuta:

```powershell
# Configurar tu identidad en Git (si no lo has hecho)
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Inicializar el repositorio
git init

# Agregar todos los archivos
git add .

# Hacer el primer commit
git commit -m "Primer commit - Proyecto completo"
```

---

### **2️⃣ CREAR REPOSITORIO EN GITHUB**

#### **Opción A: Desde la web (MÁS FÁCIL)**

1. Ve a: https://github.com/new
2. Nombre del repositorio: `nombre-de-tu-app`
3. Descripción: `Sistema de mantenimiento vehicular`
4. **Selecciona: PRIVATE** (para que sea privado)
5. **NO marques**: "Add a README file"
6. Click en **"Create repository"**

7. Copia el comando que aparece (algo así):
```powershell
git remote add origin https://github.com/TU-USUARIO/nombre-de-tu-app.git
git branch -M main
git push -u origin main
```

#### **Opción B: Desde la terminal** (Requiere GitHub CLI)

```powershell
# Instalar GitHub CLI (si no lo tienes)
winget install --id GitHub.cli

# Autenticarte
gh auth login

# Crear repositorio privado
gh repo create nombre-de-tu-app --private --source=. --push
```

---

### **3️⃣ DAR ACCESO A TUS COLABORADORES EN USA**

1. Ve a tu repositorio en GitHub
2. Click en **"Settings"** (arriba a la derecha)
3. En el menú izquierdo, click en **"Collaborators"**
4. Click en **"Add people"**
5. Ingresa el **nombre de usuario de GitHub** o **email** de tus colaboradores
6. Selecciona el nivel de acceso: **"Write"** o **"Admin"**
   - **Write**: Pueden hacer push, pull, crear branches
   - **Admin**: Acceso total (recomendado para tu equipo)
7. Click en **"Add [usuario] to this repository"**
8. Ellos recibirán un email de invitación

**🔑 IMPORTANTE:** Comparte con ellos:
- El link del repositorio: `https://github.com/TU-USUARIO/nombre-de-tu-app`
- La invitación que les llegará por email

---

### **4️⃣ SUBIR CAMBIOS (Cada vez que trabajes)**

```powershell
# Ver qué archivos cambiaron
git status

# Agregar archivos modificados
git add .

# Hacer commit con mensaje descriptivo
git commit -m "Descripción de los cambios"

# Subir a GitHub
git push
```

---

## 👥 PARA TUS COLABORADORES EN USA

### **1️⃣ ACEPTAR LA INVITACIÓN**

1. Revisar el email de GitHub
2. Click en **"Accept invitation"**
3. O ir directamente al repositorio y aceptar desde ahí

---

### **2️⃣ CLONAR EL REPOSITORIO**

```bash
# Navegar a donde quieren guardar el proyecto
cd ~/Documents  # o la carpeta que prefieran

# Clonar el repositorio
git clone https://github.com/TU-USUARIO/nombre-de-tu-app.git

# Entrar al proyecto
cd nombre-de-tu-app
```

---

### **3️⃣ INSTALAR DEPENDENCIAS**

#### **Backend (Python)**
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r backend/requirements.txt
```

#### **Frontend (React/TypeScript)**
```bash
cd frontend-web
npm install
# o
yarn install
```

#### **Mobile App (React Native)**
```bash
cd mobile-app
npm install
# o
yarn install
```

---

### **4️⃣ CONFIGURAR VARIABLES DE ENTORNO**

Crear archivo `.env` en la raíz del proyecto con:

```env
# Base de datos
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db

# API Keys (solicitar al administrador)
OPENAI_API_KEY=tu-key-aqui
CLAUDE_API_KEY=tu-key-aqui

# JWT Secret
SECRET_KEY=tu-secret-key-aqui
```

**⚠️ IMPORTANTE:** Solicita las API keys al administrador (México)

---

### **5️⃣ TRABAJAR EN EL PROYECTO**

```bash
# SIEMPRE antes de empezar, descargar cambios
git pull

# Hacer tus modificaciones en los archivos...

# Ver qué cambió
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción clara de lo que hiciste"

# Subir cambios
git push
```

---

## 🔄 FLUJO DE TRABAJO COLABORATIVO

### **✅ BUENAS PRÁCTICAS**

1. **SIEMPRE hacer `git pull` antes de empezar a trabajar**
2. **Hacer commits frecuentes** con mensajes descriptivos
3. **Hacer push regularmente** para que todos vean tus cambios
4. **Comunicarse** cuando estén trabajando en los mismos archivos

### **📝 MENSAJES DE COMMIT CLAROS**

```bash
# ❌ MAL
git commit -m "cambios"
git commit -m "fix"

# ✅ BIEN
git commit -m "Agregar validación de usuario en login"
git commit -m "Corregir error en cálculo de mantenimiento preventivo"
git commit -m "Actualizar interfaz de dashboard"
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS COMUNES

### **❌ Error: "Permission denied"**
**Solución:** Verifica que aceptaste la invitación al repositorio

### **❌ Error: "Conflict" al hacer push**
```bash
# Descargar cambios del servidor
git pull

# Resolver conflictos manualmente en los archivos
# Buscar las marcas: <<<<<<, ======, >>>>>>

# Después de resolver
git add .
git commit -m "Resolver conflictos"
git push
```

### **❌ Error: "Authentication failed"**
```bash
# Configurar credenciales
git config --global credential.helper store

# Al hacer push, ingresa:
# Usuario: tu-usuario-github
# Password: tu-token-personal (NO tu contraseña)
```

**Crear token personal:** https://github.com/settings/tokens

---

## 🚀 INICIAR LA APLICACIÓN

### **Backend**
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### **Frontend**
```bash
cd frontend-web
npm run dev
# o
yarn dev
```

### **Con Docker (Recomendado)**
```bash
docker-compose up -d
```

---

## 📞 CONTACTO Y COORDINACIÓN

**Zona Horaria:**
- México (Central Time): UTC-6
- USA (Eastern Time): UTC-5
- USA (Pacific Time): UTC-8

**💡 Sugerencia:** Usar herramientas de comunicación:
- **Slack** / **Discord** para mensajes
- **GitHub Issues** para bugs y tareas
- **GitHub Projects** para organizar el trabajo

---

## 🔒 SEGURIDAD

### **⚠️ NUNCA SUBIR A GIT:**
- API Keys
- Contraseñas
- Archivos `.env`
- Tokens de acceso
- Certificados privados

### **✅ ARCHIVO .gitignore YA ESTÁ CONFIGURADO**
El archivo `.gitignore` ya protege estos archivos sensibles.

---

## 📚 RECURSOS ÚTILES

- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **GitHub Docs:** https://docs.github.com/
- **Visual Studio Code:** Instalar extensión "GitLens" para ver cambios

---

## ✅ CHECKLIST DE CONFIGURACIÓN

### Para el Administrador (México):
- [ ] Git configurado
- [ ] Repositorio creado en GitHub
- [ ] Colaboradores invitados
- [ ] Primer commit y push realizado
- [ ] API keys compartidas de forma segura (NO por Git)

### Para Colaboradores (USA):
- [ ] Invitación aceptada
- [ ] Repositorio clonado
- [ ] Dependencias instaladas
- [ ] Variables de entorno configuradas
- [ ] Aplicación corriendo localmente
- [ ] Primer commit de prueba exitoso

---

## 🎯 ¡LISTO PARA COLABORAR!

Una vez completados todos los pasos, tanto tú como tus colaboradores podrán:
- ✅ Ver todos los archivos del proyecto
- ✅ Hacer modificaciones
- ✅ Subir cambios
- ✅ Descargar cambios de otros
- ✅ Trabajar simultáneamente sin perder trabajo

**¡Buen trabajo en equipo! 🚀**


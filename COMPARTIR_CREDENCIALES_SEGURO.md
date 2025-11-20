# 🔒 GUÍA: COMPARTIR CREDENCIALES DE FORMA SEGURA

## ⚠️ IMPORTANTE

**NUNCA subas estas credenciales a GitHub:**
- ❌ API Keys (OpenAI, Claude, etc.)
- ❌ Contraseñas de base de datos
- ❌ JWT Secrets
- ❌ Tokens de acceso
- ❌ Certificados privados

El archivo `.gitignore` ya está configurado para proteger archivos `.env`, pero siempre verifica.

---

## ✅ MÉTODOS SEGUROS PARA COMPARTIR CREDENCIALES

### **OPCIÓN 1: Servicios de Mensajes Encriptados (RECOMENDADO)**

#### **A) Signal** (Más seguro)
- Descarga: https://signal.org/
- Encriptación end-to-end
- Los mensajes se autodestruyen
- Ideal para equipos pequeños

#### **B) WhatsApp Business**
- Disponible para equipos
- Encriptación end-to-end
- Familiar para todos

#### **C) Telegram Secret Chat**
- Usar "Secret Chat" (NO chat normal)
- Encriptación end-to-end
- Timer de autodestrucción

**📝 CÓMO COMPARTIR:**
```
Hola equipo, aquí están las credenciales del proyecto:

# Backend
DATABASE_URL=postgresql://user:pass@host:5432/db

# API Keys
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
CLAUDE_API_KEY=sk-ant-xxxxxxxxxxxxx

# JWT
SECRET_KEY=xxxxxxxxxxxxx

Por favor:
1. Guárdenlas en su archivo .env local
2. NO las suban a Git
3. Eliminen este mensaje después de copiarlas
```

---

### **OPCIÓN 2: Password Manager Compartido**

#### **A) Bitwarden** (Gratis para equipos pequeños)
- https://bitwarden.com/
- Crear "Organization"
- Compartir "Collections" con el equipo
- Cada miembro descarga las credenciales

#### **B) 1Password** (Pago)
- https://1password.com/
- Vaults compartidos
- Control de acceso por usuario

#### **C) LastPass** (Freemium)
- https://www.lastpass.com/
- Carpetas compartidas
- Límite en versión gratis

---

### **OPCIÓN 3: Variables de Entorno Encriptadas (Para Producción)**

#### **GitHub Secrets** (Para CI/CD)
```bash
# Configurar en GitHub
Settings → Secrets and variables → Actions → New repository secret

# Usar en workflows
${{ secrets.OPENAI_API_KEY }}
```

#### **Herramientas de Gestión de Secretos:**
- **AWS Secrets Manager**
- **Azure Key Vault**
- **Google Cloud Secret Manager**
- **HashiCorp Vault**

---

### **OPCIÓN 4: Archivo Encriptado (Para email)**

#### **Usando 7-Zip (Windows)**
```powershell
# Crear archivo con credenciales
# Archivo: credenciales.txt

# Encriptar con 7-Zip
7z a -p -mhe=on credenciales.7z credenciales.txt

# Enviar por email
# Compartir contraseña por otro medio (WhatsApp, Signal)
```

#### **Usando GPG (Linux/Mac)**
```bash
# Encriptar
gpg -c credenciales.txt

# Enviar credenciales.txt.gpg por email
# Compartir contraseña por otro medio
```

---

## 🎯 MÉTODO RECOMENDADO PARA TU EQUIPO

### **Para Equipos Pequeños (2-5 personas):**

1. **Usar Signal o WhatsApp:**
   - Crear grupo del equipo
   - Compartir credenciales
   - Fijar mensaje con las credenciales
   - Cada miembro las guarda en su `.env` local

2. **Documento Compartido (Última opción):**
   - Google Docs con acceso restringido
   - Solo compartir link con el equipo
   - No marcar como "Anyone with link"
   - Usar "Restricted - Only people added"

---

## 📋 PLANTILLA DE CREDENCIALES PARA COMPARTIR

Copia esto y envíalo de forma segura:

```env
# ===========================================
# CREDENCIALES DEL PROYECTO
# ===========================================
# IMPORTANTE: NO SUBIR A GIT
# ===========================================

# Base de Datos
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_db
DB_USER=usuario_db
DB_PASSWORD=contraseña_db
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nombre_db

# API Keys - IA
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxx
CLAUDE_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxxxxxxx

# Seguridad
SECRET_KEY=tu-secret-key-super-segura-aqui
JWT_SECRET_KEY=tu-jwt-secret-key-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Email (si aplica)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu-email@gmail.com
SMTP_PASSWORD=tu-contraseña-app

# Frontend
VITE_API_URL=http://localhost:8000
VITE_APP_NAME=Sistema Mantenimiento Vehicular

# Otros servicios (según tu proyecto)
AWS_ACCESS_KEY_ID=xxxxxxxxxx
AWS_SECRET_ACCESS_KEY=xxxxxxxxxx
AWS_REGION=us-east-1

# ===========================================
# INSTRUCCIONES:
# ===========================================
# 1. Copia todo este contenido
# 2. Crea un archivo llamado .env en la raíz del proyecto
# 3. Pega este contenido en el archivo
# 4. Guarda el archivo
# 5. Elimina este mensaje del chat
# ===========================================
```

---

## 🔐 MEJORES PRÁCTICAS

### ✅ HACER:
- Usar canales encriptados
- Rotar credenciales periódicamente
- Usar diferentes credenciales para desarrollo/producción
- Verificar que `.gitignore` incluye `.env`
- Eliminar credenciales de chats después de compartir

### ❌ NO HACER:
- Enviar por email sin encriptar
- Subir a GitHub (ni siquiera en repositorios privados)
- Compartir en chats de trabajo no encriptados (Slack sin encriptación)
- Dejar credenciales en mensajes permanentes
- Usar credenciales de producción en desarrollo

---

## 🚨 SI COMPROMETISTE UNA CREDENCIAL

### **Pasos inmediatos:**

1. **Revocar inmediatamente:**
   - API Keys: Regenerar en la consola del proveedor
   - Contraseñas: Cambiar de inmediato
   - Tokens: Invalidar y crear nuevos

2. **Si se subió a Git por error:**
```bash
# CUIDADO: Esto reescribe el historial
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Forzar push (avisar al equipo primero)
git push origin --force --all
```

3. **Notificar al equipo:**
   - Informar que las credenciales cambiaron
   - Compartir las nuevas de forma segura

---

## 📞 CONTACTO DE EMERGENCIA

Si alguien del equipo pierde acceso a las credenciales:
- Contactar al administrador del proyecto
- Verificar identidad antes de compartir
- Compartir por canal seguro

---

## ✅ CHECKLIST DE SEGURIDAD

- [ ] Credenciales compartidas por canal encriptado
- [ ] Archivo `.gitignore` verificado
- [ ] Cada miembro tiene su archivo `.env` local
- [ ] Nadie ha subido credenciales a Git
- [ ] Equipo sabe qué hacer si comprometen una credencial
- [ ] Credenciales de producción separadas de desarrollo

---

## 🎓 RECURSOS ADICIONALES

- **OWASP - Secrets Management:** https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- **GitHub - Removing Sensitive Data:** https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- **Git Guardian:** https://www.gitguardian.com/ (Detecta secretos en repos)

---

**🔒 La seguridad es responsabilidad de todos. ¡Mantén las credenciales seguras!**


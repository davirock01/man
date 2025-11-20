# 🌎 Sistema de Mantenimiento Vehicular - Colaboración Internacional

## 📋 Descripción del Proyecto

Sistema completo de gestión de mantenimiento vehicular con:
- 🔧 Backend API (FastAPI/Python)
- 💻 Frontend Web (React/TypeScript)
- 📱 Aplicación Móvil (React Native)
- 🤖 Integración con IA (OpenAI/Claude)
- 📊 Dashboard de analíticas
- ⚙️ Mantenimiento predictivo

---

## 👥 Colaboración México 🇲🇽 - USA 🇺🇸

Este proyecto está siendo desarrollado colaborativamente entre equipos en México y Estados Unidos.

---

## 🚀 INICIO RÁPIDO

### Para Administrador (Primera vez):
```bash
# Doble click en:
SUBIR_A_GITHUB_FACIL.bat
```

### Para Colaboradores (Primera vez):
```bash
# Ver instrucciones en:
INSTRUCCIONES_PARA_USA.md (English)
GUIA_COLABORACION_COMPLETA.md (Español)
```

### Para Todos (Uso diario):
```bash
# Doble click en:
ACTUALIZAR_PROYECTO.bat
```

---

## 📚 DOCUMENTACIÓN DISPONIBLE

### 🔵 Configuración y Colaboración:
- **`PASOS_RAPIDOS.md`** - Guía rápida de configuración
- **`GUIA_COLABORACION_COMPLETA.md`** - Guía detallada en español
- **`INSTRUCCIONES_PARA_USA.md`** - Quick guide in English
- **`COMPARTIR_CREDENCIALES_SEGURO.md`** - Seguridad de credenciales

### 🔵 Scripts Automatizados:
- **`SUBIR_A_GITHUB_FACIL.bat`** - Configuración inicial de GitHub
- **`ACTUALIZAR_PROYECTO.bat`** - Sincronización diaria

### 🔵 Documentación Técnica:
- **`ARCHITECTURE.md`** - Arquitectura del sistema
- **`GUIA_IMPLEMENTACION.md`** - Guía de implementación
- **`COMO_ABRIR_LA_APP.md`** - Cómo iniciar la aplicación

---

## 🏗️ Estructura del Proyecto

```
app/
├── backend/              # API Backend (FastAPI)
│   ├── app/
│   │   ├── api/         # Endpoints
│   │   ├── core/        # Configuración
│   │   ├── models/      # Modelos de BD
│   │   ├── schemas/     # Schemas Pydantic
│   │   ├── services/    # Lógica de negocio
│   │   └── main.py      # Entry point
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend-web/         # Frontend Web (React)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
│   └── package.json
│
├── mobile-app/          # App Móvil (React Native)
│   ├── src/
│   │   ├── screens/
│   │   ├── components/
│   │   └── services/
│   └── package.json
│
├── docs/                # Documentación
├── man/                 # Scripts y herramientas
└── README.md           # Este archivo
```

---

## 🛠️ Tecnologías

### Backend:
- Python 3.11+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Celery (Jobs)
- Docker

### Frontend:
- React 18
- TypeScript
- Vite
- TailwindCSS
- React Query

### Mobile:
- React Native
- Expo
- TypeScript

### IA/ML:
- OpenAI API
- Claude API
- Scikit-learn

---

## 🔧 Instalación Local

### Prerequisitos:
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- PostgreSQL 15+
- Git

### Con Docker (Recomendado):
```bash
docker-compose up -d
```

### Manual:

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend-web
npm install
npm run dev
```

**Mobile:**
```bash
cd mobile-app
npm install
npm start
```

---

## 🌐 URLs de Desarrollo

- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **Frontend Web:** http://localhost:3000
- **Mobile App:** Expo DevTools

---

## 🔄 Flujo de Trabajo Git

### Antes de trabajar:
```bash
git pull
```

### Después de hacer cambios:
```bash
git add .
git commit -m "Descripción clara de cambios"
git push
```

### Resolver conflictos:
```bash
git pull
# Resolver conflictos en archivos
git add .
git commit -m "Resolver conflictos"
git push
```

---

## 🧪 Testing

### Backend:
```bash
cd backend
pytest
```

### Frontend:
```bash
cd frontend-web
npm test
```

---

## 📦 Deployment

### Producción:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Variables de Entorno:
Crear archivo `.env` (solicitar credenciales al administrador):
```env
DATABASE_URL=postgresql://...
OPENAI_API_KEY=sk-...
CLAUDE_API_KEY=sk-ant-...
SECRET_KEY=...
```

---

## 👥 Equipo

### México 🇲🇽:
- Project Lead & Backend Development
- Infrastructure & DevOps

### USA 🇺🇸:
- Frontend Development
- Mobile Development
- Testing & QA

---

## 📞 Contacto

Para preguntas sobre:
- **Acceso al repositorio:** Administrador del proyecto
- **Credenciales:** Ver `COMPARTIR_CREDENCIALES_SEGURO.md`
- **Bugs/Features:** GitHub Issues
- **Dudas técnicas:** Team Slack/Discord

---

## 📄 Licencia

[Especificar licencia del proyecto]

---

## ✅ Checklist de Onboarding

### Para nuevos colaboradores:
- [ ] Invitación a GitHub aceptada
- [ ] Repositorio clonado
- [ ] Dependencias instaladas (backend)
- [ ] Dependencias instaladas (frontend)
- [ ] Variables de entorno configuradas
- [ ] Base de datos conectada
- [ ] Aplicación corriendo localmente
- [ ] Primer commit de prueba realizado
- [ ] Acceso a canales de comunicación del equipo
- [ ] Documentación leída

---

## 🎯 Estado Actual

- ✅ Backend API operacional
- ✅ Frontend web funcional
- ✅ Mobile app en desarrollo
- ✅ Integración con IA activa
- ✅ Sistema de alertas implementado
- ✅ Dashboard de analíticas funcional

---

## 🚀 Próximos Pasos

1. Completar tests unitarios
2. Optimizar queries de base de datos
3. Mejorar UI/UX mobile
4. Implementar notificaciones push
5. Deploy a producción

---

## 💡 Tips para Colaboración

- 🕐 Respeta las zonas horarias
- 💬 Comunica cambios importantes
- 📝 Documenta decisiones técnicas
- 🧪 Prueba antes de hacer push
- 🤝 Ayuda a tus compañeros

---

**¡Bienvenido al equipo! 🎉**

Para cualquier duda, consulta la documentación o contacta al equipo.


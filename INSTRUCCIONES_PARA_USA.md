# 🇺🇸 QUICK START GUIDE - USA TEAM

## 📥 STEP 1: ACCEPT GITHUB INVITATION

1. Check your email for GitHub invitation
2. Click **"Accept invitation"**

---

## 💻 STEP 2: CLONE THE REPOSITORY

Open terminal (PowerShell, Terminal, or Git Bash) and run:

```bash
# Navigate to your workspace folder
cd ~/Documents
# or wherever you want to store the project

# Clone the repository (replace with actual URL)
git clone https://github.com/USERNAME/repo-name.git

# Enter the project folder
cd repo-name
```

---

## 🔧 STEP 3: INSTALL DEPENDENCIES

### **Backend (Python)**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### **Frontend (React/TypeScript)**

```bash
cd frontend-web
npm install
# or
yarn install
```

### **Mobile App (React Native)**

```bash
cd mobile-app
npm install
# or
yarn install
```

---

## ⚙️ STEP 4: CONFIGURE ENVIRONMENT

Create a `.env` file in the project root:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# API Keys (request from admin)
OPENAI_API_KEY=your-key-here
CLAUDE_API_KEY=your-key-here

# JWT Secret
SECRET_KEY=your-secret-key-here
```

**⚠️ IMPORTANT:** Request API keys from the project admin (México)

---

## 🚀 STEP 5: RUN THE APPLICATION

### **Using Docker (Recommended)**

```bash
docker-compose up -d
```

### **Manual Start**

**Backend:**
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend-web
npm run dev
# or
yarn dev
```

---

## 🔄 DAILY WORKFLOW

### **Before you start working:**

```bash
# ALWAYS pull latest changes first
git pull
```

### **After making changes:**

```bash
# Check what changed
git status

# Add your changes
git add .

# Commit with clear message
git commit -m "Add user authentication feature"

# Push to GitHub
git push
```

---

## 📝 COMMIT MESSAGE EXAMPLES

✅ **GOOD:**
- `Add vehicle health monitoring dashboard`
- `Fix login validation bug`
- `Update maintenance prediction algorithm`

❌ **BAD:**
- `changes`
- `fix`
- `update`

---

## 🆘 TROUBLESHOOTING

### **Error: "Permission denied"**
- Make sure you accepted the GitHub invitation
- Check your SSH keys or use HTTPS with personal access token

### **Error: "Conflict" when pushing**
```bash
# Pull changes first
git pull

# Resolve conflicts in files (look for: <<<<<<, ======, >>>>>>)
# After resolving:
git add .
git commit -m "Resolve merge conflicts"
git push
```

### **Error: "Authentication failed"**
```bash
# Use Personal Access Token instead of password
# Create token at: https://github.com/settings/tokens
```

---

## 🕐 TIME ZONES

- **México (Central Time):** UTC-6
- **USA (Eastern Time):** UTC-5
- **USA (Pacific Time):** UTC-8

---

## ✅ SETUP CHECKLIST

- [ ] GitHub invitation accepted
- [ ] Repository cloned
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] Environment variables configured
- [ ] Application running locally
- [ ] First test commit successful

---

## 📞 NEED HELP?

Contact the project admin in México for:
- API keys
- Database credentials
- Architecture questions
- Access issues

---

## 🎯 YOU'RE ALL SET!

You now have full access to:
- ✅ View and edit all project files
- ✅ Push your changes
- ✅ Pull changes from the team
- ✅ Work simultaneously with others

**Happy coding! 🚀**


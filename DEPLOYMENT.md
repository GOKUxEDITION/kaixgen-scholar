# 🚀 Deployment Guide — KAIxGen Scholar

This guide explains how to deploy KAIxGen Scholar on different platforms.

---

# 🌐 1️⃣ Deploy on Render (Recommended)

## Step 1: Create Account
Go to https://render.com and sign in.

## Step 2: Create New Web Service
- Click **New +**
- Select **Web Service**
- Connect your GitHub repository
- Choose `kaixgen-scholar`

## Step 3: Configure Settings

Runtime:
Python 3

Build Command:
pip install -r requirements.txt

Start Command:
python main.py

## Step 4: Deploy

Click **Create Web Service**

Your app will be live at:

https://your-app-name.onrender.com

---

# 🚂 2️⃣ Deploy on Railway

## Step 1
Go to https://railway.app

## Step 2
- New Project
- Deploy from GitHub
- Select repository

Railway automatically detects Python.

Start command:
python main.py

Your URL:
https://your-app-name.up.railway.app

---

# 🐳 3️⃣ Deploy Using Docker (VPS / Cloud Server)

## Build Docker Image

docker build -t kaixgen-scholar .

## Run Container

docker run -d -p 8000:8000 kaixgen-scholar

---

# 🖥 4️⃣ Deploy on VPS (Ubuntu Server)

## Install Dependencies

sudo apt update
sudo apt install python3 python3-pip git -y

## Clone Repository

git clone https://github.com/GOKUxEDITION/kaixgen-scholar.git
cd kaixgen-scholar

## Install Requirements

pip3 install -r requirements.txt

## Run Project

python3 main.py

(Optional: use screen or tmux to keep running)

---

# ⚙ 5️⃣ Environment Variables (Important)

If your project requires secrets or API keys:

Never hardcode them.

Use:

export VARIABLE_NAME=value

Or configure them inside:
- Render Environment Settings
- Railway Variables
- Docker ENV

---

# 🛡 Production Recommendations

- Use Docker for consistency
- Enable auto-deploy from GitHub
- Monitor logs
- Use environment variables
- Keep dependencies updated
- Add reverse proxy (Nginx) for VPS production

---

# 📦 Future Production Scaling

- Convert to FastAPI or Flask API
- Add Gunicorn for production server
- Use PostgreSQL instead of local DB
- Add CI/CD pipeline
- Enable HTTPS with custom domain

---

KAIxGen Scholar is designed to scale from local testing to production infrastructure.

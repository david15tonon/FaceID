#!/bin/bash

echo "🚀 Setting up FaceID System"

# Check for required tools
command -v node >/dev/null 2>&1 || { echo "❌ Node.js is required but not installed."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 is required but not installed."; exit 1; }
command -v docker >/dev/null 2>&1 || { echo "❌ Docker is required but not installed."; exit 1; }

echo "✅ All required tools found"

# Setup Frontend
echo "📦 Setting up Frontend..."
cd frontend
npm install
cp .env.example .env.local
echo "✅ Frontend setup complete"
cd ..

# Setup Backend
echo "🐍 Setting up Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
echo "✅ Backend setup complete"
deactivate
cd ..

# Setup Streamlit
echo "📊 Setting up Streamlit App..."
cd streamlit-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
echo "✅ Streamlit setup complete"
deactivate
cd ..

# Setup Docker
echo "🐳 Setting up Docker environment..."
cd backend
docker-compose up -d db redis
echo "✅ Docker services started"
cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Update .env files with your configuration"
echo "2. Run database migrations: cd backend && alembic upgrade head"
echo "3. Start frontend: cd frontend && npm run dev"
echo "4. Start backend: cd backend && uvicorn app.main:app --reload"
echo "5. Start streamlit: cd streamlit-app && streamlit run app.py"

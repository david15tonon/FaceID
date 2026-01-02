#!/bin/bash
# Setup script for development environment

echo "Setting up FaceID development environment..."

# Setup frontend
echo "Setting up frontend..."
cd frontend
npm install
cd ..

# Setup backend
echo "Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Setup streamlit app
echo "Setting up streamlit app..."
cd streamlit-app
pip install -r requirements.txt
cd ..

echo "Setup complete!"

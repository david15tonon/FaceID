# Architecture Documentation

## System Architecture

FaceID is built with a microservices architecture:

1. **Frontend** - React/Vite application deployed on Vercel
2. **Backend** - FastAPI Python application for API and ML processing
3. **Streamlit App** - Admin/demo interface for system management

## Technology Stack

- **Frontend**: React, Vite, Tailwind CSS
- **Backend**: Python, FastAPI, SQLAlchemy, OpenCV
- **ML**: face-recognition, OpenCV
- **Database**: SQLite (development), PostgreSQL (production)

# FaceID - Face Recognition System

A comprehensive face recognition system with real-time identity verification, military-grade security, and comprehensive analytics.

## Features

- 🔐 **Secure Authentication** - JWT-based auth with MFA support
- 📷 **Face Enrollment** - Register faces via webcam or upload
- 🔍 **Face Verification** - Real-time identity verification
- 📊 **Analytics Dashboard** - Comprehensive metrics and insights
- 📋 **Audit Logs** - Complete activity tracking
- ⚙️ **Admin Panel** - Streamlit-based management interface
- 🚀 **RESTful API** - Well-documented FastAPI backend
- 💻 **Modern UI** - React-based responsive frontend

## Architecture

The system consists of three main components:

1. **Frontend** - React/Vite application (deployable to Vercel)
2. **Backend** - FastAPI Python server with PostgreSQL
3. **Streamlit App** - Admin dashboard and analytics

## Tech Stack

### Frontend
- React 18
- Vite
- Tailwind CSS
- React Router
- Axios

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- face_recognition (dlib)
- OpenCV

### Streamlit App
- Streamlit
- Plotly
- Pandas

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL
- Redis

### Installation

1. Clone the repository:
```bash
git clone https://github.com/david15tonon/FaceID.git
cd FaceID
```

2. Run setup script:
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

3. Configure environment variables:
   - Update `frontend/.env.local`
   - Update `backend/.env`
   - Update `streamlit-app/.env`

4. Start services with Docker:
```bash
docker-compose up -d
```

5. Run database migrations:
```bash
cd backend
source venv/bin/activate
alembic upgrade head
```

6. Start the applications:

**Frontend:**
```bash
cd frontend
npm run dev
# Available at http://localhost:3000
```

**Backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload
# Available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

**Streamlit App:**
```bash
cd streamlit-app
source venv/bin/activate
streamlit run app.py
# Available at http://localhost:8501
```

## Project Structure

```
face-recognition-system/
├── frontend/              # React application
├── backend/              # FastAPI backend
├── streamlit-app/        # Admin dashboard
├── shared/               # Shared code
├── docs/                 # Documentation
├── scripts/              # Utility scripts
├── .github/              # CI/CD workflows
└── docker-compose.yml    # Docker configuration
```

## Documentation

- [API Reference](docs/api/API_REFERENCE.md)
- [System Architecture](docs/architecture/system_design.md)
- [Database Schema](docs/architecture/database_schema.md)
- [Getting Started Guide](docs/user_guides/getting_started.md)
- [Face Enrollment Guide](docs/user_guides/face_enrollment.md)

## Deployment

### Frontend (Vercel)
```bash
cd frontend
vercel --prod
```

### Backend (Docker)
Build and deploy the Docker container to your cloud provider.

### Streamlit (Streamlit Cloud)
1. Push code to GitHub
2. Connect repository on streamlit.io
3. Set `streamlit-app/app.py` as main file
4. Configure environment variables

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/signup` - User registration
- `GET /api/auth/me` - Get current user

### Faces
- `POST /api/faces/enroll` - Enroll new face
- `POST /api/faces/verify` - Verify face
- `GET /api/faces/user/{user_id}` - Get user faces
- `DELETE /api/faces/{face_id}` - Delete face

### Users, Reports, Logs
- See [API Reference](docs/api/API_REFERENCE.md) for complete documentation

## Testing

Run tests:
```bash
./scripts/run_tests.sh
```

Backend tests only:
```bash
cd backend
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Security

- Passwords hashed with bcrypt
- JWT token authentication
- MFA support
- SQL injection protection via ORM
- Input validation with Pydantic
- HTTPS required in production

## License

MIT License - see [LICENSE](LICENSE) file for details

## Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation
- Review existing issues

## Acknowledgments

- face_recognition library (dlib)
- FastAPI framework
- React community
- Streamlit team

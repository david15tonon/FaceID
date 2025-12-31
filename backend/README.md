# FaceID Backend API

FastAPI-based backend for the FaceID face recognition system.

## Features

- Face recognition using face_recognition library
- User authentication with JWT
- Face enrollment and verification
- PostgreSQL database with SQLAlchemy ORM
- Redis for caching
- RESTful API design
- Comprehensive logging

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis
- face_recognition (dlib)
- OpenCV
- Pillow

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis
- CMake (for dlib)

### Installation

```bash
pip install -r requirements.txt
```

### Configuration

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

### Database Migration

```bash
alembic upgrade head
```

### Development

```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

Interactive docs at `http://localhost:8000/docs`

### Docker

```bash
docker-compose up --build
```

## Project Structure

- `app/api/` - API routes
- `app/models/` - Database models
- `app/schemas/` - Pydantic schemas
- `app/services/` - Business logic
- `app/ml/` - Machine learning components
- `app/core/` - Core configuration
- `app/utils/` - Utility functions
- `tests/` - Test files

## API Endpoints

### Authentication
- POST `/api/auth/login` - User login
- POST `/api/auth/signup` - User registration
- POST `/api/auth/logout` - User logout
- GET `/api/auth/me` - Get current user

### Faces
- POST `/api/faces/enroll` - Enroll new face
- POST `/api/faces/verify` - Verify face
- GET `/api/faces/user/{user_id}` - Get user faces
- DELETE `/api/faces/{face_id}` - Delete face

### Users
- GET `/api/users` - List users
- GET `/api/users/{user_id}` - Get user
- PUT `/api/users/{user_id}` - Update user
- DELETE `/api/users/{user_id}` - Delete user

### Reports & Logs
- GET `/api/reports` - List reports
- GET `/api/logs` - List logs

## Testing

```bash
pytest
```

## License

MIT

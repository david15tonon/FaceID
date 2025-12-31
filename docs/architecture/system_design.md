# System Architecture

## Overview

FaceID is a comprehensive face recognition system built with a microservices architecture consisting of three main components:

1. **Frontend (React/Vite)** - User-facing web application
2. **Backend (FastAPI)** - RESTful API and business logic
3. **Streamlit App** - Admin dashboard and management interface

## Architecture Diagram

```
┌─────────────────┐
│   Users/Admin   │
└────────┬────────┘
         │
    ┌────┴────────────────────┐
    │                         │
┌───▼──────┐         ┌───────▼────┐
│ Frontend │         │ Streamlit  │
│  React   │         │    App     │
└───┬──────┘         └───────┬────┘
    │                        │
    └──────────┬─────────────┘
               │
        ┌──────▼───────┐
        │   Backend    │
        │   FastAPI    │
        └──────┬───────┘
               │
     ┌─────────┼─────────┐
     │         │         │
┌────▼───┐ ┌──▼───┐ ┌──▼────┐
│ PostgreSQL Redis │  ML     │
│  Database │ Cache│ Models  │
└──────────┘ └─────┘ └───────┘
```

## Components

### Frontend
- **Technology**: React 18, Vite, Tailwind CSS
- **Purpose**: User interface for face enrollment and verification
- **Key Features**:
  - User authentication
  - Face capture via webcam
  - Image upload
  - Dashboard with statistics
  - Profile management

### Backend
- **Technology**: FastAPI, SQLAlchemy, face_recognition
- **Purpose**: API server and business logic
- **Key Features**:
  - RESTful API
  - Face detection and encoding
  - Face matching algorithm
  - User management
  - Authentication and authorization
  - Logging and auditing

### Streamlit App
- **Technology**: Streamlit, Plotly
- **Purpose**: Admin interface and analytics
- **Key Features**:
  - System dashboard
  - Face enrollment management
  - Verification logs
  - Analytics and reporting
  - System settings

### Database
- **Technology**: PostgreSQL
- **Purpose**: Persistent data storage
- **Tables**:
  - `users` - User accounts
  - `faces` - Face encodings and metadata
  - `recognition_logs` - Audit trail
  - `reports` - Generated reports

### Cache
- **Technology**: Redis
- **Purpose**: Session management and caching
- **Use Cases**:
  - Session storage
  - Rate limiting
  - Temporary data caching

## Data Flow

### Face Enrollment
1. User captures/uploads face image
2. Frontend sends image to Backend API
3. Backend detects face in image
4. Backend generates 128-dimensional encoding
5. Encoding stored in database
6. Success response returned to frontend

### Face Verification
1. User submits face image for verification
2. Frontend sends image to Backend API
3. Backend generates encoding from image
4. Backend compares against all stored encodings
5. Best match determined by distance calculation
6. Result returned with confidence score

## Security

- **Authentication**: JWT tokens
- **Password Hashing**: bcrypt
- **HTTPS**: TLS/SSL encryption (production)
- **CORS**: Configured for specific origins
- **Input Validation**: Pydantic schemas
- **SQL Injection**: SQLAlchemy ORM protection

## Scalability

- **Horizontal Scaling**: Backend can run multiple instances
- **Load Balancing**: Use nginx or similar
- **Database**: PostgreSQL replication for read scaling
- **Caching**: Redis for frequently accessed data
- **CDN**: For frontend static assets

## Deployment

- **Frontend**: Vercel
- **Backend**: Docker containers on cloud platform
- **Streamlit**: Streamlit Cloud
- **Database**: Managed PostgreSQL (e.g., AWS RDS)
- **Redis**: Managed Redis (e.g., AWS ElastiCache)

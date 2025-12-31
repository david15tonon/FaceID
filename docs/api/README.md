# API Documentation

## Endpoints

### Authentication

#### POST /api/v1/auth/login
Login to the system

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

#### POST /api/v1/auth/register
Register a new user

### Face Recognition

#### POST /api/v1/faces/enroll
Enroll a new face

#### POST /api/v1/faces/verify
Verify a face against enrolled faces

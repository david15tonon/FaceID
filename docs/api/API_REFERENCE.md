# FaceID API Documentation

## Base URL
```
http://localhost:8000/api
```

## Authentication

All authenticated endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### Authentication

#### POST /auth/login
Login with email and password.

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

#### POST /auth/signup
Register a new user.

**Request:**
```json
{
  "name": "John Doe",
  "email": "user@example.com",
  "password": "password123"
}
```

#### GET /auth/me
Get current user information (requires authentication).

### Faces

#### POST /faces/enroll
Enroll a new face (multipart/form-data).

**Parameters:**
- `image`: Image file (JPG, PNG)
- `user_id`: User ID

**Response:**
```json
{
  "success": true,
  "message": "Face enrolled successfully",
  "data": {
    "face_id": 1,
    "user_id": 1
  }
}
```

#### POST /faces/verify
Verify a face against enrolled faces (multipart/form-data).

**Parameters:**
- `image`: Image file (JPG, PNG)

**Response:**
```json
{
  "success": true,
  "user_id": 1,
  "confidence": 0.985,
  "message": "Match found"
}
```

#### GET /faces/user/{user_id}
Get all faces for a specific user.

#### DELETE /faces/{face_id}
Delete a face.

### Users

#### GET /users
List all users (with pagination).

#### GET /users/{user_id}
Get specific user details.

#### PUT /users/{user_id}
Update user information.

#### DELETE /users/{user_id}
Delete a user.

### Reports

#### GET /reports
List all reports.

#### GET /reports/{report_id}
Get specific report.

#### POST /reports/generate
Generate a new report.

### Logs

#### GET /logs
List system logs with optional filtering.

**Query Parameters:**
- `skip`: Number of records to skip
- `limit`: Maximum number of records to return
- `action`: Filter by action type
- `user_id`: Filter by user ID

## Error Responses

All endpoints may return error responses in this format:

```json
{
  "detail": "Error message description"
}
```

Common HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `404`: Not Found
- `500`: Internal Server Error

# Database Schema

## Tables

### users
User accounts table.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| email | VARCHAR | Unique email address |
| name | VARCHAR | Full name |
| hashed_password | VARCHAR | Bcrypt hashed password |
| is_active | BOOLEAN | Account status |
| is_verified | BOOLEAN | Email verification status |
| mfa_enabled | BOOLEAN | MFA status |
| mfa_secret | VARCHAR | MFA secret key (nullable) |
| created_at | TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

**Indexes:**
- PRIMARY KEY (id)
- UNIQUE INDEX (email)

### faces
Face encodings and metadata.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| user_id | INTEGER | Foreign key to users |
| encoding | BYTEA | Face encoding (128-dimensional) |
| image_path | VARCHAR | Path to stored image (nullable) |
| created_at | TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

**Indexes:**
- PRIMARY KEY (id)
- FOREIGN KEY (user_id) REFERENCES users(id)
- INDEX (user_id)

### recognition_logs
Audit trail for all recognition events.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| user_id | INTEGER | Foreign key to users (nullable) |
| action | VARCHAR | Action type (enroll, verify, failed) |
| success | BOOLEAN | Operation success status |
| confidence | FLOAT | Confidence score (nullable) |
| ip_address | VARCHAR | Client IP address (nullable) |
| user_agent | VARCHAR | Client user agent (nullable) |
| created_at | TIMESTAMP | Event timestamp |

**Indexes:**
- PRIMARY KEY (id)
- FOREIGN KEY (user_id) REFERENCES users(id)
- INDEX (user_id)
- INDEX (action)
- INDEX (created_at)

### reports
Generated system reports.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| title | VARCHAR | Report title |
| report_type | VARCHAR | Type (daily, weekly, monthly) |
| content | TEXT | Report content (nullable) |
| created_at | TIMESTAMP | Creation timestamp |

**Indexes:**
- PRIMARY KEY (id)
- INDEX (report_type)
- INDEX (created_at)

## Relationships

```
users (1) ──< (N) faces
users (1) ──< (N) recognition_logs
```

## Migrations

Database migrations are managed using Alembic.

### Create Migration
```bash
alembic revision --autogenerate -m "description"
```

### Apply Migrations
```bash
alembic upgrade head
```

### Rollback
```bash
alembic downgrade -1
```

## Initial Setup

1. Create PostgreSQL database
2. Update DATABASE_URL in .env
3. Run migrations:
```bash
alembic upgrade head
```

## Backup

### Manual Backup
```bash
pg_dump -U user -d facedb > backup.sql
```

### Restore
```bash
psql -U user -d facedb < backup.sql
```

## Performance Optimization

- **Indexes**: Added on frequently queried columns
- **Connection Pooling**: SQLAlchemy connection pool
- **Query Optimization**: Use of selective loading
- **Partitioning**: Consider for large tables (logs)

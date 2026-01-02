#!/bin/bash
# Database migration script

echo "Running database migrations..."

cd backend
alembic upgrade head

echo "Migrations complete!"

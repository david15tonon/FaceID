#!/bin/bash

echo "🧪 Running Tests"

# Backend Tests
echo "Testing Backend..."
cd backend
source venv/bin/activate
pytest
BACKEND_EXIT=$?
deactivate
cd ..

if [ $BACKEND_EXIT -eq 0 ]; then
    echo "✅ Backend tests passed"
else
    echo "❌ Backend tests failed"
    exit 1
fi

echo "✅ All tests passed!"

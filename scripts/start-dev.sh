#!/bin/bash
# Start all services for development

echo "Starting FaceID services..."

# Start backend
echo "Starting backend..."
cd backend
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# Start frontend
echo "Starting frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

# Start streamlit
echo "Starting streamlit..."
cd streamlit-app
streamlit run app.py &
STREAMLIT_PID=$!
cd ..

echo "All services started!"
echo "Backend PID: $BACKEND_PID"
echo "Frontend PID: $FRONTEND_PID"
echo "Streamlit PID: $STREAMLIT_PID"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID $STREAMLIT_PID" EXIT
wait

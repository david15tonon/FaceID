from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import auth, faces, users, reports, logs

app = FastAPI(
    title="FaceID API",
    description="Face Recognition System API",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(faces.router, prefix="/api/faces", tags=["Faces"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])
app.include_router(logs.router, prefix="/api/logs", tags=["Logs"])

@app.get("/")
async def root():
    return {"message": "FaceID API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

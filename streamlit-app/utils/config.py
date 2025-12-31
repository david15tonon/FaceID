# Configuration
import os

class Config:
    API_URL = os.getenv("API_URL", "http://localhost:8000")
    APP_NAME = "FaceID"
    VERSION = "1.0.0"

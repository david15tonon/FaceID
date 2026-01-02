import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration class"""
    
    # API Settings
    API_URL = os.getenv('API_URL', 'http://localhost:8000/api')
    API_KEY = os.getenv('API_KEY', '')
    
    # Camera Settings
    ENABLE_CAMERA = os.getenv('ENABLE_CAMERA', 'true').lower() == 'true'
    
    # Face Recognition Settings
    FACE_RECOGNITION_TOLERANCE = float(os.getenv('FACE_RECOGNITION_TOLERANCE', '0.6'))
    MAX_FACE_DISTANCE = float(os.getenv('MAX_FACE_DISTANCE', '0.6'))
    
    # UI Settings
    PRIMARY_COLOR = os.getenv('PRIMARY_COLOR', '#FF0000')
    SECONDARY_COLOR = os.getenv('SECONDARY_COLOR', '#000000')

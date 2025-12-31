import face_recognition
import numpy as np
from PIL import Image
import io
from typing import Optional


class FaceEncodingService:
    """Face encoding service"""
    
    @staticmethod
    def generate_encoding(image_bytes: bytes) -> Optional[np.ndarray]:
        """
        Generate face encoding from image
        Returns encoding as numpy array or None if no face found
        """
        # Load image
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)
        
        # Generate encoding
        encodings = face_recognition.face_encodings(image_np)
        
        if len(encodings) == 0:
            return None
        
        return encodings[0]
    
    @staticmethod
    def encoding_to_bytes(encoding: np.ndarray) -> bytes:
        """Convert numpy encoding to bytes for storage"""
        return encoding.tobytes()
    
    @staticmethod
    def bytes_to_encoding(encoding_bytes: bytes) -> np.ndarray:
        """Convert bytes back to numpy encoding"""
        return np.frombuffer(encoding_bytes, dtype=np.float64)

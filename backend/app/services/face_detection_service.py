import face_recognition
import numpy as np
from PIL import Image
import io
from typing import List, Optional


class FaceDetectionService:
    """Face detection service"""
    
    @staticmethod
    def detect_faces(image_bytes: bytes) -> List[tuple]:
        """
        Detect faces in an image
        Returns list of face locations (top, right, bottom, left)
        """
        # Load image
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)
        
        # Detect faces
        face_locations = face_recognition.face_locations(image_np)
        return face_locations
    
    @staticmethod
    def has_single_face(image_bytes: bytes) -> bool:
        """Check if image contains exactly one face"""
        face_locations = FaceDetectionService.detect_faces(image_bytes)
        return len(face_locations) == 1

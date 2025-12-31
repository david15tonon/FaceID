import face_recognition
import numpy as np
from typing import List, Tuple


class FaceDetector:
    """Face detection using face_recognition library"""
    
    def __init__(self, model: str = "hog"):
        """
        Initialize face detector
        Args:
            model: 'hog' (faster) or 'cnn' (more accurate)
        """
        self.model = model
    
    def detect(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        Detect faces in image
        Returns list of (top, right, bottom, left) coordinates
        """
        return face_recognition.face_locations(image, model=self.model)
    
    def detect_and_encode(self, image: np.ndarray) -> Tuple[List, List]:
        """
        Detect faces and generate encodings
        Returns (locations, encodings)
        """
        locations = self.detect(image)
        encodings = face_recognition.face_encodings(image, locations)
        return locations, encodings

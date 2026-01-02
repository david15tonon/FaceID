import face_recognition
import numpy as np
from typing import List, Optional, Tuple


class FaceRecognitionService:
    """Face recognition service"""
    
    def __init__(self, tolerance: float = 0.6):
        self.tolerance = tolerance
    
    def compare_faces(
        self,
        known_encodings: List[np.ndarray],
        face_encoding: np.ndarray
    ) -> Tuple[bool, Optional[int], Optional[float]]:
        """
        Compare a face encoding against known encodings
        Returns: (match_found, matched_index, distance)
        """
        if not known_encodings:
            return False, None, None
        
        distances = face_recognition.face_distance(known_encodings, face_encoding)
        min_distance_idx = np.argmin(distances)
        min_distance = distances[min_distance_idx]
        
        if min_distance < self.tolerance:
            confidence = 1 - min_distance
            return True, min_distance_idx, confidence
        
        return False, None, None

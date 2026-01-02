import face_recognition
import numpy as np
from typing import List, Tuple, Optional


class FaceMatcher:
    """Face matching and comparison"""
    
    def __init__(self, tolerance: float = 0.6):
        """
        Initialize face matcher
        Args:
            tolerance: How much distance between faces to consider a match (lower is stricter)
        """
        self.tolerance = tolerance
    
    def compare_faces(
        self,
        known_encodings: List[np.ndarray],
        face_encoding: np.ndarray
    ) -> List[bool]:
        """
        Compare face encoding against list of known encodings
        Returns list of True/False for each comparison
        """
        return face_recognition.compare_faces(
            known_encodings,
            face_encoding,
            tolerance=self.tolerance
        )
    
    def face_distance(
        self,
        known_encodings: List[np.ndarray],
        face_encoding: np.ndarray
    ) -> np.ndarray:
        """
        Calculate distance between face encoding and known encodings
        Lower distance means more similar
        """
        return face_recognition.face_distance(known_encodings, face_encoding)
    
    def find_best_match(
        self,
        known_encodings: List[np.ndarray],
        face_encoding: np.ndarray
    ) -> Tuple[Optional[int], Optional[float]]:
        """
        Find the best matching face
        Returns (index, distance) or (None, None) if no match
        """
        if not known_encodings:
            return None, None
        
        distances = self.face_distance(known_encodings, face_encoding)
        min_idx = np.argmin(distances)
        min_distance = distances[min_idx]
        
        if min_distance < self.tolerance:
            return min_idx, float(min_distance)
        
        return None, None

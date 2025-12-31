import face_recognition
import numpy as np
from typing import Optional, List


class FaceEncoder:
    """Face encoding generator"""
    
    @staticmethod
    def encode_face(image: np.ndarray, face_location: Optional[tuple] = None) -> Optional[np.ndarray]:
        """
        Generate face encoding from image
        Args:
            image: numpy array of image
            face_location: (top, right, bottom, left) or None to detect automatically
        Returns:
            128-dimensional face encoding or None if no face found
        """
        if face_location:
            encodings = face_recognition.face_encodings(image, [face_location])
        else:
            encodings = face_recognition.face_encodings(image)
        
        if len(encodings) == 0:
            return None
        
        return encodings[0]
    
    @staticmethod
    def encode_faces(image: np.ndarray) -> List[np.ndarray]:
        """Encode all faces in image"""
        return face_recognition.face_encodings(image)

import cv2
import numpy as np
from PIL import Image
import io
from typing import Tuple, Optional


def load_image_from_bytes(image_bytes: bytes) -> np.ndarray:
    """Load image from bytes into numpy array"""
    image = Image.open(io.BytesIO(image_bytes))
    return np.array(image)


def resize_image(image: np.ndarray, max_width: int = 800, max_height: int = 800) -> np.ndarray:
    """Resize image while maintaining aspect ratio"""
    height, width = image.shape[:2]
    
    if width > max_width or height > max_height:
        scaling_factor = min(max_width / width, max_height / height)
        new_width = int(width * scaling_factor)
        new_height = int(height * scaling_factor)
        return cv2.resize(image, (new_width, new_height))
    
    return image


def crop_face(image: np.ndarray, face_location: Tuple[int, int, int, int]) -> np.ndarray:
    """Crop face from image given location (top, right, bottom, left)"""
    top, right, bottom, left = face_location
    return image[top:bottom, left:right]


def convert_to_rgb(image: np.ndarray) -> np.ndarray:
    """Convert image to RGB if needed"""
    if len(image.shape) == 2:  # Grayscale
        return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    elif image.shape[2] == 4:  # RGBA
        return cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    return image

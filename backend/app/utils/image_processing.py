# Image processing utilities
import cv2
import numpy as np
from PIL import Image
import base64
from io import BytesIO

def decode_base64_image(base64_string):
    """Decode base64 string to image"""
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    return np.array(image)

def encode_image_to_base64(image):
    """Encode image to base64 string"""
    pil_img = Image.fromarray(image)
    buffered = BytesIO()
    pil_img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

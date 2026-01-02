import os
import shutil
from pathlib import Path
from typing import Optional


class StorageService:
    """File storage service"""
    
    UPLOAD_DIR = Path("uploads")
    
    def __init__(self):
        self.UPLOAD_DIR.mkdir(exist_ok=True)
    
    def save_file(self, file_bytes: bytes, filename: str, subfolder: str = "") -> str:
        """Save file and return path"""
        if subfolder:
            folder = self.UPLOAD_DIR / subfolder
            folder.mkdir(exist_ok=True)
        else:
            folder = self.UPLOAD_DIR
        
        file_path = folder / filename
        
        with open(file_path, "wb") as f:
            f.write(file_bytes)
        
        return str(file_path)
    
    def delete_file(self, file_path: str) -> bool:
        """Delete a file"""
        try:
            os.remove(file_path)
            return True
        except Exception:
            return False
    
    def get_file(self, file_path: str) -> Optional[bytes]:
        """Get file contents"""
        try:
            with open(file_path, "rb") as f:
                return f.read()
        except Exception:
            return None

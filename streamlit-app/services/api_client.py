import requests
import os
from typing import Optional, Dict, Any


class APIClient:
    """Client for interacting with the backend API"""
    
    def __init__(self, base_url: Optional[str] = None, api_key: Optional[str] = None):
        self.base_url = base_url or os.getenv('API_URL', 'http://localhost:8000/api')
        self.api_key = api_key or os.getenv('API_KEY', '')
        self.session = requests.Session()
        
        if self.api_key:
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}'})
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Login to the system"""
        response = self.session.post(
            f"{self.base_url}/auth/login",
            json={'email': email, 'password': password}
        )
        response.raise_for_status()
        return response.json()
    
    def enroll_face(self, image_data, user_id: int) -> Dict[str, Any]:
        """Enroll a face"""
        files = {'image': image_data}
        data = {'user_id': user_id}
        response = self.session.post(
            f"{self.base_url}/faces/enroll",
            files=files,
            data=data
        )
        response.raise_for_status()
        return response.json()
    
    def verify_face(self, image_data) -> Dict[str, Any]:
        """Verify a face"""
        files = {'image': image_data}
        response = self.session.post(
            f"{self.base_url}/faces/verify",
            files=files
        )
        response.raise_for_status()
        return response.json()
    
    def get_logs(self, limit: int = 100) -> Dict[str, Any]:
        """Get system logs"""
        response = self.session.get(
            f"{self.base_url}/logs",
            params={'limit': limit}
        )
        response.raise_for_status()
        return response.json()
    
    def get_reports(self) -> Dict[str, Any]:
        """Get reports"""
        response = self.session.get(f"{self.base_url}/reports")
        response.raise_for_status()
        return response.json()

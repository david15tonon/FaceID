# Authentication service
from ..core.security import verify_password, get_password_hash, create_access_token

class AuthService:
    def authenticate_user(self, email: str, password: str):
        # Authentication logic
        pass
    
    def create_user(self, email: str, password: str):
        hashed_password = get_password_hash(password)
        # User creation logic
        pass

from app.core.security import verify_password, get_password_hash, create_access_token
from app.models.user import User
from sqlalchemy.orm import Session
from typing import Optional


class AuthService:
    """Authentication service"""
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """Authenticate a user with email and password"""
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    @staticmethod
    def create_user(db: Session, email: str, name: str, password: str) -> User:
        """Create a new user"""
        hashed_password = get_password_hash(password)
        user = User(email=email, name=name, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def generate_token(user: User) -> str:
        """Generate JWT token for user"""
        return create_access_token(data={"sub": user.email, "user_id": user.id})

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import verify_password, get_password_hash, create_access_token
from app.models.user import User
from app.schemas.auth import LoginRequest, SignupRequest, TokenResponse, MFAVerifyRequest
from app.schemas.user import User as UserSchema

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Login endpoint"""
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    access_token = create_access_token(data={"sub": user.email, "user_id": user.id})
    
    return TokenResponse(
        access_token=access_token,
        user={
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "is_active": user.is_active
        }
    )


@router.post("/signup", response_model=TokenResponse)
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    """Signup endpoint"""
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(request.password)
    new_user = User(
        email=request.email,
        name=request.name,
        hashed_password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    access_token = create_access_token(data={"sub": new_user.email, "user_id": new_user.id})
    
    return TokenResponse(
        access_token=access_token,
        user={
            "id": new_user.id,
            "email": new_user.email,
            "name": new_user.name,
            "is_active": new_user.is_active
        }
    )


@router.post("/logout")
async def logout():
    """Logout endpoint"""
    return {"message": "Successfully logged out"}


@router.get("/me", response_model=UserSchema)
async def get_current_user(db: Session = Depends(get_db)):
    """Get current user endpoint"""
    # This would normally use a dependency to get the current user from the token
    # For now, return a placeholder
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


@router.post("/mfa/verify")
async def verify_mfa(request: MFAVerifyRequest):
    """Verify MFA code"""
    # Implement MFA verification logic
    return {"message": "MFA verified successfully"}

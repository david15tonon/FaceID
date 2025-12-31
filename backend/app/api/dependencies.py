# API dependencies
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def get_current_user(token = Depends(security)):
    # User authentication logic
    return {"user_id": "123"}

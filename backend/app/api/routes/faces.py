# Face recognition routes
from fastapi import APIRouter

router = APIRouter()

@router.post("/enroll")
async def enroll_face():
    return {"message": "Enroll face endpoint"}

@router.post("/verify")
async def verify_face():
    return {"message": "Verify face endpoint"}

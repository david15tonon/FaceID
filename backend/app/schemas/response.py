# Response schemas
from pydantic import BaseModel
from typing import Any, Optional

class Response(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None

# Configuration settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FaceID API"
    version: str = "1.0.0"
    api_prefix: str = "/api/v1"
    database_url: str = "sqlite:///./faceid.db"
    secret_key: str = "your-secret-key-here"
    
    class Config:
        env_file = ".env"

settings = Settings()

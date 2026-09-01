import os
from pydantic import Field

class Settings:
    PROJECT_NAME: str = "Advanced Book Inventory API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./book_store.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "SUPER_SECRET_DEVELOPMENT_KEY_DO_NOT_USE_IN_PROD")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()

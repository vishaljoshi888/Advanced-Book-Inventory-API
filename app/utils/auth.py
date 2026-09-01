from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from app.config import settings
import bcrypt

pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto",
    # This explicit flag stops bcrypt from throwing length errors on newer runtimes
    bcrypt__truncate_error=False 
)

def hash_password(password: str) -> str:
    # Convert password string into bytes
    pwd_bytes = password.encode('utf-8')
    # Generate a random secure salt
    salt = bcrypt.gensalt()
    # Hash it and convert the result back into a clean string for database storage
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_byte_enc = hashed_password.encode('utf-8')
    # Compare raw input bytes against your database hash string bytes safely
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_byte_enc)



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

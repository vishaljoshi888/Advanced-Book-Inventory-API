from typing import Optional
from sqlmodel import SQLModel, Field

# --- EXISTING BOOK SCHEMAS ---
class BookBase(SQLModel):
    title: str = Field(index=True, min_length=1, max_length=100)
    author: str = Field(index=True, min_length=1, max_length=50)
    year: int = Field(gt=0, le=2026)
    is_available: bool = True

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class BookCreate(BookBase):
    pass

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    is_available: Optional[bool] = None


# --- 🆕 NEW USER & AUTH SCHEMAS ---
class UserBase(SQLModel):
    username: str = Field(unique=True, index=True, min_length=3, max_length=20)
    email: str = Field(unique=True, index=True)

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: Optional[str] = None

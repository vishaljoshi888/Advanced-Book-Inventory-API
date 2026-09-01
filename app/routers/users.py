from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from app.database import get_session
from app.models import User, UserCreate, Token
from app.utils.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["User Authentication"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(*, session: Session = Depends(get_session), user_in: UserCreate):
    # Check if username or email already exists
    existing_user = session.exec(select(User).where((User.username == user_in.username) | (User.email == user_in.email))).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or Email already registered")
    
    hashed_pwd = hash_password(user_in.password)
    db_user = User(username=user_in.username, email=user_in.email, hashed_password=hashed_pwd)
    
    session.add(db_user)
    session.commit()
    return {"message": "User registered successfully"}

@router.post("/token", response_model=Token)
def login_for_access_token(*, session: Session = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    user = session.exec(select(User).where(User.username == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

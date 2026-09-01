from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from typing import List, Optional
from app.database import get_session
from app.models import Book, BookCreate, BookUpdate,User
from app.dependencies import get_current_user



router = APIRouter(
    prefix="/books",
    tags=["Books Management"]
)

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(*, session: Session = Depends(get_session), book_in: BookCreate,current_user: User = Depends(get_current_user)):
    db_book = Book.model_validate(book_in)
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@router.get("/", response_model=List[Book])
def read_books(
    *, 
    session: Session = Depends(get_session), 
    offset: int = 0, 
    limit: int = Query(default=100, le=100),
    author: Optional[str] = None
):
    statement = select(Book)
    if author:
        statement = statement.where(Book.author.contains(author))
    
    books = session.exec(statement.offset(offset).limit(limit)).all()
    return books

@router.get("/{book_id}", response_model=Book)
def read_book(*, session: Session = Depends(get_session), book_id: int):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.patch("/{book_id}", response_model=Book)
def update_book(*, session: Session = Depends(get_session), book_id: int, book_in: BookUpdate,current_user: User = Depends(get_current_user)):
    db_book = session.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Extract incoming patch payload data excluding default None values
    book_data = book_in.model_dump(exclude_unset=True)
    for key, value in book_data.items():
        setattr(db_book, key, value)
        
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(*, session: Session = Depends(get_session), book_id: int,current_user: User = Depends(get_current_user)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return None

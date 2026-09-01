from sqlmodel import SQLModel, create_engine, Session
from app.config import settings

# connect_args={"check_same_thread": False} is strictly needed for SQLite
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency to yield database sessions per request
def get_session():
    with Session(engine) as session:
        yield session

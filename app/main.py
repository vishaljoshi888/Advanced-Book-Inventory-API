from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config import settings
from app.database import create_db_and_tables
from app.routers import books
from app.routers import books, users

# Lifespan event handler triggers database preparation on server startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="2.0.0",
    lifespan=lifespan
)

# Connect decoupled routing sub-modules
app.include_router(users.router)
app.include_router(books.router)

@app.get("/", tags=["General System"])
def health_check():
    return {"status": "healthy", "service": settings.PROJECT_NAME}

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session, pool
from app.main import app
from app.database import get_session

# Create an in-memory SQLite database engine for isolation
# StaticPool is required to share a single in-memory DB across multiple threads/sessions
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL, 
    connect_args={"check_same_thread": False}, 
    poolclass=pool.StaticPool
)


@pytest.fixture(name="session")
def session_fixture():
    """Provides a clean database session for each individual test function."""
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="client")
def client_fixture(session: Session):
    """Overrides the real database session globally using an explicit mock generator."""
    
    # 1. Force the dynamic override function to return our isolated test session
    def get_session_override():
        return session
        
    # 2. Apply it directly to the app instance object dictionary map
    app.dependency_overrides[get_session] = get_session_override
    
    # 3. Create the active client wrapper context
    with TestClient(app) as client:
        yield client
        
    # 4. Wipe out overrides completely to prevent test-to-test cross leakage
    app.dependency_overrides.clear()

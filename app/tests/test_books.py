from fastapi.testclient import TestClient

def test_read_books_empty(client: TestClient):
    """Tests that a fresh database returns an empty list of books."""
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_book_unauthenticated(client: TestClient):
    """Tests that writing data without logging in returns a 401 Unauthorized error."""
    book_payload = {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "is_available": True
    }
    response = client.post("/books/", json=book_payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"

def test_user_registration_and_login(client: TestClient):
    """Tests the full identity lifecycle: Registering a user and logging in to get a JWT token."""
    # 1. Register a new account
    register_payload = {
        "username": "tester",
        "email": "tester@example.com",
        "password": "SecurePassword123"
    }
    register_response = client.post("/auth/register", json=register_payload)
    assert register_response.status_code == 201
    assert register_response.json()["message"] == "User registered successfully"

    # 2. Login with those credentials to request an OAuth2 access token
    login_form_data = {
        "username": "tester",
        "password": "SecurePassword123"
    }
    login_response = client.post("/auth/token", data=login_form_data) # Uses form-data, not json
    assert login_response.status_code == 200
    
    token_json = login_response.json()
    assert "access_token" in token_json
    assert token_json["token_type"] == "bearer"


def test_create_book_authenticated(client: TestClient):
    """Tests that an authenticated user with a valid JWT token can successfully add a book."""
    # 1. Register and login a dummy user to grab a valid token
    client.post("/auth/register", json={
        "username": "bookworm",
        "email": "worm@example.com",
        "password": "MySecretPassword"
    })
    login_response = client.post("/auth/token", data={"username": "bookworm", "password": "MySecretPassword"})
    access_token = login_response.json()["access_token"]

    # 2. Add the secure token to the HTTP Authorization header
    headers = {"Authorization": f"Bearer {access_token}"}

    # 3. Send the POST request with the header payload
    book_payload = {
        "title": "Neuromancer",
        "author": "William Gibson",
        "year": 1984,
        "is_available": True
    }
    response = client.post("/books/", json=book_payload, headers=headers)
    
    # 4. Assertions to confirm success
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == "Neuromancer"
    assert response_data["id"] is not None  # DB auto-generated the ID

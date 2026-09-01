# 📚 Advanced Book Inventory API

A production-ready **FastAPI Backend Application** that implements a secure, modular book inventory management system (CRUD). This project uses modern tools like **SQLModel** for database interactions, features robust route protection using **JWT (JSON Web Tokens)**, and includes an isolated automated test suite.

---

## ✨ Features

- **Production-Ready Architecture:** Decoupled codebase utilizing a clean modular design (`routers`, `models`, `database`, `utils`).
- **Unified Schemas:** Powered by **SQLModel** to merge Pydantic validation schemas and SQLAlchemy database models seamlessly.
- **Persistent Local Database:** Automatic migrations and structural operations using an internal SQLite instance.
- **JWT Authentication Layer:** Comprehensive security endpoints (`/auth/register`, `/auth/token`) to issue encrypted access tokens using pure native `bcrypt` cryptography.
- **Granular Route Guarding:** Public read permissions (`GET`) for standard inventory browsing, while data-mutation controls (`POST`, `PATCH`, `DELETE`) are safely locked behind authentication guards.
- **Automated API Interactive Docs:** Instant OpenAPI Swagger environment generation served directly at `/docs`.
- **Robust Test Coverage:** Full end-to-end automated testing suite using **Pytest** and an isolated, in-memory SQLite backend.

---

## 📂 Project Architecture

```text
book_api_advanced/
│
├── .gitignore          # Excludes local databases, caches, and secrets from Git
├── Dockerfile          # Production packaging configuration
├── README.md           # Documentation
├── requirements.txt    # System dependency matrix
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Central App entrypoint and configuration initialization
│   ├── config.py        # Global environment settings validation
│   ├── database.py      # SQLite Engine management & dynamic session provider
│   ├── models.py        # Database tables and request validation definition schemas
│   ├── dependencies.py  # Central JWT extraction and authentication guard functions
│   ├── routers/
│   │   ├── books.py     # Inventory CRUD endpoint pathways
│   │   └── users.py     # Identity Management and login pathway routines
│   └── utils/
│       └── auth.py      # Secure password hashing utilities (Bcrypt engine)
│
└── tests/               # 🧪 Automated Testing Workspace
    ├── __init__.py
    ├── conftest.py      # Isolated, in-memory SQLite database configuration & fixtures
    └── test_books.py    # Unit & Mock-Authenticated integration tests
```

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have **Python 3.10+** installed on your computer.

### 2. Installation & Setup
Clone or navigate to your project directory and follow these terminal steps:

```bash
# 1. Install all dependencies from the requirements matrix
pip install -r requirements.txt

# 2. Start the hot-reloading development server
fastapi dev app/main.py
```
*(Alternatively, you can start the application using: `uvicorn app.main:app --reload`)*

The terminal will confirm the project is active:
```text
INFO:     Uvicorn server running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## 🧪 Running Automated Tests

To ensure that your endpoints are working correctly and data is securely isolated from your local development database, run your tests using **Pytest**:

```bash
pytest
```

The testing suite automatically uses a temporary **in-memory SQLite environment** and verifies 4 core lifecycles:
1. Fetching inventory lists from an empty database.
2. Blocking unauthenticated requests with an expected `401 Unauthorized` block.
3. User identity lifecycle (Registration & logging in to successfully fetch a JWT).
4. Secure data mutation using mock authenticated access tokens.

---

## 🛠️ Interactive UI Testing

1. Open your browser and navigate to the interactive dashboard: **`http://127.0.0`**.
2. **Register a User Account:** Open the blue **`POST /auth/register`** endpoint route box, select *Try it out*, provide a custom username, email, and password payload, and hit **Execute**.
3. **Authenticate:** Scroll to the top right of the Swagger frame and select the green **Authorize** padlock box. Input your registered username and password credentials. Leave the Client ID/Secret fields completely blank and click *Authorize*.
4. **Manage Inventory:** All structural modification routes (`POST`, `PATCH`, `DELETE`) will now have closed padlocks. You are fully authenticated and can begin reading and writing records directly into the SQLite database!

---

## ⚙️ Core Dependencies

- **FastAPI:** Core modern web API framework layer.
- **SQLModel:** Advanced ORM mapper combining Pydantic parsing and SQLAlchemy core.
- **Bcrypt:** Modern Python secure cryptographic hashing libraries.
- **Python-Jose:** Enterprise JSON Web Token generation utilities.
- **Pytest & HTTPX:** Modern testing frameworks for API runtime simulation.

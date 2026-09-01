# 📚 Advanced Book Inventory API

A production-ready **FastAPI Backend Application** that implements a secure, modular book inventory management system (CRUD). This project uses modern tools like **SQLModel** for database interactions and features robust secure route protection using **JWT (JSON Web Tokens)**.

---

## ✨ Features

- **Production-Ready Architecture:** Decoupled codebase utilizing a modular design (`routers`, `models`, `database`, `utils`).
- **Unified Schemas:** Powered by **SQLModel** to merge Pydantic validation schemas and SQLAlchemy database models seamlessly.
- **Persistent Local Database:** Automatic migrations and structural operations using an internal SQLite instance.
- **JWT Authentication Layer:** Comprehensive security endpoints (`/auth/register`, `/auth/token`) to issue encrypted access tokens using pure native `bcrypt` cryptography.
- **Granular Route Guarding:** Public read permissions (`GET`) for standard inventory browsing, while data-mutation controls (`POST`, `PATCH`, `DELETE`) are locked behind authentication guards.
- **Automated API Interactive Docs:** Instant OpenAPI Swagger environment generation served directly at `/docs`.

---

## 📂 Project Architecture

```text
book_api_advanced/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Central App entrypoint and configuration initialization
│   ├── config.py        # Global environment settings validation
│   ├── database.py      # SQLite Engine management & dynamic database context generator
│   ├── models.py        # Database tables and request validation definition schemas
│   ├── dependencies.py  # Central JWT extraction and authentication guard functions
│   ├── routers/
│   │   ├── books.py     # Inventory CRUD endpoint pathways
│   │   └── users.py     # Identity Management and login pathway routines
│   └── utils/
│       └── auth.py      # Secure password hashing utilities (Bcrypt engine)
├── requirements.txt     # System dependency matrix
└── book_store.db        # SQLite database binary file (Auto-generated on startup)
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

## 🛠️ Testing the System Lifecycle

1. Open your browser and navigate to the interactive dashboard: **`http://127.0.0`**.
2. **Register a User Account:** Open the blue **`POST /auth/register`** endpoint route box, select *Try it out*, provide a custom username, email, and password payload, and hit **Execute**.
3. **Authenticate:** Scroll to the top right of the Swagger frame and select the green **Authorize** padlock box. Input your registered username and password credentials. Leave the Client ID/Secret fields completely blank and click *Authorize*.
4. **Manage Inventory:** All structural modification routes (`POST`, `PATCH`, `DELETE`) will now have closed padlocks. You are fully authenticated and can begin reading and writing records directly into the SQLite database!

---

## ⚙️ Core Dependencies

- **FastAPI:** Core modern web API framework framework layer.
- **SQLModel:** Advanced ORM mapper combining Pydantic parsing and SQLAlchemy core.
- **Bcrypt:** Modern Python secure cryptographic hashing libraries.
- **Python-Jose:** Enterprise JSON Web Token generation utilities.

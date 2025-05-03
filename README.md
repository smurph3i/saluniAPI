# Salon App API Project Structure

salon_api/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── core/ # Core config and utilities
│ │ ├── config.py # Settings (using pydantic + dotenv)
│ │ ├── security.py # JWT handling, password hashing
│ ├── db/
│ │ ├── base.py # SQLAlchemy Base and metadata
│ │ ├── session.py # DB session logic
│ │ └── init_db.py # Optional seeding script
│ ├── models/ # SQLAlchemy models
│ │ ├── user.py
│ │ ├── service.py
│ │ ├── appointment.py
│ ├── schemas/ # Pydantic schemas (input/output)
│ │ ├── user.py
│ │ ├── token.py
│ ├── api/ # API routers
│ │ ├── deps.py # Dependencies (e.g. get_current_user)
│ │ ├── routes/
│ │ │ ├── auth.py
│ │ │ ├── user.py
│ │ │ ├── service.py
│ │ │ └── appointment.py
│ ├── crud/ # CRUD abstractions for DB operations
│ │ ├── user.py
│ │ ├── service.py
│ ├── tests/ # Pytest tests
│ │ ├── test_auth.py
│ │ └── test_service.py
├── alembic/ # DB migrations
│ └── versions/
├── .env # Environment variables
├── requirements.txt # Project dependencies
├── alembic.ini # Alembic config
└── README.md

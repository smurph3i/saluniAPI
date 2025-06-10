# Salon App API Project Structure

<pre>
SaluniAPI/ 
├── app/ 
│   ├── main.py             # FastAPI app entrypoint 
│   ├── core/               # Core config and utilities 
│   │   ├── config.py       # Settings (Pydantic + python-dotenv) 
│   │   ├── security.py     # JWT handling, password hashing 
│   │   ├── token_service.py
│   ├── db/ 
│   │   ├── __init__.py
│   │   ├── base_class.py         # SQLAlchemy Base and metadata 
│   │   ├── deps.py
│   │   ├── session.py      # DB session management 
│   │   ├── test_connection.py      
│   │   └── init_db.py      # Optional DB seed script 
│   ├── models/             # SQLAlchemy models 
│   │   ├── __init__.py 
│   │   ├── user.py 
│   │   ├── service.py 
│   │   ├── appointment.py 
│   ├── schemas/            # Pydantic schemas (DTOs) 
│   │   ├── __init__.py 
│   │   ├── user.py 
│   │   ├── token.py 
│   ├── api/                # API routing 
│   │   ├── deps.py         # Dependencies (e.g. auth guards) 
│   │   ├── v1/
│   │   │   ├── routes/ 
│   │   │   │   ├── health.py
│   │   │   │   ├── auth.py 
│   │   │   │   ├── login.py
│   │   │   │   ├── users.py 
│   │   │   │   ├── service.py 
│   │   │   │   └── appointment.py 
│   ├── crud/               # CRUD operations 
│   │   ├── crud_user.py 
│   │   ├── crud_service.py 
│   │   └── crud_appointment.py 
│   ├── tests/              # Pytest tests 
│   │   ├── conftest.py
│   │   ├── test_health.py
│   │   ├── test_users.py
│   │   ├── test_auth.py 
│   │   ├── test_security.py 
│   │   └── test_service.py 
├── alembic/                # DB migrations 
│       └── versions/ 
├── .env                    # Environment variables 
├── requirements.txt        # Dependencies 
├── alembic.ini             # Alembic configuration 
└── README.md 
</pre>

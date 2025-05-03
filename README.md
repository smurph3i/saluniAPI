# Salon App API Project Structure

<pre>
SaluniAPI/ 
├── app/ 
│   ├── main.py             # FastAPI app entrypoint 
│   ├── core/               # Core config and utilities 
│   │   ├── config.py       # Settings (Pydantic + python-dotenv) 
│   │   ├── security.py     # JWT handling, password hashing 
│   ├── db/ 
│   │   ├── base.py         # SQLAlchemy Base and metadata 
│   │   ├── session.py      # DB session management 
│   │   └── init_db.py      # Optional DB seed script 
│   ├── models/             # SQLAlchemy models 
│   │   ├── user.py 
│   │   ├── service.py 
│   │   ├── appointment.py 
│   ├── schemas/            # Pydantic schemas (DTOs) 
│   │   ├── user.py 
│   │   ├── token.py 
│   ├── api/                # API routing 
│   │   ├── deps.py         # Dependencies (e.g. auth guards) 
│   │   ├── routes/ 
│   │   │ ├── auth.py 
│   │   │ ├── user.py 
│   │   │ ├── service.py 
│   │   │ └── appointment.py 
│   ├── crud/               # CRUD operations 
│   │   ├── user.py 
│   │   ├── service.py 
│   ├── tests/              # Pytest tests 
│   │   ├── test_auth.py 
│   │   └── test_service.py 
├── alembic/                # DB migrations 
│       └── versions/ 
├── .env                    # Environment variables 
├── requirements.txt        # Dependencies 
├── alembic.ini             # Alembic configuration 
└── README.md 
</pre>

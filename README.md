# saluniAPI

## Structure of the files

booking_api/
├── main.py # Entry point of application
├── requirements.txt # Dependencies
├── alembic/ # Database migrations
├── app/
│ ├── **init**.py
│ ├── config.py # Configuration settings
│ ├── database.py # Database connection
│ ├── models/ # SQLAlchemy models
│ │ ├── **init**.py
│ │ ├── user.py
│ │ ├── booking.py
│ │ ├── resource.py # Bookable resources
│ │ └── availability.py
│ ├── schemas/ # Pydantic models for request/response
│ │ ├── **init**.py
│ │ ├── user.py
│ │ ├── booking.py
│ │ └── resource.py
│ ├── api/ # API routes
│ │ ├── **init**.py
│ │ ├── v1/ # Version 1 of your API
│ │ │ ├── **init**.py
│ │ │ ├── endpoints/
│ │ │ │ ├── **init**.py
│ │ │ │ ├── users.py
│ │ │ │ ├── bookings.py
│ │ │ │ ├── resources.py
│ │ │ │ └── availability.py
│ │ │ └── router.py # Combines all v1 routes
│ ├── core/ # Business logic
│ │ ├── **init**.py
│ │ ├── security.py # Authentication & permissions
│ │ ├── booking_logic.py
│ │ └── availability_logic.py
│ └── utils/ # Utilities and helpers
│ ├── **init**.py
│ └── datetime_utils.py
└── tests/ # Unit and integration tests

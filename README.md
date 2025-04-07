# SaluniAPI

## Description:

The API allows users to Book sessions with their favorite Hairdresser or barber

## Structure of the files

### Current Structure

```
saluni_api/
├──app
│   ├── __init__.py
│   ├── main.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   └── models/
│       ├── __init__.py
│       ├── booking.py
│   └── schemas/
│      ├── __init__.py
│      └── booking.py
```

### Aimed Structure

```
booking_api/
├── main.py                 # Entry point of application
├── requirements.txt        # Dependencies
├── alembic/                # Database migrations
├── app/
│   ├── __init__.py
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database connection
│   ├── models/             # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── booking.py
│   │   ├── resource.py     # Bookable resources
│   │   └── availability.py
│   ├── schemas/            # Pydantic models for request/response
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── booking.py
│   │   └── resource.py
│   ├── api/                # API routes
│   │   ├── __init__.py
│   │   ├── v1/             # Version 1 of your API
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   ├── bookings.py
│   │   │   │   ├── resources.py
│   │   │   │   └── availability.py
│   │   │   └── router.py   # Combines all v1 routes
│   ├── core/               # Business logic
│   │   ├── __init__.py
│   │   ├── security.py     # Authentication & permissions
│   │   ├── booking_logic.py
│   │   └── availability_logic.py
│   └── utils/              # Utilities and helpers
│       ├── __init__.py
│       └── datetime_utils.py
└── tests/                  # Unit and integration tests ration tests
```

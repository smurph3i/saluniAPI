from fastapi import FastAPI
from app.api.v1.routes import health, users

app = FastAPI(title="SaluniAPI")

app.include_router(health.router)  # Register the health route
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

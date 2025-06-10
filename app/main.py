from fastapi import FastAPI
from app.api.v1.routes import health, users, login

app = FastAPI(title="SaluniAPI")

app.include_router(health.router)  # Register the health route
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(login.router, prefix="/api/v1", tags=["auth"])

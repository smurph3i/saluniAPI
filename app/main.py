from fastapi import FastAPI
from app.api.routes import health

app = FastAPI(title="SaluniAPI")

app.include_router(health.router)  # Register the health route

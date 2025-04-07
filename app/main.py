from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Annotated
from database import engine, SessionLocal
from .database.database import get_db
from .models import booking as booking_models
from .schemas import booking as booking_schemas

app = FastAPI(
    title="Saluni Booking API",
    description="API for managing Salon Bookings",
    version="1.0.0"
)

booking_models.Base.metadata.create_all(bind=get_db().__next__().bind)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

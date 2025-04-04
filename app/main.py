from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI(
    title="Saluni Booking API",
    description="API for managing Salon Bookings",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

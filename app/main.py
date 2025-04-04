from fastapi import FastAPI

app = FastAPI(
    title="Saluni Booking API",
    description="API for managing Salon Bookings",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

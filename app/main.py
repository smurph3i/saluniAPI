from fastapi import FastAPI
from app.api.routes import auth, user, service, appointment

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(service.router, prefix="/services", tags=["services"])
app.include_router(appointment.router,
                   prefix="/appointments", tags=["appointments"])

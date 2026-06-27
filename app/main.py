from fastapi import FastAPI
from app.routers import bookings
from app.database import Base, engine
import app.models

from app.routers import users
from app.routers import classes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fitness Booking API",
    description="Backend API for Fitness Studio Booking",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(classes.router)
app.include_router(bookings.router)

@app.get("/")
def home():
    return {"message": "Welcome to Fitness Booking API"}
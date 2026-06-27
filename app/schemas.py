from pydantic import BaseModel, EmailStr
from datetime import datetime


# ---------- User ----------

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- Class ----------

class ClassCreate(BaseModel):
    name: str
    date_time: datetime
    instructor: str
    available_slots: int


# ---------- Booking ----------

class BookingCreate(BaseModel):
    class_id: int

class ClassResponse(BaseModel):
    id: int
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

    class Config:
        from_attributes = True
class BookingResponse(BaseModel):
    id: int
    class_id: int
    booking_time: datetime

    class Config:
        from_attributes = True        
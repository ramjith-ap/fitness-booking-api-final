from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import Booking, FitnessClass
from app.schemas import BookingCreate

router = APIRouter(tags=["Bookings"])


@router.post("/book")
def book_class(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    fitness_class = db.query(FitnessClass).filter(
        FitnessClass.id == booking.class_id
    ).first()

    if fitness_class is None:
        raise HTTPException(status_code=404, detail="Class not found")

    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    existing_booking = db.query(Booking).filter(
        Booking.user_id == current_user.id,
        Booking.class_id == booking.class_id
    ).first()

    if existing_booking:
        raise HTTPException(status_code=400, detail="Already booked")

    new_booking = Booking(
        user_id=current_user.id,
        class_id=booking.class_id,
        booking_time=datetime.utcnow()
    )

    fitness_class.available_slots -= 1

    db.add(new_booking)
    db.commit()

    return {"message": "Class booked successfully"}
@router.get("/bookings")
def get_bookings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    bookings = db.query(Booking).filter(
        Booking.user_id == current_user.id
    ).all()

    return bookings

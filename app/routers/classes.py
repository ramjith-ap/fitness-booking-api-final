from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import FitnessClass
from app.schemas import ClassCreate, ClassResponse
from app.dependencies import get_current_user

router = APIRouter(tags=["Classes"])


@router.post("/classes", response_model=ClassResponse)
def create_class(
    fitness_class: ClassCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_class = FitnessClass(
        name=fitness_class.name,
        date_time=fitness_class.date_time,
        instructor=fitness_class.instructor,
        available_slots=fitness_class.available_slots
    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return new_class


@router.get("/classes", response_model=list[ClassResponse])
def get_classes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return db.query(FitnessClass).all()
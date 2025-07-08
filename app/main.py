from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.models import (
    FitnessClassModel,
    BookingModel,
    BookingRequest,
    FitnessClass,
    Booking
)
from app.db import db
from app.utils import convert_to_timezone
from app.seed import seed_classes

app = FastAPI(title="Fitness Booking API")

# ✅ CORS setup (optional, for Postman or browser testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Automatically seed class data on app startup
@app.on_event("startup")
def load_seed_data():
    seed_classes()

# ✅ GET /classes – List all upcoming classes
@app.get("/classes", response_model=List[FitnessClass])
def get_classes(timezone: str = Query(default="Asia/Kolkata")):
    classes = db.query(FitnessClassModel).all()
    return [convert_to_timezone(cls, timezone) for cls in classes]

# ✅ POST /book – Book a class by ID
@app.post("/book", response_model=Booking)
def book_class(booking_req: BookingRequest):
    try:
        cls = db.query(FitnessClassModel).filter(
            FitnessClassModel.id == booking_req.class_id
        ).first()

        if not cls:
            raise HTTPException(status_code=404, detail="Class not found")

        if cls.available_slots <= 0: # type: ignore
            raise HTTPException(status_code=400, detail="No slots available")

        cls.available_slots -= 1 # type: ignore

        new_booking = BookingModel(
            class_id=cls.id,
            client_name=booking_req.client_name,
            client_email=booking_req.client_email
        )

        db.add(cls)
        db.add(new_booking)
        db.commit()
        db.refresh(new_booking)

        return new_booking

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Booking failed: {str(e)}")

# ✅ GET /bookings – Fetch bookings by email
@app.get("/bookings", response_model=List[Booking])
def get_bookings(email: str):
    bookings = db.query(BookingModel).filter(
        BookingModel.client_email == email
    ).all()
    return bookings

# ✅ Root route – Health check
@app.get("/")
def root():
    return {"message": "Fitness Booking API is running!"}

# app/models.py

from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# --- SQLAlchemy Models (Database) ---

class FitnessClassModel(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    instructor = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)  # Stored in IST
    available_slots = Column(Integer, default=0)

    bookings = relationship("BookingModel", back_populates="fitness_class")


class BookingModel(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)

    fitness_class = relationship("FitnessClassModel", back_populates="bookings")


# --- Pydantic Models (Request/Response) ---

class FitnessClass(BaseModel):
    id: int
    name: str
    instructor: str
    date_time: datetime
    available_slots: int

    model_config = ConfigDict(from_attributes=True)  # ✅ Pydantic v2


class Booking(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    model_config = ConfigDict(from_attributes=True)  # ✅ Pydantic v2


class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

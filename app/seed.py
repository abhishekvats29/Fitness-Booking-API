# app/seed.py

from datetime import datetime, timedelta
from app.db import db
from app.models import FitnessClassModel
from sqlalchemy.exc import IntegrityError

def seed_classes():
    # Skip seeding if classes already exist
    if db.query(FitnessClassModel).first():
        return

    now = datetime.now()

    classes = [
        FitnessClassModel(
            name="Yoga",
            instructor="Aayusha",
            date_time=now + timedelta(days=1, hours=6),
            available_slots=10
        ),
        FitnessClassModel(
            name="Zumba",
            instructor="Astha",
            date_time=now + timedelta(days=2, hours=8),
            available_slots=15
        ),
        FitnessClassModel(
            name="HIIT",
            instructor="Raman",
            date_time=now + timedelta(days=3, hours=7),
            available_slots=12
        )
    ]

    try:
        db.add_all(classes)
        db.commit()
    except IntegrityError:
        db.rollback()

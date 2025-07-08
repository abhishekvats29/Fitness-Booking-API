# app/utils.py

from zoneinfo import ZoneInfo  # Python 3.9+
from app.models import FitnessClassModel
from datetime import datetime

# Convert class time from IST to requested timezone
def convert_to_timezone(fitness_class: FitnessClassModel, target_tz: str):
    try:
        ist = ZoneInfo("Asia/Kolkata")
        target = ZoneInfo(target_tz)

        original_time = fitness_class.date_time.replace(tzinfo=ist)
        converted_time = original_time.astimezone(target)

        return {
            "id": fitness_class.id,
            "name": fitness_class.name,
            "instructor": fitness_class.instructor,
            "date_time": converted_time,
            "available_slots": fitness_class.available_slots,
        }
    except Exception:
        # Fallback to original IST if timezone is invalid
        return {
            "id": fitness_class.id,
            "name": fitness_class.name,
            "instructor": fitness_class.instructor,
            "date_time": fitness_class.date_time,
            "available_slots": fitness_class.available_slots,
        }

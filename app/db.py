# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models import Base  # Updated import

DATABASE_URL = "sqlite:///./fitness.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=False)
db = scoped_session(SessionFactory)

# Create tables on first run
Base.metadata.create_all(bind=engine)

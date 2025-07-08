# tests/test_main.py

import sys
import os

# ✅ Fix import path for main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Fitness Booking API is running!"}

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_class_invalid_id():
    response = client.post("/book", json={
        "class_id": 999,
        "client_name": "Test",
        "client_email": "test@example.com"
    })
    assert response.status_code == 404
    assert response.json()["detail"] == "Class not found"

def test_get_bookings_missing_email():
    response = client.get("/bookings")
    assert response.status_code == 422

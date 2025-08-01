# Fitness Booking API

A lightweight, timezone-aware booking API for a fictional fitness studio. Built using **FastAPI**, **SQLite**, and **SQLAlchemy**. Supports class listing, booking, and booking history retrieval with a simple and modular design.

---
## 🌐 Live Demo

👉 **Deployed Link**: Click here to view Live Demo
[https://fitness-booking-api.onrender.com]

👉 **Swagger Docs**:  Click here to view Live Docs
[https://fitness-booking-api.onrender.com/docs]

👉 **Redoc UI Page**:  Click here to view Live ReDocs
[https://fitness-booking-api.onrender.com/redoc]

---
### Screenshots

#### Live API Documentation (Swagger UI)
<img width="1920" height="971" alt="Image" src="https://github.com/user-attachments/assets/83b80ad6-cbb9-4c59-aa40-da0b7b79e8a0" />

#### Sample API Response (POST /book-class)
<img width="1137" height="706" alt="Image" src="https://github.com/user-attachments/assets/4068db56-2236-4821-9a85-b99ab3943cdd" />

---
## Features

- 🧘 View available fitness classes (Yoga, Zumba, HIIT)
- 🕒 Timezone-aware scheduling (default: Asia/Kolkata)
- 📨 Book classes using client name & email
- 📧 View all bookings made by an email
- ❌ Handles overbooking and validation errors
- 📄 Auto-generated API docs via Swagger & ReDoc
- 🧪 Tested using pytest
- 🐳 Docker-ready deployment

---
## Tech Stack

- ⚙️ **Backend**: FastAPI (Python)
- 🐳 **Deployment**: Render (Docker)
- 📨 **Email Validation**: Pydantic + email-validator
- 📄 **API Docs**: Swagger UI (FastAPI default)
- 💾 **Database**: SQLite
- 🧪 **Testing Tool**: Swagger UI / Postman (optional)
  
---
## ⚙️ Setup Instructions
### Create Virtual Environment
bash
python -m venu venu

### Activate
source venv/bin/activate
.\venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Run locally
uvicorn app.main:app --reload

---

## Visit in browser:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Running Tests

pytest


## 📄 API Documentation
A complete breakdown of all endpoints, request/response formats, query parameters, and error codes is available here:

## 🧑‍💻 Developer Info

- Author: Abhishek Vats
- Role: Python Developer – Booking API Assignment
- Date: July 2025
- Submission: Code, Dockerfile, Tests, Docs, Loom Video

## 📝 License

This project is Developed as a part of a FullStack API Assignmnet.


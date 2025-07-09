# 🏋️ Fitness Booking API

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
### 📸 Screenshots

#### ✅ Live API Documentation (Swagger UI)
<img src="https://github.com/user-attachments/assets/f26605d0-4d0d-4922-848c-b73196630685" alt="Swagger Docs Screenshot" style="width: 100%; max-width: 800px; border-radius: 8px;" />

#### ✅ Sample API Response (POST /book-class)
![Booking response](screenshots/post-booking-success.png)

---
## 🚀 Features

- 🧘 View available fitness classes (Yoga, Zumba, HIIT)
- 🕒 Timezone-aware scheduling (default: Asia/Kolkata)
- 📨 Book classes using client name & email
- 📧 View all bookings made by an email
- ❌ Handles overbooking and validation errors
- 📄 Auto-generated API docs via Swagger & ReDoc
- 🧪 Tested using pytest
- 🐳 Docker-ready deployment

---

## ⚙️ Setup Instructions

### 🐍 Create Virtual Environment

```bash
python -m venv venv

# Activate:
source venv/bin/activate        # macOS/Linux
.\venv\Scripts\activate         # Windows

## Install Dependencies

pip install -r requirements.txt


## ▶️ Run Locally

uvicorn main:app --reload

## Visit in browser:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Running Tests

pytest


## 📄 API Documentation
A complete breakdown of all endpoints, request/response formats, query parameters, and error codes is available here:

🎥 Loom Walkthrough
🎬 Watch Demo Video: Click here to view Loom demo

(Replace with your Loom recording link)

## 🧑‍💻 Developer Info

Author: Abhishek Vats
Role: Python Developer – Fullstack API Assignment
Date: July 2025
Submission: Code, Dockerfile, Tests, Docs, Loom Video

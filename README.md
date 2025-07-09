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
<img width="1920" height="971" alt="Image" src="https://github.com/user-attachments/assets/83b80ad6-cbb9-4c59-aa40-da0b7b79e8a0" />

#### ✅ Sample API Response (POST /book-class)
<img src="https://github.com/user-attachments/assets/f26605d0-4d0d-4922-848c-b73196630685" alt="Swagger Docs Screenshot" style="width: 100%; display: block; margin: auto;" />

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
---

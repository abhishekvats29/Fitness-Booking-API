# 🏋️ Fitness Booking API – FastAPI Project

A lightweight, timezone-aware booking API for a fictional fitness studio. Built using **FastAPI**, **SQLite**, and **SQLAlchemy**. Supports class listing, booking, and booking history retrieval with a simple and modular design.

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

## 🌐 Live Demo

👉 **Deployed Link**: [https://fitness-api-your-link.onrender.com](https://fitness-api-your-link.onrender.com)

👉 **Swagger Docs**: [https://fitness-api-your-link.onrender.com/docs](https://fitness-api-your-link.onrender.com/docs)

---

## 🖼️ Screenshot

![Fitness Booking API Docs](screenshots/swagger-ui.png)

> (Replace the above with a real screenshot from Swagger UI)

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


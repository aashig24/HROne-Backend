# HROne Backend Task – E-commerce API (FastAPI + MongoDB)

This is a simple backend application that simulates an e-commerce API, built using FastAPI and MongoDB.

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- MongoDB Atlas (via PyMongo)
- Uvicorn (for local dev)

## 📦 Features

- `POST /products` → Add a product
- `GET /products` → List/search products with filters (name, size)
- `POST /orders` → Place an order
- `GET /orders/{user_id}` → View orders of a specific user

## 📁 Project Structure

├──main.py # FastAPI app and endpoints
├── models.py # Request/Response models
├── db.py # MongoDB connection setup
└── .env # MongoDB URI and DB name


## 🧪 How to Run Locally

1. Create a virtual environment
2. Install requirements: pip install fastapi uvicorn pymongo python-dotenv
3.  Create a `.env` file:
MONGO_URI=mongodb+srv://aashigupta1509:UXNIRhK0wdtBk2BJ@cluster0.xiit5pv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
DB_NAME=hrone
4. Run server: uvicorn main:app --reload --port 8080
5. Open Swagger UI: http://localhost:8080/docs









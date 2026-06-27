# Fitness Booking API

A backend REST API for managing fitness class bookings built using FastAPI and SQLite.

## Features

- User Registration
- User Login with JWT Authentication
- Create Fitness Classes
- View All Fitness Classes
- Book Available Classes
- View User Bookings
- Prevent Overbooking
- Password Hashing
- SQLite Database
- Swagger API Documentation

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Passlib
- Uvicorn

---

## Installation

Clone the repository


git clone <your-github-repository-url>

Move into project directory


cd fitness-booking-api


Create virtual environment


python -m venv venv


Activate virtual environment

Windows


venv\Scripts\activate


Install dependencies


pip install -r requirements.txt


---

## Run the Project


uvicorn app.main:app --reload


Server runs at


http://127.0.0.1:8000


Swagger Documentation


http://127.0.0.1:8000/docs


---

## API Endpoints

### Authentication

POST /signup

POST /login

### Classes

POST /classes

GET /classes

### Bookings

POST /book

GET /bookings

---

## Database

SQLite

Database file


fitness.db


---

## Authentication

JWT Token Based Authentication

Protected APIs

- POST /classes
- GET /classes
- POST /book
- GET /bookings

---
#### Author

Ramjith A P
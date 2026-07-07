# 🎓 Student Management System API

<p align="center">

![Student Management](https://img.shields.io/badge/STUDENT%20MANAGEMENT-SYSTEM-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-brightgreen?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?style=for-the-badge)
![REST API](https://img.shields.io/badge/REST-API-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### 🚀 A RESTful Student Management System built with FastAPI and MongoDB

**Create • Read • Update • Delete • REST APIs**

[Features](#-key-features) •
[Architecture](#-system-architecture) •
[Tech Stack](#️-technologies-used) •
[Installation](#-installation) •
[API Endpoints](#-api-endpoints)

</p>

---

# 🎯 Overview

The **Student Management System API** is a backend application developed using **FastAPI** and **MongoDB** to perform complete **CRUD (Create, Read, Update, Delete)** operations on student records.

The project demonstrates the complete backend workflow, including API development, request-response handling, database connectivity, data validation using Pydantic, and RESTful service implementation.

Designed as part of an AI/ML internship, this project strengthened the understanding of backend development principles that serve as the foundation for modern AI and machine learning applications.

---

# ✨ Key Features

- 📌 RESTful API Architecture
- ➕ Add New Student Records
- 📋 Retrieve Student Information
- ✏️ Update Existing Student Details
- ❌ Delete Student Records
- 🗄️ MongoDB Database Integration
- ⚡ FastAPI High-Performance Backend
- ✅ Request Validation using Pydantic
- 📖 Automatic Swagger API Documentation
- 🔄 JSON-based Request & Response Handling

---

# 🏗️ System Architecture

```
                Client
                   │
                   ▼
          FastAPI Application
                   │
                   ▼
            API Route Layer
                   │
                   ▼
          Service (Business Logic)
                   │
                   ▼
             MongoDB Database
                   │
                   ▼
            JSON API Response
```
---

# ⚙️ Application Workflow

```
User Request
      │
      ▼
FastAPI Endpoint
      │
      ▼
Request Validation
      │
      ▼
Business Logic
      │
      ▼
MongoDB Database
      │
      ▼
Response Generation
      │
      ▼
JSON Response
```

---

# 📂 Project Structure

```
Student-Management-System/
│
├── database/
│   └── database_connection.py      # MongoDB connection setup
│
├── models/
│   └── student_models.py           # Database models
│
├── routes/
│   └── student_routes.py           # API endpoints
│
├── schemas/
│   └── student_schema.py           # Pydantic request/response schemas
│
├── services/
│   └── student_service.py          # Business logic & CRUD operations
│
├── configurations.py               # Application configuration
├── main.py                         # FastAPI application entry point
├── pyproject.toml                  # Project dependencies
├── uv.lock                         # Dependency lock file
└── README.md
```

---

# 🚀 Key Functionalities

## 👨‍🎓 Student Registration

Create new student records with details such as:

- Student ID
- Name
- Age
- Email
- Course
- Department

---

## 📄 View Students

Retrieve

- All Students
- Individual Student by ID

---

## ✏️ Update Student Information

Modify existing student records without affecting other entries.

---

## 🗑️ Delete Student Records

Remove student information permanently from the database.

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/students` | Add a new student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{id}` | Retrieve student by ID |
| PUT | `/students/{id}` | Update student details |
| DELETE | `/students/{id}` | Delete student |

---

# ⚙️ Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.9+ |
| Backend Framework | FastAPI |
| Database | MongoDB |
| Data Validation | Pydantic |
| API Testing | Swagger UI |
| API Style | REST |
| Environment Variables | python-dotenv |
| Version Control | Git & GitHub |

---

# 📊 Request Lifecycle

The application follows the workflow below:

1. Client sends an HTTP request.
2. FastAPI receives the request.
3. Pydantic validates incoming data.
4. CRUD logic processes the request.
5. MongoDB stores or retrieves data.
6. FastAPI returns a JSON response.
7. Swagger UI automatically documents the API.

---

# 📸 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔐 Environment Variables

Create a `.env` file.

```env
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=student_database
```

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/FastAPI-Student-Management-System.git
```

Navigate to the project directory.

```bash
cd FastAPI-Student-Management-System
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
uvicorn app:app --reload
```

Open your browser.

```
http://127.0.0.1:8000/docs
```

---

# 📈 Future Enhancements

- 🔐 JWT Authentication
- 👤 User Login & Registration
- 📚 Course Management Module
- 🎓 Faculty Management
- 📊 Student Analytics Dashboard
- ☁️ Docker Deployment
- 🧪 Unit Testing
- 📦 CI/CD Integration

---

# 🎯 Learning Outcomes

This project helped in understanding:

- REST API Development
- FastAPI Framework
- Backend Architecture
- CRUD Operations
- MongoDB Integration
- Request Validation
- JSON Data Exchange
- API Documentation
- Client–Server Communication
- Backend Development Best Practices

---



</p>

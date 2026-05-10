# Employee Task Management System

A RESTful API built with **FastAPI** and **Microsoft SQL Server** for managing employees and their assigned tasks within an organization. The system supports authentication, role-based access, and full CRUD operations on employees and tasks.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Dependencies](#dependencies)

---

## Overview

The Employee Task Management System provides a backend API that allows organizations to:

- Register and authenticate users with JWT-based security
- Manage employee records (create, read, update, delete)
- Assign, track, and update tasks for employees
- Enforce access control so that only authorized users can perform sensitive operations

---

## Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Framework    | FastAPI                             |
| Language     | Python 3.x                          |
| Database     | Microsoft SQL Server (SQL Express)  |
| ORM          | SQLAlchemy                          |
| DB Driver    | pyodbc (ODBC Driver 18)             |
| Auth         | JWT (python-jose) + bcrypt (passlib)|
| Validation   | Pydantic                            |
| Server       | Uvicorn                             |
| IDE          | VS Code (workspace included)        |

---

## Project Structure

```
Employee-Task-Management-System/
├── app/                        # Main application package
│   ├── main.py                 # FastAPI app entry point
│   ├── database.py             # Database connection & session
│   ├── models/                 # SQLAlchemy ORM models
│   ├── schemas/                # Pydantic request/response schemas
│   ├── routers/                # API route handlers
│   └── auth/                   # Authentication logic (JWT, hashing)
├── .env                        # Environment variables (DB connection)
├── requirments.txt             # Python dependencies
├── Employee Task Management System API.code-workspace
└── README.md
```

---

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+**
- **Microsoft SQL Server** (SQL Express or higher)
- **ODBC Driver 18 for SQL Server** — [Download here](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
- **pip** (Python package manager)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/BinoyBabu10/Employee-Task-Management-System.git
   cd Employee-Task-Management-System
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirments.txt
   ```

---

## Configuration

The app reads its database connection from the `.env` file in the project root.

```env
DATABASE_URL=mssql+pyodbc://@localhost\SQLEXPRESS/EmployeeTaskManagementSystem?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes
```

**Before running**, make sure:

- SQL Server is running on `localhost\SQLEXPRESS`
- A database named `EmployeeTaskManagementSystem` exists (or the app will create the tables via SQLAlchemy)
- Windows Authentication (`trusted_connection=yes`) is enabled, or update the URL with your SQL Server username/password:

  ```env
  DATABASE_URL=mssql+pyodbc://username:password@localhost\SQLEXPRESS/EmployeeTaskManagementSystem?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes
  ```

> **Security Note:** Do not commit `.env` files with real credentials to version control. Add `.env` to your `.gitignore`.

---

## Running the Application

Start the development server with Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, visit:

- **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Dependencies

All dependencies are listed in `requirments.txt`:

| Package          | Purpose                                      |
|------------------|----------------------------------------------|
| `fastapi`        | Web framework for building APIs              |
| `uvicorn`        | ASGI server to run FastAPI                   |
| `sqlalchemy`     | ORM for database models and queries          |
| `pyodbc`         | ODBC connector for SQL Server                |
| `python-dotenv`  | Load environment variables from `.env`       |
| `pydantic`       | Data validation and serialization            |
| `python-jose`    | JWT token creation and verification          |
| `passlib`        | Password hashing (bcrypt)                    |
| `python-multipart` | Form data support (for login endpoints)  |

---

## Author

**BinoyBabu10** — [GitHub Profile](https://github.com/BinoyBabu10)

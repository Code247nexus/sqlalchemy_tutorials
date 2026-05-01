# 📦 Employee Management System (ORM Layer)

This project implements a **CLI-based Employee Management System** using **SQLAlchemy ORM** with PostgreSQL. The focus is on building a clean and modular database interaction layer using object-oriented design.

---

## 🚀 Tech Stack

* Python
* SQLAlchemy (ORM)
* PostgreSQL
* dotenv (environment variables)

---

## 🧠 What This Project Demonstrates

* Mapping Python classes to database tables using ORM
* Performing CRUD operations using SQLAlchemy sessions
* Managing database connections using a singleton pattern
* Separating concerns using layered architecture (core, models, repository)

---

## 🏗️ Project Structure

```text
project_root/
│
├── main.py                 # CLI entry point
├── tables.py               # Table creation
├── .env                    # Environment variables
│
├── core/
│   └── database.py         # Engine, Session, Base
│
├── models/
│   └── models1.py          # Employee ORM model
│
├── repository/
│   └── emp_repository.py   # CRUD operations
```

---

## 🔹 ORM Model

```python
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)
```

---

## ⚙️ Core ORM Components

### 🔸 Engine

The engine acts as the core interface between the application and the database, managing connections and executing SQL statements.

### 🔸 Base

Base is the declarative foundation class used to define ORM models and store metadata about all tables.

### 🔸 Session

A session is a transactional workspace used to interact with the database, allowing operations like insert, update, delete, and commit.

---

## 🔄 ORM Workflow

```text
Python Object → SQLAlchemy ORM → SQL Query → PostgreSQL
PostgreSQL → ORM → Python Object
```

---

## 📌 Features

* Create Employee
* Retrieve Employee by ID
* Retrieve All Employees
* Update Employee Details
* Delete Employee

---

## ⚡ How to Run

1. Clone the repository
2. Create a `.env` file:

```env
user=your_db_user
password=your_db_password
database=your_db_name
```

3. Install dependencies:

```bash
pip install sqlalchemy psycopg2-binary python-dotenv
```

4. Run the project:

```bash
python main.py
```

---

## 🧠 Key Learnings

* Understanding how ORM abstracts SQL queries
* Managing session lifecycle in database operations
* Importance of a single shared database instance
* Structuring backend code for scalability

---

## 📈 Future Improvements

* Add FastAPI for REST API support
* Implement JWT authentication
* Add Pydantic validation layer
* Introduce Alembic for database migrations
* Deploy the application

---

## 🎯 Summary

This project demonstrates how SQLAlchemy ORM can be used to build a clean, modular, and scalable database layer, forming the foundation for a production-ready backend system.

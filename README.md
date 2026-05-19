# FastAPI CRUD Assignment

This project is developed using FastAPI, SQLAlchemy, and MySQL.

It includes:
- Category CRUD APIs
- Product CRUD APIs
- One-to-Many relationship
- Pagination
- Swagger Documentation

---

# GitHub Repository

Repo Link:

```bash
git clone https://github.com/aman70216/AssingmentGivenByNimapInfotech.git
```

---

# Steps to Run the Application

## 1. Clone the Repository

```bash
git clone https://github.com/aman70216/AssingmentGivenByNimapInfotech.git
```

---

## 2. Move to Project Folder

```bash
cd AssingmentGivenByNimapInfotech
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install Required Packages

```bash
pip install -r requirements.txt
```

---

# Database Configuration

Create a MySQL database:

```sql
CREATE DATABASE ProductAndCategory;
```

Update database connection in `database.py` file:

```python
DATABASE_URL = "mysql+pymysql://root:yourpassword@localhost/ProductAndCategory"
```

Replace:
- `root` with your MySQL username
- `yourpassword` with your MySQL password

---

# Run the Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

After starting the server open:

```bash
http://127.0.0.1:8000/docs
```

---

# Database Design

## Categories Table

| Column | Type |
|---|---|
| id | Integer |
| name | String |

---

## Products Table

| Column | Type |
|---|---|
| id | Integer |
| name | String |
| price | Float |
| category_id | Integer (Foreign Key) |

---

# Relationship

One Category can have multiple Products.

Each Product belongs to one Category.

Relationship Type:
```bash
One-to-Many
```

---

# API Endpoints
Important Instruction Replace {id} with Number Other Wise It will Throw Error 

## Category APIs

| Method | Endpoint |
|---|---|
| GET | http://127.0.0.1:8000/api/categories |
| POST | http://127.0.0.1:8000/api/categories |
| GET | http://127.0.0.1:8000/api/categories/{id} |
| PUT | http://127.0.0.1:8000/api/categories/{id} |
| DELETE | http://127.0.0.1:8000/api/categories/{id} |

---

## Product APIs

| Method | Endpoint |
|---|---|
| GET | http://127.0.0.1:8000/api/products |
| POST | http://127.0.0.1:8000/api/products |
| GET | http://127.0.0.1:8000/api/products/{id} |
| PUT | http://127.0.0.1:8000/api/products/{id} |
| DELETE | http://127.0.0.1:8000/api/products/{id} |

---

# Features

- CRUD Operations
- Server-side Pagination
- SQLAlchemy ORM
- MySQL Database
- FastAPI Swagger Docs
- Category and Product Relationship

---

# Technologies Used

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn

---

Built by Aman Mishra

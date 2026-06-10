# FastAPI Expense API

A beginner-friendly backend API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Pydantic** for managing expense records.

This project was created as a backend practice project to understand how FastAPI works with a real PostgreSQL database using SQLAlchemy ORM.

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
* Git/GitHub

## Features

* Create a new expense
* Get all expenses
* Get a single expense by ID
* Update an expense by ID
* Delete an expense by ID
* Filter expenses by category
* Filter expenses by paid status
* Pagination using `skip` and `limit`
* Expense summary endpoint
* Error handling with `HTTPException`
* PostgreSQL database integration
* SQLAlchemy ORM model
* Pydantic request validation
* Clean project structure
* Dependency management using `requirements.txt`

## Project Structure

```text
expense-api/
│
├── main.py              # Current FastAPI routes/endpoints
├── database.py          # Database connection and session setup
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── old_versions/        # Earlier practice versions of the API
    ├── main_old_basic.py
    └── main_old_psycopg2.py
```

## Note About Old Versions

The `old_versions/` folder contains earlier practice versions of this API.

* `main_old_basic.py` contains the first basic version using temporary list storage.
* `main_old_psycopg2.py` contains the raw PostgreSQL/psycopg2 version.

The current working version of the project is:

```text
main.py
```

## API Endpoints

| Method | Endpoint                    | Description                    |
| ------ | --------------------------- | ------------------------------ |
| GET    | `/`                         | Home route                     |
| POST   | `/expenses`                 | Create a new expense           |
| GET    | `/expenses`                 | Get all expenses               |
| GET    | `/expenses?category=Food`   | Filter expenses by category    |
| GET    | `/expenses?paid=true`       | Filter expenses by paid status |
| GET    | `/expenses?skip=0&limit=10` | Get expenses with pagination   |
| GET    | `/expenses/summary`         | Get expense summary            |
| GET    | `/expenses/{expense_id}`    | Get one expense by ID          |
| PUT    | `/expenses/{expense_id}`    | Update expense by ID           |
| DELETE | `/expenses/{expense_id}`    | Delete expense by ID           |

## Example Request Body

```json
{
  "title": "Lunch",
  "amount": 25,
  "category": "Food",
  "paid": true
}
```

## Example Responses

### Get All Expenses

```json
{
  "message": "Expenses fetched successfully",
  "skip": 0,
  "limit": 10,
  "expenses": [
    {
      "id": 1,
      "title": "Lunch",
      "amount": 25,
      "category": "Food",
      "paid": true
    }
  ]
}
```

### Expense Summary

```json
{
  "message": "Expense summary fetched successfully",
  "total_expenses": 5,
  "total_amount": 300,
  "paid_count": 3,
  "unpaid_count": 2
}
```

### Expense Not Found

```json
{
  "detail": "Expense not found"
}
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd expense-api
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL database

Create a PostgreSQL database for the project.

Example database name:

```text
expense_db
```

Then make sure your database connection inside `database.py` matches your local PostgreSQL username, password, host, port, and database name.

Example format:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/expense_db"
```

### 5. Run the FastAPI server

```bash
uvicorn main:app --reload
```

### 6. Open Swagger UI

Open this URL in your browser:

```text
http://127.0.0.1:8000/docs
```

## Query Parameter Examples

### Filter by category

```text
/expenses?category=Food
```

### Filter by paid status

```text
/expenses?paid=true
```

### Pagination

```text
/expenses?skip=0&limit=10
```

### Combined filter and pagination

```text
/expenses?category=Food&paid=true&skip=0&limit=10
```

## What I Learned

* How to create FastAPI routes
* How to use Pydantic schemas for request validation
* How to connect FastAPI with PostgreSQL
* How to use SQLAlchemy ORM
* How to create database models
* How to perform CRUD operations
* How to use path parameters
* How to use query parameters
* How to filter API results
* How to add pagination using `skip` and `limit`
* How to create a summary endpoint
* How to handle errors using `HTTPException`
* How to organize backend code into separate files
* How to manage project dependencies using `requirements.txt`
* How to test API endpoints using Swagger UI

## Future Improvements

* Add user authentication
* Add JWT login system
* Add date-based filtering
* Add search by title
* Add Docker support
* Deploy the API online
* Add automated tests

## Project Status

This project is completed as a serious backend practice project.

The next step is to build a new API from scratch to strengthen FastAPI, PostgreSQL, and SQLAlchemy skills before starting the first main portfolio project.

from fastapi import HTTPException
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel


app = FastAPI()
class Expense(BaseModel):
    title:str
    amount :float
    category : str
    paid: bool = False



def get_connection():
    return psycopg2.connect(
        dbname = "expense_db",
        user = "mhnkarim",
        host = "localhost",
        port = "5432"
    )


@app.get("/")
def home():
    return {
        "message":"Expense API with PostgreSQL"
    }

@app.get("/expenses")
def get_expenses():
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM expenses ORDER BY id;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return {
        "message": "expenses fetched from PostgreSQL",
        "expenses": [dict(row) for row in rows]
    }

@app.post("/expenses")
def add_expenses(expense:Expense):
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        INSERT into expenses(title,amount,category,paid)
        VALUES(%s,%s,%s,%s)
        RETURNING *;
    """,(expense.title,expense.amount,expense.category,expense.paid))
    new_expense = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return {
        "message": "expense added successfully",
        "expense": dict(new_expense)
    }

@app.get("/expenses/{expense_id}")
def get_expense_by_id(expense_id:int):
    connection = get_connection()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT * from expenses where id = %s;
    """, (expense_id,))
    expense = cursor.fetchone()
    cursor.close()
    connection.close()
    if expense is None:
        raise HTTPException(status_code=404,detail="expense not found")
    return {
        "message": "expense fetched from PostgreSQL",
        "expense": dict(expense)
    }
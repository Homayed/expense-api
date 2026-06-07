from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor



app = FastAPI()

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

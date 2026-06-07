from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class Expense(BaseModel):
    title: str
    amount: float
    category: str
    paid: bool = False

@app.get("/")
def home():
    return {
        "message": "hello"
    }

expenses = []
next_id = 1

@app.get("/expenses")
def get_expenses(category:str = None , paid:bool = None):
    filtered_expenses = []
    for expense in expenses:
        if category is not None and expense["category"]!=category:
            continue
        if paid is not None and expense["paid"]!=paid:
            continue
        filtered_expenses.append(expense)

    return {
        "message": "expenses shown successfully",
        "expenses": filtered_expenses
    }

@app.post("/expenses")
def add_expense(expense:Expense):
    global next_id
    new_expense = {
        "id": next_id,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "paid": expense.paid,
    }
    expenses.append(new_expense)
    next_id += 1
    return {
        "message": "expense added successfully",
        "expense": new_expense
    }

@app.get("/expenses/{expense_id}")
def find_expense(expense_id:int):
    for expense in expenses:
        if expense["id"] == expense_id:
            return {
                "message": "expense shown successfully",
                "expense": expense
            }
    raise HTTPException(status_code=404, detail= "expense not found")
@app.put("/expenses/{expense_id}")
def update_expense(expense_id:int, new_expense: Expense):
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["title"] = new_expense.title
            expense["amount"] = new_expense.amount
            expense["category"] = new_expense.category
            expense["paid"] = new_expense.paid
            return {
                "message": "expense updated successfully",
                "expense": expense
            }
    raise HTTPException(status_code=404, detail="expense not found")

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id:int):
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            return {
                "message": "expense deleted successfully",
                "expense": expense
            }
    raise HTTPException(status_code=404, detail="expense not found")

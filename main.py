
from fastapi import FastAPI, HTTPException , Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Expense
from schemas import ExpenseCreate

app = FastAPI()
Base.metadata.create_all(bind= engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Expense API is running with SQLAlchemy"
    }

@app.get("/expenses")
def get_expenses(category: str = None, paid: bool = None,skip: int = 0,
    limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(Expense)

    if category is not None:
        query = query.filter(Expense.category == category)

    if paid is not None:
        query = query.filter(Expense.paid == paid)

    expenses = query.offset(skip).limit(limit).all()

    return {
        "message": "Expenses fetched successfully",
        "expenses": expenses,
        "skip": skip,
        "limit": limit,
    }
@app.get("/expenses/summary")
def get_expense_summary(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()

    total_expenses = len(expenses)
    total_amount = 0
    paid_count = 0
    unpaid_count = 0

    for expense in expenses:
        total_amount += expense.amount

        if expense.paid == True:
            paid_count += 1
        else:
            unpaid_count += 1

    return {
        "message": "Expense summary fetched successfully",
        "total_expenses": total_expenses,
        "total_amount": total_amount,
        "paid_count": paid_count,
        "unpaid_count": unpaid_count
    }

@app.post("/expenses")
def add_expense(expense:ExpenseCreate,db:Session = Depends(get_db)):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        paid=expense.paid
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return {
        "message":"expense added successfully",
        "expense":new_expense
    }

@app.get("/expenses/{expense_id}")
def get_expense_by_id(expense_id:int, db:Session = Depends(get_db) ):
    expense = db.query(Expense).filter(Expense.id==expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {
        "message":"expense found successfully",
        "expense":expense
    }

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id:int, db:Session = Depends(get_db) ):
    expense = db.query(Expense).filter(Expense.id==expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()
    return {
        "message":"expense deleted successfully",
        "expense":expense
    }

@app.put("/expenses/{expense_id}")
def update_expense(expense_id:int,new_expense:ExpenseCreate, db:Session = Depends(get_db) ):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    expense.title = new_expense.title
    expense.amount = new_expense.amount
    expense.category = new_expense.category
    expense.paid = new_expense.paid

    db.commit()
    db.refresh(expense)

    return {
        "message":"expense updated successfully",
        "expense":expense
    }


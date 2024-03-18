from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine



app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    models.Base.metadata.create_all(bind=engine)
    


@app.post("/employees/", response_model=schemas.EmployeeResponse)
def create_user(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)


@app.get("/employees/", response_model=list[schemas.EmployeeResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_employees(db, skip=skip, limit=limit)
    return users


@app.get("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def read_user(emp_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_employee(db, emp_id=emp_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/employees/{emp_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    emp_id: int, employee_update: schemas.EmployeeCreate, db: Session = Depends(get_db)
):
    db_employee = crud.update_employee(db=db, emp_id=emp_id, employee_update=employee_update)
    if db_employee:
        return db_employee
    else:
        raise HTTPException(status_code=404, detail="Employee not found")


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_employee(db=db, emp_id=emp_id)
    if deleted_user:
        return deleted_user
    else:
        raise HTTPException(status_code=404, detail="Employee not found")
    

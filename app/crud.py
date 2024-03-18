from sqlalchemy.orm import Session

from . import models, schemas


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_user = models.Employee(name=employee.name, department=employee.department)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_employee(db: Session, emp_id: int, employee_update: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        for key, value in employee_update.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return db_employee
    return None

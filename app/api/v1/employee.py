from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.employee_schema import EmployeeCreate,EmployeeResponse
from app.services.employee_service import EmployeeService
from  typing import List
from app.core.security import get_current_user
router=APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@router.post("/",response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    return EmployeeService.create_employee(db, employee)

@router.get("/",response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db),current_user=Depends(get_current_user)):
    return EmployeeService.get_employees(db)


from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.department import Department
from app.schemas.department_schemas import DepartmentCreate,DepartmentResponse
from app.repositories.department_repository import DepartmentRepository
from app.services.department_service import DepartmentService
from typing import List
from app.schemas.employee_schema import EmployeeResponse
from app.services.employee_service import EmployeeService

router=APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

@router.post("/",response_model=DepartmentResponse)
def create_department(department:DepartmentCreate,db:Session=Depends(get_db)):
    return DepartmentService.create_department(db,department)
    

@router.get("/",response_model=list[DepartmentResponse])
def get_departments(db:Session=Depends(get_db)):
    return DepartmentService.get_departments(db)

@router.get("/{department_id}",response_model=DepartmentResponse)
def get_department_by_id(department_id:int,db:Session=Depends(get_db)):
    return DepartmentService.get_department_by_id(db,department_id)

@router.get(
    "/{department_id}/employees",
    response_model=List[EmployeeResponse]
)
def get_department_employees(
    department_id: int,
    db: Session = Depends(get_db)
):
    return EmployeeService.get_employees_by_department(
        db,
        department_id
    )
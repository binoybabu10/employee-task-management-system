from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.employee_repository import EmployeeRepository
from app.repositories.department_repository import DepartmentRepository
from app.schemas.employee_schema import EmployeeCreate

class EmployeeService:
    @staticmethod
    def create_employee(
        db:Session,
        employee:EmployeeCreate
    ):
        existing_employee=(
            EmployeeRepository.get_employee_by_email(db,employee.email)
        )
        if existing_employee:
            raise HTTPException(status_code=400,detail="Employee with this email already exists")
        department=DepartmentRepository.get_department_by_id(db,employee.department_id)
        if not department:
            raise HTTPException(status_code=400,detail="Department does not exist")
        return EmployeeRepository.create_employee(db,employee)
    

    @staticmethod
    def get_employees(db:Session):
        return EmployeeRepository.get_all_employees(db)
    
    @staticmethod
    def get_employees_by_department(db: Session, department_id: int):
        return EmployeeRepository.get_employees_by_department(db, department_id)
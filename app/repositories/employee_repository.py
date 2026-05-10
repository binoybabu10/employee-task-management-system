from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate

class EmployeeRepository:
    @staticmethod
    def create_employee(
        db:Session,
        employee:EmployeeCreate
    ):
        new_employee=Employee(
            name=employee.name,
            email=employee.email,
            department_id=employee.department_id,
            manager_id=employee.manager_id
        )
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee
    
    @staticmethod
    def get_all_employees(db:Session):
        employees=db.query(Employee).all()
        return employees
    
    @staticmethod
    def get_employee_by_email(db:Session,email:str):
        employee=db.query(Employee).filter(Employee.email==email).first()
        return employee
    
    @staticmethod
    def get_employees_by_department(db: Session, department_id: int):
        return db.query(Employee).filter(
        Employee.department_id == department_id
    ).all()
    

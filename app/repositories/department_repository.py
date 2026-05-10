from app.models.employee import Employee
from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department_schemas import DepartmentCreate


class DepartmentRepository:
    @staticmethod
    def create_department(
        db:Session,
        department:DepartmentCreate
    ):
        new_department=Department(department=department.department)
        db.add(new_department)
        db.commit()
        db.refresh(new_department)
        return new_department
    
    @staticmethod
    def get_all_departments(db:Session):
        departments=db.query(Department).all()
        return departments
    
    @staticmethod
    def get_departments_by_name(db:Session,department_name:str):
        department=db.query(Department).filter(Department.department==department_name).first()
        return department
    
    @staticmethod
    def get_department_by_id(db: Session, department_id: int):
        return db.query(Department).filter(
        Department.id == department_id
    ).first()

   


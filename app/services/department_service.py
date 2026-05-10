from fastapi import HTTPException
from sqlalchemy.orm import Session


from app.repositories.department_repository import DepartmentRepository
from app.schemas.department_schemas import DepartmentCreate

class DepartmentService:
    @staticmethod
    def create_department(
        db:Session,
        department:DepartmentCreate
    ):
        existing_department=(
            DepartmentRepository.get_departments_by_name(db,department.department)
        )
        if existing_department:
            raise HTTPException(status_code=400,detail="Department already exists")
        return DepartmentRepository.create_department(db,department)
    @staticmethod
    def get_departments(db:Session):
        return DepartmentRepository.get_all_departments(db)
    
    @staticmethod
    def get_department_by_id(db: Session, department_id: int):
        department = DepartmentRepository.get_department_by_id(db, department_id)
        if not department:
            raise HTTPException(status_code=404, detail="Department not found")
        return department
    
    
from pydantic import BaseModel
from typing import Optional

from app.schemas.department_schemas import DepartmentResponse
class EmployeeCreate(BaseModel):
    name:str
    email:str
    department_id:int
    manager_id:Optional[int]=None

class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:str
    department:DepartmentResponse
    manager_id:Optional[int]=None

    class Config:
        orm_mode=True    
from pydantic import BaseModel


class DepartmentCreate(BaseModel):#the model that will be used to create a department
    department:str

class DepartmentResponse(BaseModel):#the response model that will be returned
    id:int
    department:str
    

    class Config:#to tell pydantic to work with SQLAlchemy models
        orm_mode=True    
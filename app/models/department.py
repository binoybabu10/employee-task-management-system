from sqlalchemy import Column,Integer,String
from app.core.database import Base


class Department(Base):
    __tablename__="departments"
    id=Column(Integer,primary_key=True,index=True)
    department=Column(String(100),nullable=False,unique=True)

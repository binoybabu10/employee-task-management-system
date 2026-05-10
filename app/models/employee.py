from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    manager_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=True
    )

    # Relationship with Department
    department = relationship(
        "Department",
        backref="employees"
    )

    # Self relationship
    manager = relationship(
        "Employee",
        remote_side=[id]
    )
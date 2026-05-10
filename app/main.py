from fastapi import FastAPI
from sqlalchemy import text
from .core.database import engine,Base
from app.models.department import Department
from app.models.employee import Employee
from app.models.user import User
from app.api.v1.department import router as department_router
from app.api.v1.employee import router as employee_router
from app.api.v1.auth import router as user_router
app=FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(department_router)
app.include_router(employee_router)
app.include_router(user_router)
@app.get("/")
def home():
    return "API is working fine"

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        return {"message":"db connected"}
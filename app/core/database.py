from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from .config import settings

engine=create_engine(settings.DATABASE_URL)#creates db connection

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)#register db connection with sessionmaker to create db session

Base=declarative_base()#Base class for all the models to inherit from

def get_db():
    db=SessionLocal()
    try:
        yield db#dependency injection 
    finally:
        db.close()
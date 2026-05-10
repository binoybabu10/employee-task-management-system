from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth_schema import UserCreate

class UserRepository:
    @staticmethod
    def create_user(db: Session, user: UserCreate,hashed_password:str):
        new_user = User(
            username=user.username,
            email=user.email,
            password_hash=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user(db: Session):
        return db.query(User).all()


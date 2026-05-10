from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.auth_schema import UserCreate
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def register_user(db: Session, user: UserCreate):

        existing_user = UserRepository.get_user_by_email(db, user.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        existing_user = UserRepository.get_user_by_username(
            db,
            user.username
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        hashed_password = hash_password(user.password)

        return UserRepository.create_user(
            db,
            user,
            hashed_password
        )

    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str
    ):

        existing_user = UserRepository.get_user_by_email(
            db,
            email
        )

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(
            password,
            existing_user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            data={"sub": existing_user.email}
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    @staticmethod
    def get_user(db: Session):
        return UserRepository.get_user(db)
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth_schema import (
    UserCreate,
    TokenResponse,
    UserResponse
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Register User
@router.post("/", response_model=UserResponse)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return AuthService.register_user(db, user)


# Login User
@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return AuthService.login_user(
        db,
        form_data.username,
        form_data.password
    )


# Get All Users
@router.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return AuthService.get_user(db)
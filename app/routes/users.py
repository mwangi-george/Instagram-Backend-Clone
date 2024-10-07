from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..models import get_db
from ..services.users import UserServices
from ..schemas.users import (
    ActionConfirm,
    TokenCreate,
    UserCreate,

)


def create_user_router() -> APIRouter:
    router = APIRouter(prefix="/auth", tags=["Authentication"])

    # instantiate UserServices class with implementation logic
    user_services = UserServices()

    # ------------------User Sign Up--------------------------
    @router.post(path="/signup", response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
        response = user_services.create_user(user_data, db)
        formated_response = ActionConfirm(msg=response)
        return formated_response

    # ------------------User Login--------------------------
    @router.post(path="/login", response_model=TokenCreate, status_code=status.HTTP_200_OK)
    async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
        token = user_services.login_user(form_data.username, form_data.password, db)
        return token

    return router

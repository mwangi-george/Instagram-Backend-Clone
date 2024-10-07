from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..models import get_db
from ..services.users import UserServices
from ..schemas.users import (
    ActionConfirm,
    UserCreate
)


def create_user_router() -> APIRouter:
    router = APIRouter(prefix="/auth", tags=["Authentication"])

    # instantiate UserServices class with implementation logic
    user_services = UserServices()

    @router.post("/signup", response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
        response = user_services.create_user(user_data, db)
        formated_response = ActionConfirm(msg=response)
        return formated_response

    return router

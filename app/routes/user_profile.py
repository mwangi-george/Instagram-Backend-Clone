from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from ..models import get_db
from ..services.user_profile import UserProfileServices
from ..schemas.user_profile import UserProfileSchema


def create_user_profile_router() -> APIRouter:
    router = APIRouter(
        prefix="/user",
        tags=["user"],
    )
    user_profile_services = UserProfileServices()

    @router.get(
        path="/{username}",
        response_model=UserProfileSchema,
        status_code=status.HTTP_200_OK,
        name="user_profile",
        description="Get user profile by username",
    )
    async def get_user_profile(username: str, db: Session = Depends(get_db)) -> UserProfileSchema:
        user = user_profile_services.get_user_profile(username, db)
        return user

    return router

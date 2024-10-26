from sqlalchemy.orm import Session
from ..models import User
from fastapi import HTTPException, status


class UserProfileServices:
    def __init__(self):
        pass

    @staticmethod
    def get_user_profile(username: str, db: Session):
        user = db.query(User).filter_by(username=username).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        return user

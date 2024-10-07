from sqlalchemy import or_
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..models import User
from ..schemas.users import UserCreate


class UserServices:
    """ Class to manage users """
    def __init__(self):
        pass

    @staticmethod
    def create_user(user_data: UserCreate, db: Session):
        db_existing_user = db\
            .query(User)\
            .filter(or_(User.email == user_data.email, User.username == user_data.username))\
            .first()

        if db_existing_user:
            if db_existing_user.email == user_data.email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'email: {user_data.email} is already registered'
                )
            elif db_existing_user.username == user_data.username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f'username: {user_data.username} is not available'
                )
        else:
            db_user = User(
                email=user_data.email,
                username=user_data.username,
                password=user_data.password
            )
            try:
                db.add(db_user)
                db.commit()
                db.refresh(db_user)
                return f'{user_data.username} registered successfully'
            except Exception as e:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='Could not register user. Something went wrong!'
                )

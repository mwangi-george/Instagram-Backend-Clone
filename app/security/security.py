import os
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from passlib.context import CryptContext
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from ..models import User, get_db

load_dotenv()


class Security:
    def __init__(self):
        pass

    ALGORITHM = os.getenv('ALGORITHM')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES = 10
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
    ADMIN_EMAIL = os.getenv('EMAIL')
    ADMIN_EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    def get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, password, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    @staticmethod
    def get_user(username, db: Session) -> User | None:
        """ Query user by username from database """
        db_user = db.query(User).filter_by(username=username).first()
        return db_user

    def authenticate_user(self, username, password, db: Session) -> bool | User:
        """ Authenticate a user against the database """
        db_user = self.get_user(username, db)
        if not db_user:
            return False
        if not self.verify_password(password, db_user.password):
            return False
        return db_user

    def create_access_token(self, data: dict, for_password_reset: bool = False) -> str:
        """ Create an access token for authentication """
        try:
            to_encode = data.copy()
            if for_password_reset:
                expire = datetime.now(timezone.utc) + timedelta(minutes=self.PASSWORD_RESET_TOKEN_EXPIRE_MINUTES)
            else:
                expire = datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

            to_encode.update({'exp': expire})
            encoded_jwt = jwt.encode(to_encode, self.JWT_SECRET_KEY, algorithm=self.ALGORITHM)
            return encoded_jwt
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Could not validate credentials',
            )

    def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
        """ Get current user from token """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try:
            payload = jwt.decode(token, self.JWT_SECRET_KEY, algorithms=[self.ALGORITHM])
            username: str = payload.get('sub')
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = self.get_user(username, db)
        if not user:
            raise credentials_exception
        return user










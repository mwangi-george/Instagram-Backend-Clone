from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from .base import Base


class PasswordReset(Base):
    """ Table to hold password reset information. """
    __tablename__ = 'password_resets'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    reset_token = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    expires_at = Column(DateTime)

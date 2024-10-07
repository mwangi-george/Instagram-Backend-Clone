from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text

from .base import Base


class User(Base):
    """ Table for users """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    bio = Column(Text, nullable=True)
    name = Column(String(100), nullable=True)
    avatar_url = Column(Text, nullable=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


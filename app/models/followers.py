from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from .base import Base


class Follower(Base):
    """ Table model for followers """
    __tablename__ = 'followers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    follower_id = Column(Integer, ForeignKey('users.id'), unique=True)
    following_id = Column(Integer, ForeignKey('users.id'), unique=True)
    created_at = Column(DateTime, default=datetime.now)

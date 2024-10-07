from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey

from .base import Base


class Like(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    post_id = Column(Integer, ForeignKey('posts.id'), unique=True)
    created_at = Column(DateTime, default=datetime.now)

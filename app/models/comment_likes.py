from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text

from .base import Base


class CommentLike(Base):
    __tablename__ = 'comment_likes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    comment_id = Column(Integer, ForeignKey('comments.id'))
    created_at = Column(DateTime, default=datetime.now)

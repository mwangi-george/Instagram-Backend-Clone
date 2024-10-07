from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text

from .base import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    caption = Column(Text)
    media_url = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)



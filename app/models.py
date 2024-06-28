
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "fastapi_posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(String(500), nullable=False)
    published = Column(
        Boolean, server_default=sqlalchemy.sql.true(), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "fastapi_users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "fastapi_users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__ = "fastapi_votes"

    user_id = Column(Integer, ForeignKey("fastapi_users.id",
                     ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("fastapi_posts.id",
                     ondelete="CASCADE"), primary_key=True)

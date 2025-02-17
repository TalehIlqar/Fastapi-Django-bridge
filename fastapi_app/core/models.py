from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from .translation_models import BookTranslation, AuthorTranslation


class Book(Base):
    __tablename__ = "core_book"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("core_author.id"), nullable=False)
    author = relationship("Author", back_populates="books")
    translations = relationship(BookTranslation, back_populates="book")
    is_active = Column(Boolean, default=True)


class Author(Base):
    __tablename__ = "core_author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    translations = relationship(AuthorTranslation, back_populates="author")
    books = relationship("Book", back_populates="author")



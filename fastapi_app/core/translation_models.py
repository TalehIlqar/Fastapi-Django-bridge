from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base



class BookTranslation(Base):
    __tablename__ = "core_book_translation"

    id = Column(Integer, primary_key=True, index=True)
    language_code = Column(String(15), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    # is_active = Column(Boolean, default=True)
    master_id = Column(Integer, ForeignKey("core_book.id"), nullable=True)
    book = relationship("Book", back_populates="translations")


class AuthorTranslation(Base):
    __tablename__ = "core_author_translation"

    id = Column(Integer, primary_key=True, index=True)
    language_code = Column(String(15), nullable=False)
    bio = Column(String, nullable=True)
    master_id = Column(Integer, ForeignKey("core_author.id"), nullable=False)
    author = relationship("Author", back_populates="translations")
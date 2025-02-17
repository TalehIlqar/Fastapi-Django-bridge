from pydantic import BaseModel
from typing import List, Optional


class BookResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True


class BooksResponse(BaseModel):
    books: List[BookResponse]


class AuthorResponse(BaseModel):
    id: int
    name: str
    bio: Optional[str]
    books: List[BookResponse]

    class Config:
        orm_mode = True


class AuthorDetailResponse(BaseModel):
    id: int
    name: str
    bio: Optional[str]
    books: List[BookResponse]

    class Config:
        orm_mode = True
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from typing import List
from .models import (
    Book, Author
)
from .schemas import (
    BooksResponse, AuthorResponse, AuthorDetailResponse
)
from ..database import get_db

router = APIRouter()

@router.get("/books/", response_model=BooksResponse)
async def list_books(request: Request, db: AsyncSession = Depends(get_db)):
    locale = request.headers.get("Accept-Language", "en").split(",")[0]

    result = await db.execute(
        select(Book).options(joinedload(Book.translations))
    )
    book_list = result.unique().scalars().all()

    translated_books = []
    for book in book_list:
        translation = next((t for t in book.translations if t.language_code == locale), None)
        if translation:
            translated_books.append({
                "id": book.id,
                "title": translation.title,
                "description": translation.description,
            })

    return {"books": translated_books}

@router.get("/authors/", response_model=List[AuthorResponse])
async def list_authors(request: Request, db: AsyncSession = Depends(get_db)):
    locale = request.headers.get("Accept-Language", "en").split(",")[0]

    try:
        result = await db.execute(
            select(Author).options(joinedload(Author.translations), joinedload(Author.books.and_(Book.is_active.is_(True))).joinedload(Book.translations))
        )
        authors = result.unique().scalars().all()

        translated_authors = []
        for author in authors:
            translation = next((t for t in author.translations if t.language_code == locale), None)
            if not translation:
                translation = next((t for t in author.translations if t.language_code == "en"), None)

            books = []
            for book in author.books:
                book_translation = next((t for t in book.translations if t.language_code == locale), None)
                if not book_translation:
                    book_translation = next((t for t in book.translations if t.language_code == "en"), None)

                if book_translation:
                    books.append({
                        "id": book.id,
                        "title": book_translation.title,
                        "description": book_translation.description,
                    })

            if translation:
                translated_authors.append({
                    "id": author.id,
                    "name": author.name,
                    "bio": translation.bio,
                    "books": books
                })

        return  translated_authors

    except Exception as e:
        return {"error": str(e)}


@router.get("/authors/{author_id}/", response_model=AuthorDetailResponse)
async def get_author_detail(author_id: int, request: Request, db: AsyncSession = Depends(get_db)):
    locale = request.headers.get("Accept-Language", "en").split(",")[0]

    # Müəllifi ID-yə əsasən gətir
    result = await db.execute(
        select(Author)
        .where(Author.id == author_id)
        .options(
            joinedload(Author.translations),
            joinedload(Author.books).joinedload(Book.translations)
        )
    )
    author = result.unique().scalars().one_or_none()  # Dəyişiklik burada edildi

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    # Müəllif tərcüməsi
    translation = next((t for t in author.translations if t.language_code == locale), None)
    if not translation:
        translation = next((t for t in author.translations if t.language_code == "en"), None)

    # Kitablar tərcüməsi
    books = []
    for book in author.books:
        book_translation = next((t for t in book.translations if t.language_code == locale), None)
        if not book_translation:
            book_translation = next((t for t in book.translations if t.language_code == "en"), None)

        if book_translation:
            books.append({
                "id": book.id,
                "title": book_translation.title,
                "description": book_translation.description,
            })

    return {
        "id": author.id,
        "name": author.name,
        "bio": translation.bio if translation else None,
        "books": books
    }

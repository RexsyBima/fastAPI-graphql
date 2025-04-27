import strawberry
from typing import List, Optional

from app.store import get_book_by_title, get_books, get_book_by_id, create_book, update_book, delete_book

@strawberry.type
class Book:
    id: strawberry.ID
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        return [Book(id=b["id"], title=b["title"], author=b["author"]) for b in get_books()]

    @strawberry.field
    def book_by_id(self, id: strawberry.ID) -> Optional[Book]:
        b = get_book_by_id(str(id))
        if b is None:
            return None
        return Book(id=b["id"], title=b["title"], author=b["author"])


    @strawberry.field
    def book_by_title(self, title: str) -> Optional[Book]:
        b = get_book_by_title(str(title))
        if b is None:
            return None
        return Book(id=b["id"], title=b["title"], author=b["author"])

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self, title: str, author: str) -> Book:
        b = create_book(title, author)
        return Book(id=b["id"], title=b["title"], author=b["author"])

    @strawberry.mutation
    def update_book(self, id: strawberry.ID, title: Optional[str] = None, author: Optional[str] = None) -> Optional[Book]:
        b = update_book(str(id), title, author)
        if b is None:
            return None
        return Book(id=b["id"], title=b["title"], author=b["author"])

    @strawberry.mutation
    def delete_book(self, id: strawberry.ID) -> bool:
        return delete_book(str(id))



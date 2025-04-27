import uuid
from typing import Optional

class Store:
    def __init__(self):
        self._books = []

    @property
    def books(self):
        return self._books

store = Store()

def get_books():
    return store.books

def get_book_by_id(book_id: str) -> Optional[dict]:
    return next((b for b in store.books if b["id"] == book_id), None)

def get_book_by_title(book_title: str) -> Optional[dict]:
    return next((b for b in store.books if b["title"] == book_title), None)

def create_book(title: str, author: str) -> dict:
    new_book = {"id": str(uuid.uuid4()), "title": title, "author": author}
    store.books.append(new_book)
    return new_book

def update_book(book_id: str, title: Optional[str] = None, author: Optional[str] = None) -> Optional[dict]:
    book = get_book_by_id(book_id)
    if not book:
        return None
    if title is not None:
        book["title"] = title
    if author is not None:
        book["author"] = author
    return book

def delete_book(book_id: str) -> bool:
    book = get_book_by_id(book_id)
    if not book:
        return False
    store.books.remove(book)
    return True

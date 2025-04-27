from typing import List
import strawberry

@strawberry.type
class Book:
    title: str
    author: str

def get_books():
    return [
        Book(title="Book 1", author="Author 1"),
        Book(title="Book 2", author="Author 2"),
    ]

@strawberry.type
class Query:
    books: List[Book] = strawberry.field(resolver=get_books)



from app.schema import Book

def get_books():
    return [
        Book(title="Book 1", author="Author 1"),
        Book(title="Book 2", author="Author 2"),
    ]

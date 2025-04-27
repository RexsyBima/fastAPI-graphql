# fastapi-graphql: Book Library API

A simple GraphQL API for managing a book library, built with FastAPI and Strawberry GraphQL. Supports in-memory CRUD operations for books and provides an interactive GraphQL Playground.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Server](#running-the-server)
- [API Usage](#api-usage)
  - [GraphQL Endpoint](#graphql-endpoint)
  - [Sample Queries](#sample-queries)
  - [Sample Mutations](#sample-mutations)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, Read, Update, Delete (CRUD) operations for books
- In-memory data store (no external database required)
- GraphQL schema powered by Strawberry GraphQL
- Interactive GraphQL Playground

## Prerequisites

- Python 3.10+ (as required by the project)
- pip (or poetry)

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd fastapi-graphql
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or using Poetry:
   ```bash
   poetry install
   ```

## Running the Server

Start the FastAPI server with Uvicorn:
```bash
uvicorn run:app --reload
```
- Server: http://127.0.0.1:8000
- GraphQL Playground: http://127.0.0.1:8000/graphql

## API Usage

### GraphQL Endpoint

All interactions use the GraphQL endpoint:
```
POST http://127.0.0.1:8000/graphql
```

### Sample Queries

- Get all books:
  ```graphql
  query {
    books {
      id
      title
      author
    }
  }
  ```

- Get a book by ID:
  ```graphql
  query {
    bookById(id: "BOOK_ID_HERE") {
      id
      title
      author
    }
  }
  ```

- Get a book by title:
  ```graphql
  query {
    bookByTitle(title: "The Hobbit") {
      id
      title
      author
    }
  }
  ```

### Sample Mutations

- Create a new book:
  ```graphql
  mutation {
    createBook(title: "1984", author: "George Orwell") {
      id
      title
      author
    }
  }
  ```

- Update a book:
  ```graphql
  mutation {
    updateBook(id: "BOOK_ID_HERE", title: "Animal Farm") {
      id
      title
      author
    }
  }
  ```

- Delete a book:
  ```graphql
  mutation {
    deleteBook(id: "BOOK_ID_HERE")
  }
  ```

## Project Structure

```
.  
├── app
│   ├── __init__.py
│   ├── schema.py    # GraphQL schema definitions
│   └── store.py     # In-memory data store
├── run.py           # FastAPI application entry point
├── requirements.txt # Python dependencies
├── pyproject.toml   # Project metadata
└── README.md        # Project documentation
```

## Development

- Format and lint code as configured
- Add tests (currently none included)
- Submit changes via pull requests

## Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

## License

This project does not include a license. Add a LICENSE file to specify licensing terms.

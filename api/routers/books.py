from fastapi import APIRouter, Body

router = APIRouter()

BOOKS = [
    {"title": "Title one", "author": "Author one", "category": "science"},
    {"title": "Title two", "author": "Author two", "category": "science"},
    {"title": "Title three", "author": "Author three", "category": "history"},
    {"title": "Title four", "author": "Author four", "category": "math"},
    {"title": "Title five", "author": "Author five", "category": "math"},
]


@router.get("/books")
async def get_books():
    return BOOKS


@router.get("/books/{dynamic_query}/")
async def get_books_by_query(book_author: str, category: str):

    books_to_return = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == book_author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            books_to_return.append(book)

    return books_to_return


@router.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@router.put("/books/update_book")
async def update_book(updated=Body()):
    for book in enumerate(BOOKS):
        if book.get("title").casefold() == updated.get("title").casefold():
            book = updated


@router.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i, book in enumerate(BOOKS):
        if book.get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

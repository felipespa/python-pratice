from fastapi import FastAPI
from api.routers import books, todos


app = FastAPI()

app.include_router(books.router)
app.include_router(todos.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

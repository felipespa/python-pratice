from fastapi import FastAPI
from api.routers import users, books

app = FastAPI()

# app.include_router(users.router)
app.include_router(books.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

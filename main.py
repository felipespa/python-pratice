from fastapi import FastAPI
import models.models as models
from api.routers import admin, books, users, todos
from database.database import engine


# test1234!


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(admin.router)
app.include_router(books.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

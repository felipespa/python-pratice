from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Annotated
from starlette import status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from .auth import get_current_user

from database.database import SessionLocal, engine

import models.models as models
from models.models import Todos


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/admin", tags=["admin"])
db_dependecy = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependecy):
    if user is None or user.get("user_role") != "admin":
        raise HTTPException(status_code=401, detail="Authentication Failed")

    return db.query(Todos).all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    user: user_dependency, db: db_dependecy, todo_id: int = Path(gt=0)
):
    if user is None or user.get("user_role") != "admin":
        raise HTTPException(status_code=401, detail="Authentication Failed")

    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

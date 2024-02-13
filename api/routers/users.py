from fastapi import APIRouter, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional
from starlette import status

router = APIRouter()


class User:
    id: int
    name: str
    email: str
    role: str
    created_at: int

    def __init__(
        self, id: int, name: str, email: str, role: str, created_at: int
    ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.role = role
        self.created_at = created_at


class UserRequest(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3)
    email: str = Field(min_length=12)
    role: str = Literal["admin", "bar"]
    created_at: int = Field(gt=1999, lt=2031)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Teste user",
                "email": "teste@email.com",
                "role": "admin",
            }
        }


USERS = [
    User(1, "Felipe", "felipin@email.com", "admin", 2024),
    User(2, "Fernandin", "fernandin@email.com", "admin", 2024),
    User(3, "Momozin", "momozinha@email.com", "user", 2024),
    User(4, "Teste", "teste@email.com", "user", 2024),
    User(5, "Usuário", "usuario@email.com", "admin", 2024),
]


def find_user_by_id(user_id: int):
    if len(USERS) > 0:
        for user in USERS:
            if user.id == user_id:
                return user


@router.get("/users", status_code=status.HTTP_200_OK)
async def get_users():
    return USERS


@router.get("/user/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int):
    return find_user_by_id(user_id) | []


@router.post("/create_user", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest):
    existed_user = find_user_by_id(user_request.id) | None

    if existed_user is None:
        new_user = User(**user_request.model_dump())
        new_user.id = 1 if len(USERS) == 0 else USERS[-1].id + 1
        USERS.append(new_user)
    else:
        raise HTTPException(status_code=404, detail="User already exist")


@router.delete("/user/{user_id}")
async def delete_user(user_id: int):
    if len(USERS) > 0:
        for i, user in USERS:
            if user.id == user_id:
                USERS.pop(i)
                break

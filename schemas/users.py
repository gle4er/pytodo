from pydantic import BaseModel

from schemas.tasks import Task


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    tasks: list[Task] = []

    class Config:
        orm_mode = True

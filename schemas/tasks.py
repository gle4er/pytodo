from typing import List
from pydantic import BaseModel, validator


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner: List[int] = []

    class Config:
        orm_mode = True

    @validator("owner", pre=True)
    def parse_owner(cls, v):
        if isinstance(v, list):
            return [i.id for i in v]
        return v.id

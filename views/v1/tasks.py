from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import session
import internal.tasks as internal
import schemas.tasks as schema


task_router = r = APIRouter()


@r.post("/users/{user_id}/tasks/", response_model=schema.Task)
def create_task_for_user(
    user_id: int,
    task: schema.TaskCreate,
    db: Session = Depends(session.get_db),
):
    return internal.create_user_task(db=db, task=task, user_id=user_id)


@r.get("/items/", response_model=list[schema.Task])
def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(session.get_db),
):
    tasks = internal.get_tasks(db, skip=skip, limit=limit)
    return tasks

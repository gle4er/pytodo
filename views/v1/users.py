from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.db import session
import internal.users as internal
import schemas.users as schema

user_router = r = APIRouter()


@r.post("/users/", response_model=schema.User)
def create_user(
    user: schema.UserCreate,
    db: Session = Depends(session.get_db),
):
    db_user = internal.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return internal.create_user(db=db, user=user)


@r.get("/users/", response_model=list[schema.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(session.get_db),
):
    users = internal.get_users(db, skip=skip, limit=limit)
    return users


@r.get("/users/{user_id}", response_model=schema.User)
def read_user(
    user_id: int,
    db: Session = Depends(session.get_db),
):
    db_user = internal.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

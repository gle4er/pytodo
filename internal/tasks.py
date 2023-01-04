from sqlalchemy.orm import Session

from models.tasks import Task
from models.users import User
import schemas.tasks as schema


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def create_user_task(db: Session, task: schema.TaskCreate, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    db_item = Task(**task.dict(), owner=[user])
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

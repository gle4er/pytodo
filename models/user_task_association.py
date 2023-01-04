from sqlalchemy import Column, ForeignKey, Integer, Index, Table

from core.db.base_class import Base


user_task_association = Table(
    "user_task_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
    Column("task_id", Integer, ForeignKey("task.id"), primary_key=True),
    Index("idx_user_task_uniq", "user_id", "task_id", unique=True),
)

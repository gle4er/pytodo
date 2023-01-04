from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.db.base_class import Base
from models.user_task_association import user_task_association


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    owner = relationship(
        "User",
        secondary=user_task_association,
        back_populates="tasks",
    )

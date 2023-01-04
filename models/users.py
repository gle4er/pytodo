from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.db.base_class import Base
from models.user_task_association import user_task_association


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    tasks = relationship(
        "Task",
        secondary=user_task_association,
        back_populates="owner",
    )

import typing as T
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from quarkboard.constants import MAX_TITLE_LENGTH
from quarkboard.models.base import BaseModel

if T.TYPE_CHECKING:
    from quarkboard.models.task import Task


class Project(BaseModel):
    __tablename__ = "projects"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(MAX_TITLE_LENGTH))
    tasks: Mapped[list["Task"]] = relationship(back_populates="project")

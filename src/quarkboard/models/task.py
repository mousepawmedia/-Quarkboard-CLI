from sqlalchemy import String
from sqlalchemy.orm import ForeignKey, Mapped, mapped_column, relationship
from quarkboard.constants import MAX_TITLE_LENGTH, MAX_DESCRIPTION_LENGTH
from quarkboard.models.base import BaseModel
from quarkboard.models.static import (
    Impact,
    Gravity,
    Priority,
    Distance,
    Friction,
    Relativity,
    Origin,
    Caught,
    Status
)
from quarkboard.models.user import User
from quarkboard.models.project import Project


class Task(BaseModel):
    __tablename__ = "tasks"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(MAX_TITLE_LENGTH))
    description: Mapped[str] = mapped_column(String(MAX_DESCRIPTION_LENGTH))

    project: Mapped["Project"] = relationship(back_populates="tasks")
    project_pk: Mapped[int] = mapped_column(ForeignKey("projects.pk"))

    impact: Mapped["Impact"] = relationship()
    gravity: Mapped["Gravity"] = relationship()
    priority: Mapped["Priority"] = relationship()

    phases: Mapped[list["TaskPhase"]] = relationship(mapped_column="task")

    origin: Mapped["Origin"] = relationship()
    caught: Mapped["Caught"] = relationship()
    volatility: Mapped[int] = mapped_column()

    status: Mapped["Status"] = relationship()


class TaskPhase(BaseModel):
    __tablename__ = "task_phases"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(MAX_TITLE_LENGTH))
    description: Mapped[str] = mapped_column(String(MAX_DESCRIPTION_LENGTH))

    task: Mapped["Task"] = relationship(back_populates="phases")
    task_pk: Mapped[int] = mapped_column(ForeignKey("tasks.pk"))

    distance: Mapped["Distance"] = relationship()
    friction: Mapped["Friction"] = relationship()
    relativity: Mapped["Relativity"] = relationship()
    energy_points: Mapped[int] = mapped_column()

    assignee: Mapped["User"] = relationship()
    assignee_pk: Mapped[int] = mapped_column(ForeignKey("users.pk"))

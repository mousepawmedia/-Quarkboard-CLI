from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from quarkboard.constants import MAX_TITLE_LENGTH
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


class Task(BaseModel):
    __tablename__ = "status"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(MAX_TITLE_LENGTH))
    description: Mapped[str] = mapped_column()

    impact: Mapped[Impact] = relationship()
    gravity: Mapped[Gravity] = relationship()
    priority: Mapped[Priority] = relationship()

    distance: Mapped[Distance] = relationship()
    friction: Mapped[Friction] = relationship()
    relativity: Mapped[Relativity] = relationship()
    energy_points: Mapped[int] = mapped_column()

    origin: Mapped[Origin] = relationship()
    caught: Mapped[Caught] = relationship()
    volatility: Mapped[int] = mapped_column()

    status: Mapped[Status] = relationship()
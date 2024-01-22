from sqlalchemy.orm import Mapped, mapped_column
from quarkboard.models.base import BaseModel


class Impact(BaseModel):
    __tablename__ = "impact"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()


class Gravity(BaseModel):
    __tablename__ = "gravity"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()


class Priority(BaseModel):
    __tablename__ = "priority"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()

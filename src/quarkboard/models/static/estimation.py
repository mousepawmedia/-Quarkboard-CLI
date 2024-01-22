from sqlalchemy.orm import Mapped, mapped_column
from quarkboard.models.base import BaseModel


class Distance(BaseModel):
    __tablename__ = "distance"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()


class Friction(BaseModel):
    __tablename__ = "friction"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()


class Relativity(BaseModel):
    __tablename__ = "relativity"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()

from sqlalchemy.orm import Mapped, mapped_column
from quarkboard.models.base import BaseModel


class Origin(BaseModel):
    __tablename__ = "origin"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()


class Caught(BaseModel):
    __tablename__ = "caught"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    score: Mapped[int] = mapped_column()


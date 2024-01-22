from sqlalchemy.orm import Mapped, mapped_column
from quarkboard.models.base import BaseModel


class Status(BaseModel):
    __tablename__ = "status"

    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

import typing as T
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from quarkboard.constants import (
    MAX_USERNAME_LENGTH, 
    MAX_EMAIL_LENGTH
)
from quarkboard.models.base import BaseModel

if T.TYPE_CHECKING:
    from quarkboard.models.oauth import OAuth


class User(BaseModel):
    __tablename__ = "user"

    pk: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(MAX_USERNAME_LENGTH))
    email: Mapped[str] = mapped_column(String(MAX_EMAIL_LENGTH))
    oauth_users: Mapped[list["OAuth"]] = relationship(
        back_populates="user"
    )

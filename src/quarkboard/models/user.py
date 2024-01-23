import typing as T
from sqlalchemy import String
from sqlalchemy.orm import ForeignKey, Mapped, mapped_column, relationship
from quarkboard.constants import (
    MAX_USERNAME_LENGTH,
    MAX_EMAIL_LENGTH,
    MAX_OAUTH_LENGTH
)
from quarkboard.models.base import BaseModel


if T.TYPE_CHECKING:
    from quarkboard.models.task import TaskPhase


class User(BaseModel):
    __tablename__ = "users"

    pk: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(MAX_USERNAME_LENGTH))
    email: Mapped[str] = mapped_column(String(MAX_EMAIL_LENGTH))
    oauth_users: Mapped[list["OAuthUser"]] = relationship(
        back_populates="user"
    )

    tasks: Mapped[list["TaskPhase"]] = relationship(back_populates="assignee")


class OAuthUser(BaseModel):
    __tablename__ = "oauth_users"

    pk: Mapped[int] = mapped_column(primary_key=True)
    provider_uri: Mapped[str] = mapped_column(String(MAX_OAUTH_LENGTH))
    oauth_id: Mapped[str] = mapped_column(String(MAX_OAUTH_LENGTH))

    user_pk: Mapped[int] = mapped_column(ForeignKey("users.pk"))
    user: Mapped["User"] = relationship(back_populates="oauth_user")

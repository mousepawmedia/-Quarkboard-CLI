from sqlalchemy import String
from sqlalchemy.orm import ForeignKey, Mapped, mapped_column, relationship
from quarkboard.constants import MAX_OAUTH_LENGTH
from quarkboard.models.base import BaseModel
from quarkboard.models.user import User


class OAuth(BaseModel):
    __tablename__ = "oauth"

    pk: Mapped[int] = mapped_column(primary_key=True)
    provider_uri: Mapped[str] = mapped_column(String(MAX_OAUTH_LENGTH))
    oauth_id: Mapped[str] = mapped_column(String(MAX_OAUTH_LENGTH))

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="oauth_user")

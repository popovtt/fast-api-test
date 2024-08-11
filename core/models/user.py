from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile


class User(Base):
    username: Mapped[str] = mapped_column(String(30), unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(username={self.username!r}, id={self.id})"

    def __repr__(self):
        return str(self)

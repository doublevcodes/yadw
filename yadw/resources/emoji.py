from typing import Optional

from pydantic import BaseModel

from .role import Role
from .user import User

__all__ = ("Emoji",)


class Emoji(BaseModel):
    id: int
    name: Optional[str]
    roles: list[Role]
    user: Optional[User]
    require_colons: Optional[bool]
    managed: Optional[bool]
    animated: Optional[bool]
    available: Optional[bool]

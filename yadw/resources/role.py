from typing import Optional

from pydantic import BaseModel

from .permissions import Permissions


class RoleTag(BaseModel):
    bot_id: Optional[int]
    integration_id: Optional[int]
    premium_subscriber: Optional[bool]


class Role(BaseModel):
    id: int
    name: str
    color: int
    hoist: bool
    position: int
    permissions: Permissions
    managed: bool
    mentionable: bool

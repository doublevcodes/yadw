from typing import Optional

from pydantic import BaseModel

from yadw.resources.user import User

from .guild import Guild
from .user import User

__all__ = ("GuildTemplate",)


class GuildTemplate(BaseModel):
    code: str
    name: str
    description: Optional[str]
    usage_count: int
    creator_id: int
    creator: User
    created_at: str
    updated_at: str
    source_guild_id: int
    serialized_source_guild: Optional[Guild]
    is_dirty: Optional[bool]

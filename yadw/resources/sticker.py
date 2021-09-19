from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from .user import User


class Sticker(BaseModel):
    id: int
    pack_id: Optional[int]
    name: str
    description: Optional[str]
    tags: Optional[str]
    asset: str
    type: int
    format_type: int
    available: Optional[bool]
    guild_id: int
    user: Optional[User]
    sort_value: Optional[int]


class StickerTypes(IntEnum):
    pass


class StickerFormat(IntEnum):
    pass


class StickerItem(BaseModel):
    pass


class StickerPack(BaseModel):
    pass

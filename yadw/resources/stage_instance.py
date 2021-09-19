from enum import IntEnum

from pydantic import BaseModel


class StageInstance(BaseModel):
    id: int
    guild_id: int
    channel_id: int
    topic: str
    privacy_level: int
    discorverable_disabled: bool


class PrivacyLevel(IntEnum):
    PUBLIC: 1
    GUILD_ONLY: 2

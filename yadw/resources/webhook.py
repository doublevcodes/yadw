from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from .channel import Channel
from .guild import Guild
from .user import User


class Webhook(BaseModel):
    id: int
    type: int
    guild_id: Optional[int]
    channel_id: Optional[int]
    user: Optional[User]
    name: Optional[str]
    avatar: Optional[str]
    token: Optional[str]
    application_id: Optional[int]
    source_guild: Optional[Guild]
    source_channel: Optional[Channel]
    url: Optional[str]


class WebhookTypes(IntEnum):
    INCOMING = 1
    CHANNEL_FOLLOWER = 2
    APPLICATION = 3

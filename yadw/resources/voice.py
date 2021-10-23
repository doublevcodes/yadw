from typing import Optional

# from .guild import GuildMember
from pydantic import BaseModel


class VoiceState(BaseModel):
    guild_id: Optional[int]
    channel_id: Optional[int]
    user_id: int
    # member: Optional[GuildMember]
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: bool
    self_video: bool
    suppress: bool
    request_to_speak: str


class VoiceRegion(BaseModel):
    id: str
    name: str
    vip: bool
    optimal: bool
    deprecated: bool
    custom: bool

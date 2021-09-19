from typing import Optional

from pydantic import BaseModel

from .user import User

__all__ = ("Channel",)


class Channel(BaseModel):
    id: int
    type: int
    guild_id: Optional[int]
    position: Optional[int]
    permission_overwrites: Optional[list]
    name: Optional[str]
    topic: Optional[str]
    nsfw: Optional[bool]
    last_message_id: Optional[int]
    bitrate: Optional[int]
    user_limit: Optional[int]
    rate_limit_per_user: Optional[int]
    recipients: Optional[list[User]]
    icon: Optional[str]
    owner_id: Optional[int]
    application_id: Optional[int]
    parent_id: Optional[int]
    last_pin_timestamp: Optional[str]
    rtc_region: Optional[str]
    video_quality_mode: Optional[int]
    message_count: Optional[int]
    member_count: Optional[int]
    # thread_metadata:
    # member:
    default_auto_archive_duration: Optional[int]
    permissions: Optional[str]

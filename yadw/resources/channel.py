from enum import IntEnum
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


class ChannelTypes(IntEnum):
    GUILD_TEXT: 0
    DM: 1
    GUILD_VOICE: 2
    GROUP_DM: 3
    GUILD_CATEGORY: 4
    GUILD_NEWS: 5
    GUILD_STORE: 6
    GUILD_NEWS_THREAD: 10
    GUILD_PUBLIC_THREAD: 11
    GUILD_PRIVATE_THREAD: 12
    GUILD_STAGE_VOICE: 13


class VideoQualityModes(IntEnum):
    AUTO: 1
    FULL: 2


class Message(BaseModel):
    pass


class MessageType(IntEnum):
    pass


class MessageActivity(BaseModel):
    pass


class MessageActivityTypes(IntEnum):
    pass


class MessageFlags(IntEnum):
    pass


class MessageReference(BaseModel):
    pass


class FollowedChannel(BaseModel):
    pass


class Reaction(BaseModel):
    pass


class Overwrite(BaseModel):
    pass


class ThreadMetadata(BaseModel):
    pass


class ThreadMember(BaseModel):
    pass


class Embed(BaseModel):
    pass


class EmbedType(BaseModel):
    pass


class EmbedThumbnail(BaseModel):
    pass


class EmbedVideo(BaseModel):
    pass


class EmbedImage(BaseModel):
    pass


class EmbedProvider(BaseModel):
    pass


class EmbedAuthor(BaseModel):
    pass


class EmbedFooter(BaseModel):
    pass


class EmbedField(BaseModel):
    pass


class Attachement(BaseModel):
    pass


class ChannelMention(BaseModel):
    pass


class AllowedMentionType(BaseModel):
    pass


class AllowedMention(BaseModel):
    pass


# Not sure how to implement a limit class
# class EmbedLimits(IntEnum):
#     pass

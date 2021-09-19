from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from .emoji import Emoji
from .role import Role


class ExplicitContentFilterLevel(IntEnum):
    DISABLED = 0
    MEMBER_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class VerificationLevel(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


GUILD_FEATURES = [
    "ANIMATED_ICON",
    "BANNER",
    "COMMERCE",
    "COMMUNITY",
    "DISCOVERABLE",
    "FEATURABLE",
    "INVITE_SPLASH",
    "MEMBER_VERIFICATION_GATE_ENABLED",
    "NEWS",
    "PARTNERED",
    "PREVIEW_ENABLED",
    "VANITY_URL",
    "VERIFIED",
    "VIP_REGIONS",
]


class Guild(BaseModel):
    id: int
    name: str
    icon: Optional[str]
    icon_hash: Optional[str]
    splash: Optional[str]
    discovery_splash: Optional[str]
    owner: Optional[bool]
    owner_id: int
    permissions: Optional[str]
    afk_channel_id: Optional[int]
    afk_timeout: int
    widget_enabled: Optional[bool]
    widget_channel_id: Optional[int]
    verification_level: VerificationLevel
    default_message_notifications: DefaultMessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: list[Role]
    emojis: list[Emoji]

from enum import IntEnum, IntFlag
from typing import Optional

from pydantic import BaseModel


class PremiumType(IntEnum):
    none = 0
    nitro_classic = 1
    nitro = 2


class UserFlag(IntFlag):
    discord_employee = 1 << 0
    partnered_server_owner = 1 << 1
    hypesquad_events = 1 << 2
    bug_hunter_level_1 = 1 << 3
    house_bravery = 1 << 6
    house_brilliance = 1 << 7
    house_balance = 1 << 8
    early_supporter = 1 << 9
    team_user = 1 << 10
    bug_hunter_level_2 = 1 << 14
    verified_bot = 1 << 16
    early_verified_bot_developer = 1 << 17
    discord_certified_moderator = 1 << 18


class User(BaseModel):
    id: int
    username: str
    discriminator: str
    avatar: Optional[str]
    bot: Optional[bool]
    system: Optional[bool]
    mfa_enabled: Optional[bool]
    banner: Optional[str]
    accent_color: Optional[int]
    locale: Optional[str]
    verified: Optional[bool]
    email: Optional[bool]
    flags: Optional[int]
    premium_type: Optional[PremiumType]
    public_flags: Optional[int]

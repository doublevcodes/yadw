from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

# from .application import Application
from .channel import Channel
from .guild import Guild
from .stage_instance import StageInstance
from .user import User


class Invite(BaseModel):
    code: str
    guild: Optional[Guild]
    channel: Channel
    inviter: Optional[User]
    target_type: Optional[int]
    target_user: Optional[User]
    # target_application: Optional[Application]
    approximate_presence_count: Optional[int]
    approximate_member_count: Optional[int]
    expires_at: Optional[str]
    stage_instance: Optional[StageInstance]


class InviteTarget(IntEnum):
    pass


class InviteMetaData(BaseModel):
    pass


class InviteStageInstance(BaseModel):
    pass

from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from yadw.resources.application_command import ApplicationCommandType
from yadw.resources.user import User


class ResolvedData(BaseModel):
    users = Optional[dict[int, User]]
    members = Optional[
        dict[int, "PartialUser"]
    ]  # Partial users have not been implemented
    roles = Optional[dict[int, "Role"]]  # Roles have not been implemented
    channels = Optional[dict[int, "PartialChannel"]]  # Not implemented
    messages = Optional[dict[int, "PartialMessage"]]  # Not implemented


class InteractionData(BaseModel):
    id: int
    name: str
    type: ApplicationCommandType
    resolved: Optional[ResolvedData]


class InteractionType(IntEnum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3


class Interaction(BaseModel):
    id: int
    application_id: int
    type: InteractionType

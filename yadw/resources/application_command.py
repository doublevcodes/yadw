from enum import IntEnum
from typing import Optional, Union

from pydantic import BaseModel


class ApplicationCommandOptionChoice(BaseModel):
    name: str
    value: Union[str, int, float]


class ApplicationCommandOptionType(IntEnum):
    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10


class ApplicationCommandOption(BaseModel):
    type: ApplicationCommandOptionType
    name: str
    description: str
    required: Optional[bool]
    choices: list[ApplicationCommandOptionChoice]
    options: list["ApplicationCommandOption"]


class ApplicationCommandType(IntEnum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3


class ApplicationCommand(BaseModel):
    id: int
    type: Optional[ApplicationCommandType]
    application_id: int
    guild_id: Optional[int]
    name: str
    description: str
    options: list[ApplicationCommandOption]
    default_permission: bool
    version: int

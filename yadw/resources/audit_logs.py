from enum import IntEnum
from typing import Optional

from pydantic import BaseModel

from .channel import Channel
from .user import User
from .webhooks import Webhook

__all__ = ("AuditLogs",)


class AuditLog(BaseModel):
    webhooks: list[Webhook]
    users: list[User]
    # audit_log_entries: Optional[list[audit_log_entries]]
    # integrations: Optional[list[integrations]]
    threads: list[Channel]


class AuditLogEntry(BaseModel):
    target_id: Optional[str]
    changes: Optional[list[AuditLogChange]]
    user_id: Optional[int]
    id: int
    action_type: AuditLogEvent
    options: Optional[list[OptionalAuditEntry]]
    reason: Optional[str]


class AuditLogEvent(IntEnum):
    pass


class OptionalAuditEntry(BaseModel):
    pass


class AuditLogChange(BaseModel):
    pass


class AuditLogChangeKey(BaseModel):
    pass

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class AuditEntry:
    guild_id: int
    user_id: int
    action: str
    metadata: dict[str, Any] = field(default_factory=dict)


async def write_audit_log(entry: AuditEntry) -> None:
    print({"level": "info", "type": "audit", **entry.__dict__})

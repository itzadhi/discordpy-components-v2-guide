from dataclasses import dataclass
from services.audit_log import AuditEntry, write_audit_log


@dataclass(frozen=True)
class ModerationCase:
    case_id: str
    custom_id: str
    audit_channel_message: str


async def create_moderation_case(guild_id: int, moderator_id: int, target_id: int, reason: str) -> ModerationCase:
    case_id = f"case_{target_id}"
    await write_audit_log(AuditEntry(guild_id=guild_id, user_id=moderator_id, action="moderation.case.create", metadata={"case_id": case_id}))
    return ModerationCase(case_id=case_id, custom_id=f"moderation:review:{case_id}", audit_channel_message=f"Case {case_id}: {reason}")

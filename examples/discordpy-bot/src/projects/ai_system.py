from dataclasses import dataclass


@dataclass(frozen=True)
class AssistantRequest:
    custom_id: str
    safe_prompt: str
    privacy_note: str
    guild_id: int


def build_assistant_request(guild_id: int, user_id: int, prompt: str) -> AssistantRequest:
    return AssistantRequest(
        custom_id=f"ai:ask:{user_id}",
        safe_prompt=prompt[:1800],
        privacy_note="Do not store raw private messages unless the guild explicitly configured logging.",
        guild_id=guild_id,
    )

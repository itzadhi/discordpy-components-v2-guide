from dataclasses import dataclass


@dataclass(frozen=True)
class DashboardConfirmation:
    custom_id: str
    oauth_scopes: tuple[str, ...]
    state_key: str


def build_dashboard_confirmation(guild_id: int) -> DashboardConfirmation:
    return DashboardConfirmation(custom_id=f"dashboard:confirm:{guild_id}", oauth_scopes=("identify", "guilds"), state_key=f"dashboard:{guild_id}")

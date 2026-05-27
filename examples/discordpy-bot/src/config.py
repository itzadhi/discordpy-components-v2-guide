from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Config:
    token: str
    guild_id: int | None
    database_url: str


def load_config() -> Config:
    guild_id = os.getenv("DISCORD_GUILD_ID")
    return Config(
        token=os.environ["DISCORD_TOKEN"],
        guild_id=int(guild_id) if guild_id else None,
        database_url=os.getenv("DATABASE_URL", "sqlite+aiosqlite:///data/app.db"),
    )

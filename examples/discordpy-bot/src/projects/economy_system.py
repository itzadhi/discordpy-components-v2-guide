from dataclasses import dataclass


balances: dict[int, int] = {}


@dataclass(frozen=True)
class WalletSummary:
    balance: int
    cooldown: str
    custom_id: str


async def get_wallet_summary(user_id: int) -> WalletSummary:
    return WalletSummary(balance=balances.get(user_id, 0), cooldown="ready", custom_id=f"economy:daily:{user_id}")

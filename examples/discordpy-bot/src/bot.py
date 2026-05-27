import discord
from discord.ext import commands

from config import load_config
from cogs.tickets import TicketCog
from projects.verification_system import VerificationView


class ItzadhiBot(commands.Bot):
    async def setup_hook(self) -> None:
        await self.add_cog(TicketCog(self))
        self.add_view(VerificationView())
        await self.tree.sync()


def build_bot() -> ItzadhiBot:
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    bot = ItzadhiBot(command_prefix=commands.when_mentioned, intents=intents)
    return bot


if __name__ == "__main__":
    config = load_config()
    build_bot().run(config.token)

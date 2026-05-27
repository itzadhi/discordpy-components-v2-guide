import discord
from discord import app_commands
from discord.ext import commands

from projects.ticket_system import TicketOpenView


class TicketCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ticket_panel", description="Create a modern ticket panel")
    async def ticket_panel(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Use the button to open a guided ticket flow.",
            view=TicketOpenView(),
            ephemeral=True,
        )

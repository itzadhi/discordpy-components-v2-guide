import discord


class TicketModal(discord.ui.Modal, title="Open a ticket"):
    summary = discord.ui.TextInput(label="What do you need?", style=discord.TextStyle.paragraph, custom_id="ticket_summary")

    async def on_submit(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Ticket received: {str(self.summary)[:120]}", ephemeral=True)


class TicketOpenView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Open ticket", style=discord.ButtonStyle.primary, custom_id="ticket:open")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await interaction.response.send_modal(TicketModal(custom_id="ticket:submit"))

import discord
from discord.ext import commands
from discord import app_commands
from cogs.ui.modals import trivia_question


class Trivia(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        # todo :make a dict to keep track of the guild_id and the strand
        self.tests = {}

    @app_commands.command()
    async def start_round(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('use /join_game to join')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        Trivia(bot),
        guilds=[discord.Object(id=938541999961833574)]
    )

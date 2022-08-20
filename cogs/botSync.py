from discord import Interaction, app_commands, Object
from cogs._botSync import BotSyncUi
from discord.ext import commands
from cogs._help_command_setup import record
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BotSyncCog(bot), guilds=[Object(id=cacheGet("id"))])


class BotSyncCog(commands.Cog):
    def __init__(self: "BotSyncCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="edit or update your server settings")
    async def settings(self: "BotSyncCog", ctx: Interaction):
        await ctx.response.send_message(BotSyncUi(self.bot.httpx))

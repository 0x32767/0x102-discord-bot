from discord import Interaction, app_commands, Object, Embed
from cogs._botSync import BotSyncUi
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(botSyncCog(bot), guilds=[Object(id=cacheGet("id"))])


class botSyncCog(commands.Cog):
    def __init__(self: "botSyncCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="edit or update your server settings")
    async def settings(self: "botSyncCog", ctx: Interaction):
        await ctx.send_interaction(BotSyncUi())

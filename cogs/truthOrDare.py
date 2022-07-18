import cogs._helpCommandSetup
from cogs._truthOrDare import TruthOrDareUi
from discord.ext import commands
from cache import cacheGet
from discord import Interaction, app_commands, Object


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TruthOrDareCog(bot), guilds=[Object(id=cacheGet("id"))])


class TruthOrDareCog(commands.Cog):
    def __init__(self: "TruthOrDareCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="truthordare", description="Truth or Dare")
    async def truth_or_dare(self: "TruthOrDareCog", ctx: Interaction) -> None:
        await ctx.response.send_message(view=TruthOrDareUi())

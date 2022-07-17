from cogs._helpCommandSetup import recorded_commands
import cogs._helpCommandSetup
from discord.ext import commands
from cache import cacheGet
from discord import (
    Embed,
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        HelpCommand(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class HelpCommand(commands.Cog):
    def __init__(self: "HelpCommand", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command()
    async def help(self: "HelpCommand", ctx: Interaction) -> None:
        await ctx.response.send_message(
            embed=Embed(
                title="Help",
                description="This is the help command.",
                url="https://github.com/0x32767/0x102-discord-bot/blob/master/docs/help-cmd.md"
            )
        )

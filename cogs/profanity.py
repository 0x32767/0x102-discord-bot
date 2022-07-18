from discord import Interaction, app_commands, Object, Embed
from cogs._profanity import check_raw
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ProfanityReport(bot), guilds=[Object(id=cacheGet("ID"))])


class ProfanityReport(commands.Cog):
    def __init__(self: "ProfanityReport", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record("/report <message>")
    @app_commands.command(name="report", description="Report a profanity message.")
    @app_commands.describe(user="Who the message is from.")
    @app_commands.describe(message="The message to report.")
    async def report(
        self: "ProfanityReport", ctx: commands.Context, user: Interaction, message: str
    ) -> None:
        if check_raw(message):
            await ctx.send(
                Embed(
                    title="Profanity Report",
                    description=f"{user.mention} has reported a profanity message.",
                    color=0xFF0000,
                )
            )
        else:
            await ctx.send(
                Embed(
                    title="Profanity Report",
                    description=f"{user.mention} has reported a non-profanity message.",
                    color=0x00FF00,
                )
            )

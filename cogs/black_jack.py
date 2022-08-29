from discord import Interaction, app_commands, Object, Message, Embed
from cogs._help_command_setup import record
from discord.ext import commands
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BlackJackCog(bot), guilds=[Object(id=cacheGet("id"))])


class BlackJackCog(commands.Cog):
    def __init__(self: "BlackJackCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="lets you play blackjack")
    async def playbj(self: "BlackJackCog", ctx: Interaction) -> None:
        ...

    @record()
    @app_commands.command(description="")
    async def infobj(self: "BlackJackCog", ctx: Interaction) -> Message:
        return await ctx.response.send_message(
            embed=Embed("How to play black jack", description="", url="")
        )

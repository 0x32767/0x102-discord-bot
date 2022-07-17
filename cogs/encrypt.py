from cogs._encryption import EncryptionView
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet
from discord import (
    Object,
    app_commands,
    Interaction,
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        EncryptCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class EncryptCog(commands.Cog):
    def __init__(self: "EncryptCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command()
    async def encrypt(self: "EncryptCog", ctx: Interaction, msg: str) -> None:
        await ctx.response.send_message(
            view=EncryptionView(msg),
            ephemeral=True
        )

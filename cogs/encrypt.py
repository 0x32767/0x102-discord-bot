from cache import cacheGet
from discord.ext import commands
from cogs._encryption import EncryptionView
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

    @app_commands.command()
    async def encrypt(self: "EncryptCog", ctx: Interaction, msg: str) -> None:
        await ctx.response.send_message(
            view=EncryptionView(msg),
            ephemeral=True
        )

from typing import Generator
from discord import Interaction, app_commands, Object, Message, User
from usefull.textDecorations import progressBar
from hashlib import sha256, sha1, md5
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DumbCommandsCog(bot), guilds=[Object(id=cacheGet("id"))])


class DumbCommandsCog(commands.Cog):
    def __init__(self: "DumbCommandsCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="shows the durp-score of someone")
    @app_commands.describe(user="who's durp-score you want to see")
    async def durpscore(self: "DumbCommandsCog", ctx: commands.Context, user: Interaction) -> None | Message:
        if user:
            await ctx.send(f"{user.mention} has a durp-score of `{user.id % 100}`")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="get a users discord token")
    @app_commands.describe(user="who's token you want to see")
    async def hack(self: "DumbCommandsCog", ctx: Interaction, user: User) -> None:
        dec: Generator[str] = progressBar()
        msg: Message = await ctx.response.send_message()

    async def _dummyHash(self: "DumbCommandsCog", user: User) -> str:
        return f'{sha256(user.id.to_bytes(8, "big")).hexdigest()}.{sha1(user.id.to_bytes(8, "big")).hexdigest()}.{md5(user.id.to_bytes(8, "big")).hexdigest()}'

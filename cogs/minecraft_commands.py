import json
import random
from cache import cacheGet
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object,
    Member
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        MinecrtaftCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class MinecrtaftCog(commands.Cog):
    def __init__(self: 'MinecrtaftCog', bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command()
    async def kill(self: 'MinecrtaftCog', ctx: Interaction, player: Member = None) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :param player: The player that is killed
        :return:
        """
        with open("death_messages.json", "r") as f:
            data: dict[list[str]] = json.load(f)

        if player is None:
            await ctx.response.send_message(random.choice(data["self"]).replace("{player}", ctx.user.mention))

        else:
            await ctx.response.send_message(
                random.choice(
                    data["other"]
                ).replace(
                    "{player}", player.mention
                ).replace(
                    "{killer}", ctx.user.mention
                )
            )

        del data

    def __cog_docs__(self) -> str:
        return "This is the minecrtaft cog."

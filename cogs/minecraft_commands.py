import discord
import json
import random
from discord.ext import commands, menus
from discord import (
    Interaction,
    app_commands,
    Object,
    Member
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        MinecrtaftCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class MinecrtaftCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def kill(self, ctx: Interaction, player: Member=None) -> None:
        """
        :param ctx: The ctx param is passes by the discord.py libruary
        :param player: The player that is killed
        :return:
        """
        with open("C:\\Users\\Han\\programing\\Boo2 discord bot\\death_messages.json", "r") as f:
            data = json.load(f)

        if player is None:
            await ctx.response.send_message(random.choice(data["self"]).replace("{player}", ctx.user.mention))

        else:
            await ctx.response.send_message(random.choice(data["other"]).replace("{player}", player.mention).replace("{killer}", ctx.user.mention))

        del data

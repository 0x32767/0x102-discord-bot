import discord
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
        HelpComand(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class HelpComand(commands.Cog):
    def __init__(self: "HelpComand", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @app_commands.command(name="help", description="help command")
    async def help(self: "HelpComand", ctx: Interaction) -> None:
        embed: Embed = discord.Embed(
            title="Help",
            description="Use `/help` and then the name of the command to learn more about it."
        )

        for cog in self.bot.cogs:
            embed.add_field(
                name=f"{cog}",
                value=f"{self.bot.cogs[cog].__cog_docs__()}",
                inline=False
            )

        await ctx.response.send_message(embed=embed)

    def pass_(self) -> None:...

    def __cog_docs__(self) -> str:
        self.pass_()
        return """
        This cog is used to help you with the bot.
        The commands are:
         -help
        """

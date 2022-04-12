import wikipedia as wiki
from ._comand_chache import register_commands
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        WikiCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class WikiCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        register_commands(self)
        self.bot = bot

    @app_commands.command()
    async def wiki(self, ctx: Interaction, *, query: str) -> None:
        """
        :param ctx: The `ctx` peramiter is passed by default by the discord.py lib when executed
        :param query: The `query` peram is passes by the command user and is used to search wikipedia
        """
        try:
            summary = wiki.summary(query, sentences=3)
            await ctx.response.send_message(
                f"""
__**{query}**__

```
{summary}
```
            """
            )
        except Exception as e:
            await ctx.response.send_message(f"error: {e}")

    def __cog_docs__(self) -> str:
        return """
        This cog is used to search wikipedia.
        You can use the commands:
            -wiki
        """

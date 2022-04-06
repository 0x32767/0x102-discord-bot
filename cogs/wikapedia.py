import wikipedia as wiki
import discord
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
        self.bot = bot

    @app_commands.command()
    async def wiki(self, ctx: Interaction, *, query: str) -> None:
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

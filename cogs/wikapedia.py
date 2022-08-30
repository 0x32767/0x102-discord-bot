"""
Copyright (C) 23/07/2022 - Han P.B Manseck.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from discord import Interaction, app_commands, Object
from cogs._help_command_setup import record
from discord.ext import commands
from cache import cacheGet
import wikipedia as wiki


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WikiCog(bot), guilds=[Object(id=938541999961833574)])


class WikiCog(commands.Cog):
    def __init__(self: "WikiCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="Searches Wikipedia for a given term.")
    @app_commands.describe(query="The query you want to search for.")
    async def wiki(self: "WikiCog", ctx: Interaction, *, query: str) -> None:
        """
        :param ctx: The `ctx` peramiter is passed by default by the discord.py lib when executed
        :param query: The `query` peram is passes by the command user and is used to search wikipedia
        """
        try:
            summary: str = wiki.summary(query, sentences=3)
            await ctx.response.send_message(f"""__**{query}**__\n```\n{summary}\n```""")
        except Exception as e:
            await ctx.response.send_message(f"error: {e}")

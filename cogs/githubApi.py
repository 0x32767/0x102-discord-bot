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


from httpx import AsyncClient
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet
from discord import Interaction, app_commands, Object, Embed


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(githubApiCog(bot), guilds=[Object(id=cacheGet("id"))])


class githubApiCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.cs: AsyncClient = AsyncClient()
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about a github user.")
    @app_commands.describe(username="Username of the user.")
    async def getuser(self: "githubApiCog", ctx: Interaction, *, username: str) -> None:
        """
        :param ctx: The `ctx` is passed by default when the command is executed
        :param username: The `username` is the name of the user
        :return:
        """
        req = await self.cs.get(f"https://api.github.com/users/{username}")
        data = await req.json()

        em: Embed = Embed(title=f"{username}", description=f"{data['bio']}")

        em.set_thumbnail(url=f"{data['avatar_url']}")

        for key, value in zip(
            [
                "name",
                "blog",
                "location",
                "email",
                "public repos",
                "followers",
                "following",
            ],
            [
                data["name"],
                data["blog"],
                data["location"],
                data["email"],
                data["public_repos"],
                data["followers"],
                data["following"],
            ],
        ):
            em.add_field(name=key, value=value or "None")

        await ctx.response.send_message(embed=em)

        del data, req

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about a users github repos.")
    @app_commands.describe(username="Username of the user who`s repos you want to get.")
    async def getrepos(self: "githubApiCog", ctx: Interaction, *, username: str) -> None:
        """
        :param ctx: The `ctx` is passed by default when the command is executed
        :param username: The `username` is the name of the user
        :return:
        """
        req = await self.cs.get(f"https://api.github.com/users/{username}/repos")
        data = await req.json()

        em: Embed = Embed(title=f"{username}`s repos", description=f"{len(data)} repos")

        for repo in data:
            em.add_field(name=repo["name"], value=repo["description"] or "None")

        await ctx.response.send_message(embed=em)

        del data, req

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about the latest bot update.")
    async def getlatestupdate(self: "githubApiCog", ctx: Interaction) -> None:
        req = await self.cs.get("https://api.github.com/repos/0x32767/0x102-discord-bot/commits/master/")
        data = await req.json()

        em: Embed = Embed(title=f"{self.bot.user.name}'s latest update", description="get the bot's latest updates")
        em.add_field(name="Latest update date", value=data["commit"]["author"]["date"])
        em.add_field(name="Latest update message", value=data["commit"]["message"])
        em.add_field(name="Latest update url", value=data["html_url"])
        em.add_field(name="Latest update author", value=data["commit"]["author"]["name"])
        em.add_field(name="Lines of code added", value=data["stats"]["additions"])
        em.add_field(name="Lines of code deleted", value=data["stats"]["deletions"])
        em.add_field(name="Lines of code changed", value=data["stats"]["total"])
        em.add_field(name="Files changed", value=len(data["files"]))
        em.set_image(url=data["committer"]["avatar_url"])

        await ctx.response.send_message(embed=em)

        del req, data

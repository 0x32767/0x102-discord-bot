from discord.ext import commands
from cache import cacheGet
import requests
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        githubApiCog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class githubApiCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(username="Username of the user.")
    async def getuser(self: "githubApiCog", ctx: Interaction, *, username: str) -> None:
        """
        :param ctx: The `ctx` is passed by default when the command is executed
        :param username: The `username` is the name of the user
        :return:
        """
        data: dict = requests.get(
            f"https://api.github.com/users/{username}"
        ).json()

        em: Embed = Embed(
            title=f"{username}",
            description=f"{data['bio']}"
        )

        em.set_thumbnail(url=f"{data['avatar_url']}")

        for key, value in zip(
                ["name", "blog", "location", "email", "public repos", "followers", "following"],
                [
                    data["name"], data["blog"], data["location"], data["email"],
                    data["public_repos"], data["followers"], data["following"]
                ]
        ):
            em.add_field(name=key, value=value or "None")

        await ctx.response.send_message(embed=em)

        del data

    @app_commands.command()
    @app_commands.describe(username="Username of the user who`s repos you want to get.")
    async def getrepos(self: "githubApiCog", ctx: Interaction, *, username: str) -> None:
        """
        :param ctx: The `ctx` is passed by default when the command is executed
        :param username: The `username` is the name of the user
        :return:
        """
        data: dict = requests.get(
            f"https://api.github.com/users/{username}/repos"
        ).json()

        em: Embed = Embed(
            title=f"{username}`s repos",
            description=f"{len(data)} repos"
        )

        for repo in data:
            em.add_field(name=repo["name"], value=repo["description"] or "None")

        await ctx.response.send_message(embed=em)

        del data

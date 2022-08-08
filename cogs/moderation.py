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


from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet
import aiosqlite
from discord import Interaction, app_commands, Object, Embed, Member


class Moderation(commands.Cog):
    def __init__(self: "Moderation", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Kicks a member from the server.")
    @app_commands.describe(user="The user you want to kick.")
    @app_commands.describe(reason="Why you want to kick the user.")
    async def kick(
        self: "Moderation",
        ctx: Interaction,
        user: Member,
        *,
        reason: str = "You  have been naughty",
    ) -> None:
        """
        :param ctx:
        :param user:
        :param reason:
        :return:
        """
        try:
            await user.kick(reason=reason)
            await ctx.response.send_message(f'successfully kicked {user.name} for "{reason}"')

        except Exception as e:
            await ctx.response.send_message(f"error: {e}")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Bans a member from the server.")
    @app_commands.describe(user="The user you want to ban.")
    @app_commands.describe(reason="Why you want to ban the user.")
    async def ban(
        self: "Moderation",
        ctx: Interaction,
        user: Member,
        *,
        reason: str = "you have been naughty",
    ) -> None:
        try:
            await user.ban(reason=reason)
            await ctx.response.send_message(f'successfully kicked {user.name} for "{reason}"')

        except Exception as e:
            await ctx.response.send_message(f"error: {e}")

    @cogs._helpCommandSetup.record()
    @app_commands.command(name="stats", description="you can see server statistics")
    async def stats(self: "Moderation", ctx: Interaction) -> None:
        async with ctx.channel.typing():
            embed: Embed = Embed(
                title=f"{ctx.guild.name}'s stats",
                description="gives the stats of the server",
            )
            for key, stat in zip(
                ["name", "owner", "members", "region"],
                [
                    str(ctx.guild.name),
                    str(ctx.guild.owner.name),
                    str(ctx.guild.member_count),
                    str(ctx.guild.region),
                ],
            ):
                embed.add_field(name=key, value=stat)

        await ctx.response.send("ok", embed=embed)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="whitelist a user and bots")
    @app_commands.describe(member="The user you want to whitelist.")
    @commands.is_owner()
    async def whitelist(self: "Moderation", ctx: Interaction, member: Member) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect("discordbotdb.db") as db:
                async with db.cursor() as curr:
                    await curr.execute(
                        f"update whitelist set whitelisted = True where guild_id = {ctx.guild.id} and user_id = {member.id}"
                    )

                await db.commit()

            await ctx.response.send_message(f"{ctx.user.mention} has now been whitelisted!!!")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="unwhitelist a user and bots")
    @app_commands.describe(member="The user you want to unwhitelist.")
    @commands.is_owner()
    async def unwhitelist(self: "Moderation", ctx: Interaction, member: Member) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect("discordbotdb.db") as db:
                async with db.cursor() as curr:
                    await curr.execute(
                        f"update whitelist set whitelisted = False where guild_id = {ctx.guild.id} and user_id = {member.id}"
                    )

            await db.commit()

            await ctx.response.send_message(f"{ctx.user.mention} has now been unwhitelisted!!!")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="check if a user is whitelisted")
    @app_commands.describe(member="The user you want to check.")
    async def whitelisted(self: "Moderation", ctx: Interaction, member: Member) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect("discordbotdb.db") as db:
                async with db.cursor() as curr:
                    await curr.execute(
                        f"select whitelisted from whitelist where guild_id = {ctx.guild.id} and user_id = {member.id}"
                    )

                    whitelisted: tuple = await curr.fetchone()

            await db.commit()

            if whitelisted[0] == 1:
                await ctx.response.send_message(f"{member.mention} is whitelisted")
            else:
                await ctx.response.send_message(f"{member.mention} is not whitelisted")

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Check if a user is banned and then kicks them.")
    async def antiraid(self: "Moderation", ctx: Interaction) -> None:
        async with ctx.channel.typing():
            async with aiosqlite.connect("discordbotdb.db") as db:
                async with db.cursor() as curr:
                    for member in ctx.guild.members:
                        await curr.execute(
                            f"select whitelisted from whitelist where guild_id = {ctx.guild.id} and user_id = {member.id}"
                        )

                        whitelisted: tuple = await curr.fetchone()
                        if whitelisted == 1:
                            continue

                        else:
                            await member.kick(reason=f"You are not whitelisted in the `{ctx.guild.name}` server")

            await ctx.response.send_message("ok, done")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Moderation(bot), guilds=[Object(id=cacheGet("id"))])

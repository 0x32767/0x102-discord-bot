from discord import Interaction, app_commands, Object, User
from cogs._help_command_setup import record
from discord.ext import commands
from aiosqlite import connect
from cache import cacheGet


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReputationCog(bot), guilds=[Object(id=cacheGet("id"))])


class ReputationCog(commands.Cog):
    def __init__(self: "ReputationCog", bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @record()
    @app_commands.command(description="see how much reputation you have")
    async def reputation(self: "ReputationCog", ctx: Interaction):
        async with connect("discordbotdb.db") as db:
            async with db.execute("SELECT reputation FROM users WHERE id = ?", (ctx.user.id,)) as cursor:
                res = await cursor.fetchone()

                if res is None:
                    await ctx.response.send_message("you have no reputation")
                    return

                await ctx.response.send_message(f"you have {res[0]} reputation")

    @record()
    @app_commands.command(description="give someone reputation")
    @app_commands.describe(user="Who you want to give reputation to")
    @app_commands.describe(amount="how much reputation you want to give")
    @commands.has_permissions(administrator=True)
    async def give(self: "ReputationCog", ctx: Interaction, user: User, amount: int):
        async with connect("discordbotdb.db") as db:
            async with db.execute("SELECT reputation FROM users WHERE id = ?", (user.id,)) as cursor:
                res = await cursor.fetchone()

                if res is None:
                    await ctx.response.send_message("that user has no reputation")
                    return

                await db.execute("UPDATE users SET reputation = ? WHERE id = ?", (res[0] + amount, user.id))
                await ctx.response.send_message(
                    f"you have given {user.name} {amount} reputation, and they now have {res[0] + amount}"
                )

from discord import Interaction, Embed
from aiosqlite import connect


async def is_admin(ctx: Interaction) -> Embed | None:
    async with connect("data.db") as db:
        async with db.cursor() as cur:
            await cur.execute("SELECT admin FROM users WHERE userId = ? and guildId = ?", (ctx.user.id, ctx.guild.id))

            if await cur.fetchone()[0] == 1:
                return await ctx.response.send_message(
                    embed=Embed(
                        title=f"{ctx.command.name} requires admin",
                        description=f"{ctx.user.mention} you do not have admin permissions to use this command",
                        color=16711680,
                    )
                )

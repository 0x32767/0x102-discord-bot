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


from discord import Interaction, Embed
from aiosqlite import connect
from typing import Union


# This will check if the command invoker has qualified permitions
async def is_moderator(ctx: Interaction) -> bool:
    """Creates a database connection and returns a boolean corisponding to if the user is a moderator or not respectively.

    Args:
        ctx (Interaction): This is passes so that we can get the id of the user, server id and the response property,
        this is so that we can respond to a user if they don't have the required privilages

    Returns:
        Union[True, False]: This is so that we can use the function inside of an if-statement and the command can return prematurly.
    """
    async with connect("data.db") as db:
        async with db.cursor() as cur:
            await cur.execute("SELECT moderator FROM users WHERE userId = ? and guildId = ?", (ctx.user.id, ctx.guild.id))  # type: ignore

            if (await cur.fetchone())[0] in [True, 1]:  # type: ignore
                await ctx.response.send_message(
                    embed=Embed(
                        title=f"{ctx.command.name} requires moderator",  # type: ignore
                        description=f"{ctx.user.mention} you do not have moderator permissions to use this command",
                        color=16711680,
                    )
                )

                return False

    return True

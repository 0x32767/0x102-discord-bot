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

import cogs._luaErrors as err
from discord import Interaction, Embed
from lupa import LuaRuntime
import inspect


async def create_embed(embed) -> Embed or tuple[str, str]:
    if not embed:
        return

    # the discord api only lets embeds have up tp 25 fields.
    if len(embed["fields"]) >= 26:
        return err.MaxEmbedFieldsExceeded(
            {
                "message": f"the maximum amount of embeds has been reached got {len(embed['fields'])} >= 26",
                "ErrorUrl": "https://github.com/0x32767/0x102-discord-bot/blob/master/cogs/_luaErrors.py#L1",
            }
        )

    try:
        em: Embed = Embed(
            title=embed["title"], description=embed["description"], color=embed["color"]
        )

    except KeyError:
        return err.EmbedInitializeError(
            {
                "message": "the embed was not initialized correctly",
                "ErrorUrl": "https://github.com/0x32767/0x102-discord-bot/blob/master/cogs/_luaErrors.py#L44",
            }
        )

    for field in embed["fields"]:
        try:
            em.add_field(
                name=field["name"], value=field["value"], inline=field["inline"]
            )

        except KeyError:
            return err.FieldInitializeError(
                {
                    "message": "the embed was not initialized correctly, the following keys were not found: footer",
                    "ErrorUrl": "https://github.com/0x32767/0x102-discord-bot/blob/master/cogs/_luaErrors.py#L96",
                }
            )

    try:
        em.set_footer(text=embed["footer"])

    except KeyError:
        return err.FieldInitializeError(
            {
                "message": "the embed was not initialized correctly, the following keys were not found: footer",
                "ErrorUrl": "https://github.com/0x32767/0x102-discord-bot/blob/master/cogs/_luaErrors.py#L142",
            }
        )

    return em


# this function will validate out embed and check for errors.
async def check_embed(
    embed: Embed or any(inspect.getmembers(err)), ctx: Interaction
) -> bool:
    # check if the embed inherits from the Embed class.
    if not issubclass(embed.__class__.__base__, Exception):
        return await ctx.response.send_message(embed=embed)

    # I have added an embed attribute to the error classs so we can just send the embed.
    for cls in inspect.getmembers(err):
        if isinstance(embed, cls):
            return await ctx.response.send_message(embed=cls.embed)


async def run(code: str, ctx: Interaction) -> None:
    if not code:
        return

    lua: LuaRuntime = LuaRuntime()

    # This file contains only a function that creates a lua tabel out of the interaction
    # object. So we pass it the interaction form discord.py and get a lua interaction
    # table back. This is neseccery because it removes unewanted methords that could be
    # detremental to the server or bot.
    with open(".\\discord-lua-wrapper\\Interaction.lua", "r") as f:
        # iMaker is the function that creates the lua table. (it is abreviated to interactionMaker)
        iMaker = lua.eval(f.read())

    func: callable = lua.eval(code)
    match (res := func(iMaker(ctx)))["type"]:
        case "message":
            await ctx.response.send_message(res["object"]["content"])

        case "embed":
            await ctx.response.send_message(await create_embed(res["object"]))

    del lua, func
    return

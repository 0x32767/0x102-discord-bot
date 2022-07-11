from cogs._luaErrors import *
from discord import Interaction, Embed
from lupa import LuaRuntime


async def create_embed(embed) -> Embed or tuple[str, str]:
    if not embed:
        return

    # the discord api only lets embeds have up tp 25 fields.
    if len(embed["fields"]) >= 26:
        raise MaxEmbedFieldsExceeded({
            "message": f"the maximum amount of embeds has been reached got {len(embed['fields'])} >= 26",
            "ErrorUrl": ""
        })

    try:
        em: Embed = Embed(
            title=embed["title"],
            description=embed["description"],
            color=embed["color"]
        )

    except KeyError:
        return ("E", "Missing title, description or color")

    for field in embed["fields"]:
        try:
            em.add_field(
                name=field["name"],
                value=field["value"],
                inline=field["inline"]
            )

        except KeyError:
            return ("E", "Missing name, value or inline")

    try:
        em.set_footer(text=embed["footer"]["text"])

    except KeyError:
        return ("E", "Missing footer text or footer")

    return ("S", em)


async def run(code: str, ctx: Interaction) -> None:
    if not code:
        return

    lua: LuaRuntime = LuaRuntime()

    # This file contains only a function that creates a lua tabel out of the interaction
    # object. So we pass it the interaction form discord.py and get a lua interaction
    # table back. This is neseccery because it removes unewanted methords that could be
    # detremental to the server.
    with open(".\\discord-lua-wrapper\\Interaction.lua", "r") as f:
        # iMaker is the function that creates the lua table.
        iMaker = lua.eval(f.read())

    func: callable = lua.eval(code)
    match (res := func(iMaker(ctx)))["type"]:
        case "message":
            await ctx.response.send_message(res["content"])

        case "embed":
            await ctx.response.send_message(await create_embed(res["embed"]))


    del lua, func, table
    return

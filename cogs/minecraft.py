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


from json import load as jsonLoads
from aiohttp import ClientSession
from discord.ext import commands
import cogs._helpCommandSetup
from cache import cacheGet
from discord import Interaction, app_commands, Object, Embed


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MinecraftCog(bot), guilds=[Object(id=cacheGet("id"))])


class MinecraftCog(commands.Cog):
    def __init__(self: "MinecraftCog", bot: commands.Bot) -> None:
        self.cs: ClientSession = ClientSession()
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about a minecraft block.")
    @app_commands.describe(id="The id of the block you want to learn about.")
    async def mcidlookup(self: "MinecraftCog", ctx: Interaction, id: int) -> None:
        """
        :param ctx: `ctx` param is passed by the discord.pt library when executed
        :param id:  `id` param is of class integer that should correspond to a minecraft block id
        :return:
        """
        with open("assets/mcblocks.json") as f:
            data: list[dict] = jsonLoads(f)
            del f

        for block in data:
            if block["id"] != id:
                continue

            em: Embed = Embed(
                title=f"learn more about `{block['displayName']}`",
                description="use `/idlookupblock` and then the id of the block to get info about the block",
            )

            em.add_field(
                name="mine able",
                value="yes" if block["diggable"] else "no",
                inline=True,
            )
            em.add_field(
                name="tool",
                value=block["material"] if "material" in block.keys() else "none",
                inline=True,
            )
            em.add_field(name="stacks up to", value=f"{block['stackSize']}")
            em.add_field(name="transparent", value="yes" if block["transparent"] else "no")
            em.add_field(name="emits light", value=f"emits `{block['emitLight']}` light")
            await ctx.response.send_message(embed=em)
            break

        del data

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about a minecraft block.")
    @app_commands.describe(name="Give information about a minecraft block.")
    async def mcnamelookup(self: "MinecraftCog", ctx: Interaction, *, name: str) -> None:
        """
        :param ctx: The `ctx` is passed by default when the command is executed
        :param name:  The name param is class string and is the display name for the minecraft item/block
        :return:
        """
        with open("assets/mcblocks.json") as f:
            data: list[dict] = jsonLoads(f)
            del f

        for block in data:
            if block["name"] != name and block["displayName"] != name:
                continue

            em: Embed = Embed(
                title=f'learn more about `{block["displayName"]}`',
                description="use `/namelookupblock` and then the id of the block to learn about it",
            )

            em.add_field(name="mine able", value="yes" if block["diggable"] else "no")
            em.add_field(name="tool", value=block["material"])
            em.add_field(name="stacks up to", value=f"{block['stackSize']}")
            em.add_field(name="transparent", value="yes" if block["transparent"] else "no")
            em.add_field(name="emits light", value=f"emits `{block['emitLight']}` light")
            del data

            return await ctx.response.send_message(embed=em)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about a minecraft crafting recipe.")
    @app_commands.describe(item="The name of the item e.g. `campfire`")
    async def mccraft(self: "MinecraftCog", ctx: Interaction, item: str) -> None:
        """
        :param ctx: The `ctx` argument is passed by default when the command is executed
        :param item: The `item` argument is the name of the item e.g "cooked_mutton"
        :return:
        """
        with open("assets\mcrecipes.json") as f:
            data: list[dict] = jsonLoads(f)
            del f

        em: Embed = Embed(
            title=f"How to craft {item}",
            description="use `/craft` to learn the ways to make something",
        )
        i: int = 0

        for key, recipe in data.items():
            if recipe["output"][0]["name"] == item:
                em.add_field(
                    name=f"Way {i + 1} to craft {item}",
                    value="".join([f"{f['name']}: {f['count']}\n" for f in recipe["ingredients"]]),
                )
                i += 1

        await ctx.response.send_message(embed=em)
        del data, req

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Gets some info about a minecraft entity drops.")
    @app_commands.describe(entity="The name of the item e.g. `campfire`")
    async def mcloot(self, ctx: Interaction, entity: str) -> None:
        with open("assets\mcentityLoot.json") as f:
            data: list[dict] = jsonLoads(f)
            del f

        for e in data:
            if e["entity"] == entity:
                em: Embed = Embed(
                    title=f"{entity} loot",
                    description="use `/loot` to learn the loot that can be found from this entity",
                )

                for loot in e["drops"]:
                    em.add_field(name=loot["item"], value=str(loot["dropChance"]))

                return await ctx.response.send_message(embed=em)

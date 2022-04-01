import requests
import discord
from discord.ext import commands
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MinecraftCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class MinecraftCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    async def idlookupblock(self, ctx: Interaction, id: int) -> None:
        data = requests.get('https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.18.11/blocks.json').json()
        
        for block in data:
            if block['id'] == id:
                em = Embed(title=f'learn more about `{block["displayName"]}`', description='use `/idlookupblock` and then the id of the block to get info about the block')
                em.add_field(name='mineable', value='yes' if block['diggable'] else 'no')
                em.add_field(name='tool', value=block['material'])
                em.add_field(name='stacks up to', value=f"{block['stackSize']}")
                em.add_field(name='transparent', value= 'yes' if block['transparent'] else 'no')
                em.add_field(name='emmits light', value=f"emits `{block['emitLight']}` light")
                await ctx.response.send_message(embed=em)
                break

            else:
                continue

        del data

    @app_commands.command()
    async def namelookupblock(self, ctx: Interaction, name: str) -> None:
        data = requests.get('https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.18.11/blocks.json').json()

        for block in data:
            if block['name'] == name or block['displayName'] == name:
                em = Embed(title=f'learn more about `{block["displayName"]}`', description='use `/namelookupblock` and then the id of the block to learn about it')
                em.add_field(name='mineable', value='yes' if block['diggable'] else 'no')
                em.add_field(name='tool', value=block['material'])
                em.add_field(name='stacks up to', value=f"{block['stackSize']}")
                em.add_field(name='transparent', value= 'yes' if block['transparent'] else 'no')
                em.add_field(name='emmits light', value=f"emits `{block['emitLight']}` light")
                await ctx.response.send_message(embed=em)
                break

            else:
                continue

        del data

    @app_commands.command()
    async def craft(self, ctx: Interaction, item: str) -> None:
        data = requests.get('https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.18.11/recipes.json').json()
        em = Embed(title=f"How to caraft {item}", description='use `/craft` to learn the ways to make something')
        i = 0

        for key, recipie in data.items():
            if recipie['output'][0]['name'] == item:
                em.add_field(
                    name=f"Way {i+1} to caraft {item}",
                    value=''.join(
                        [f"{f['name']}: {f['count']}\n" for f in recipie['ingredients']]
                    )
                )
                i += 1

        await ctx.response.send_message(embed=em)

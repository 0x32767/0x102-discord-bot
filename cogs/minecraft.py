import requests
from discord.ext import commands
from ._comand_chache import register_commands
from discord import (
    Interaction,
    app_commands,
    Object,
    Embed
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        MinecraftCog(bot),
        guilds=[Object(id=938541999961833574)]
    )


class MinecraftCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        register_commands(self)
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(id="The id of the block you want to learn about.")
    async def idlookupblock(self, ctx: Interaction, id: int) -> None:
        """
        :param ctx: `ctx` param is passed by the discord.pt library when executed
        :param id:  `id` param is of class integer that should correspond to a minecraft block id
        :return:
        """
        data = requests.get(
            'https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.18.11/blocks.json'
        ).json()

        for block in data:
            if block['id'] != id:
                continue

            em = Embed(
                title=f'learn more about `{block["displayName"]}`',
                description='use `/idlookupblock` and then the id of the block to get info about the block'
            )

            em.add_field(name='mine able', value='yes' if block['diggable'] else 'no')
            em.add_field(name='tool', value=block['material'])
            em.add_field(name='stacks up to', value=f"{block['stackSize']}")
            em.add_field(name='transparent', value='yes' if block['transparent'] else 'no')
            em.add_field(name='emits light', value=f"emits `{block['emitLight']}` light")
            await ctx.response.send_message(embed=em)
            break

        del data

    @app_commands.command()
    @app_commands.describe(name="Give information about a minecraft block.")
    async def namelookupblock(self, ctx: Interaction, *, name: str) -> None:
        """
        :param ctx: The `ctx` is passed by default when the command is executed
        :param name:  The name param is class string and is the display name for the minecraft item/block
        :return:
        """
        data = requests.get(
            'https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.18.11/blocks.json'
        ).json()

        for block in data:
            if block['name'] != name and block['displayName'] != name:
                continue

            em = Embed(
                title=f'learn more about `{block["displayName"]}`',
                description='use `/namelookupblock` and then the id of the block to learn about it'
            )

            em.add_field(name='mine able', value='yes' if block['diggable'] else 'no')
            em.add_field(name='tool', value=block['material'])
            em.add_field(name='stacks up to', value=f"{block['stackSize']}")
            em.add_field(name='transparent', value='yes' if block['transparent'] else 'no')
            em.add_field(name='emits light', value=f"emits `{block['emitLight']}` light")
            await ctx.response.send_message(embed=em)
            break

        del data

    @app_commands.command()
    @app_commands.describe(item="The name of the item e.g. `campfire`")
    async def craft(self, ctx: Interaction, item: str) -> None:
        """
        :param ctx: The `ctx` argument is passed by default when the command is executed
        :param item: The `item` argument is the name of the item e.g 'cooked_mutton'
        :return:
        """
        data = requests.get(
            'https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/bedrock/1.18.11/recipes.json'
        ).json()

        em = Embed(title=f"How to craft {item}", description='use `/craft` to learn the ways to make something')
        i = 0

        for key, recipe in data.items():
            if recipe['output'][0]['name'] == item:
                em.add_field(
                    name=f"Way {i + 1} to craft {item}",
                    value=''.join(
                        [f"{f['name']}: {f['count']}\n" for f in recipe['ingredients']]
                    )
                )
                i += 1

        await ctx.response.send_message(embed=em)

    @app_commands.command()
    @app_commands.describe(enchantment="The name of the enchantment e.g. `Protection`")
    async def findenchant(self, ctx: Interaction, enchantment: str) -> None:
        data = requests.get(
            'https://raw.githubusercontent.com/PrismarineJS/minecraft-data/master/data/pc/1.8/enchantments.json'
        ).json()

        for enchant in data:
            if enchant['displayName'] == enchantment or enchant['name'] == enchantment:
                em = Embed(title=f"{enchant['name']}", description='use `/findenchant` to learn more about the enchantment')
                em.add_field(name='max level', value=f"{enchant['maxLevel']}")
                em.add_field(name='does not go with', value='\n'.join(list(enchant['exclude'])))

                em.add_field(name='catagory', value=f"{enchant['category']}")
                em.add_field(name='tradeable', value=f"{enchant['tradeable']}")
                em.add_field(name='discoverable', value=f"{enchant['discoverable']}")

                await ctx.response.send_message(embed=em)
                break

            else:
                continue

        del data

    def __cog_docs__(self) -> str:
        return """
        Ytou can view minecraft related information using the following commands:
            - idlookupblock
            - namelookupblock
            - craft
            - findenchant
        """

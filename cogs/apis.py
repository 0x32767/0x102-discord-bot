from requests import get as get_request
from json import loads as js_loads
from cogs._comand_chache import register_commands
from discord.ext import commands
from cache import cacheGet
from discord import (
    Embed,
    Interaction,
    app_commands,
    Object,
    ui
)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        APICog(bot),
        guilds=[Object(id=cacheGet("id"))]
    )


class APICog(commands.Cog):
    def __init__(self: 'APICog', bot: commands.Bot) -> None:
        register_commands(self)
        self.bot: commands.Bot = bot

    @app_commands.command(description='sends a random picture of a fox')
    async def fox(self: 'APICog', interaction: Interaction) -> None:
        async with interaction.channel.typing():
            async def get_fox() -> str:
                return js_loads(get_request('https://randomfox.ca/floof/').text)['image']

            async def btn_interaction(btn_interaction_p: ui.ButtonInteraction):
                embed: Embed = btn_interaction_p.message.embeds[0].set_image(url=await get_fox())
                await btn_interaction_p.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label='next')

            view: ui.View = ui.View()

            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title='A Fox')
            ui_embed.set_image(url=await get_fox())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @app_commands.command(description='sends a random image of a dog')
    async def dog(self: 'APICog', interaction: Interaction) -> None:
        async with interaction.channel.typing():
            async def get_dog() -> str:
                return js_loads(get_request('https://dog.ceo/api/breeds/image/random').text)['message']

            async def btn_interaction(_btn_interaction: ui.ButtonInteraction):
                embed: Embed = _btn_interaction.message.embeds[0].set_image(url=await get_dog())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label='next')

            view: ui.View = ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title='A Dog')
            ui_embed.set_image(url=await get_dog())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @app_commands.command(description='sends a random image of a cat')
    async def cat(self: 'APICog', interaction: Interaction) -> None:
        async with interaction.channel.typing():
            async def get_cat() -> str:
                return js_loads(get_request('https://aws.random.cat/meow').text)['file']

            async def btn_interaction(_btn_interaction: ui.ButtonInteraction) -> None:
                embed: Embed = _btn_interaction.message.embeds[0].set_image(url=await get_cat())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label='next')

            view: ui.View = ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            uiEmbed: Embed = Embed(title='A complete catalogue')
            uiEmbed.set_image(url=await get_cat())

            await interaction.response.send_message(embed=uiEmbed, view=view)

    @app_commands.command(description='sends a meme')
    async def meme(self: 'APICog', interaction: Interaction) -> None:
        async with interaction.channel.typing():
            async def get_meme():
                return js_loads(get_request('https://meme-api.herokuapp.com/gimme').text)['url']

            async def btn_interaction(_btn_interaction: ui.ButtonInteraction) -> None:
                embed: Embed = _btn_interaction.message.embeds[0].set_image(url=await get_meme())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label='next')

            view: ui.View = ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title='A meme')
            ui_embed.set_image(url=await get_meme())

        await interaction.response.send_message(embed=ui_embed, view=view)

    @app_commands.command(description='sends a random fact about a cat')
    async def catfact(self: 'APICog', interaction: Interaction) -> None:
        async with interaction.channel.typing():
            em: Embed = Embed(title='A cat fact', description='learn more about cats here: https://www.catster.com/')
            em.add_field(
                name='Did you know...',
                value=js_loads(get_request('https://catfact.ninja/fact').text)['fact']
            )

        await interaction.response.send_message(embed=em)

    @app_commands.command(description='sends a random fact about a dog')
    async def dogfact(self, interaction: Interaction) -> None:
        async with interaction.channel.typing():
            em: Embed = Embed(title='A dog fact', description='learn more about cats here: https://dog-api.kinduff.com/')
            em.add_field(
                name='Did you know...',
                value=js_loads(get_request('https://dog-api.kinduff.com/api/facts').text)['facts'][0]
            )

        await interaction.response.send_message(embed=em)

    def pass_(self) -> None:...

    def __cog_docs__(self) -> str:
        self.pass_()
        return '''
        The cog is a wrapper for all the api related commands.
        These include:
            - fox
            - dog
            - cat
            - meme
            - catfact
            - dogfact
        '''

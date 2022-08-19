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


from aiohttp import ClientSession
from discord.ext import commands
from cache import cacheGet
import cogs._helpCommandSetup
from discord import Embed, Interaction, app_commands, Object, ui


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(APICog(bot), guilds=[Object(id=cacheGet("id"))])


class APICog(commands.Cog):
    def __init__(self: "APICog", bot: commands.Bot) -> None:
        self.cs: ClientSession = ClientSession()
        self.bot: commands.Bot = bot

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Sends a random picture of a fox.")
    async def fox(self: "APICog", interaction: Interaction) -> None:
        async with interaction.channel.typing():

            async def get_fox() -> str:
                req = await self.cs.get("https://randomfox.ca/floof/")
                data = await req.json()
                del req

                return data["image"]

            async def btn_interaction(btn_interaction_p: Interaction):
                embed: Embed = btn_interaction_p.message.embeds[0].set_image(url=await get_fox())
                await btn_interaction_p.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label="next")

            view: ui.View = ui.View()

            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title="A Fox")
            ui_embed.set_image(url=await get_fox())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Sends a random image of a dog.")
    async def dog(self: "APICog", interaction: Interaction) -> None:
        async with interaction.channel.typing():

            async def get_dog() -> str:
                req = await self.cs.get("https://dog.ceo/api/breeds/image/random")
                data = await req.json()
                del req

                return data["message"]

            async def btn_interaction(_btn_interaction: Interaction):
                embed: Embed = _btn_interaction.message.embeds[0].set_image(url=await get_dog())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label="next")

            view: ui.View = ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title="A Dog")
            ui_embed.set_image(url=await get_dog())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Sends a random image of a cat.")
    async def cat(self: "APICog", interaction: Interaction) -> None:
        async with interaction.channel.typing():

            async def get_cat() -> str:
                req = await self.cs.get("https://aws.random.cat/meow")
                data = await req.json()
                del req

                return data["file"]

            async def btn_interaction(_btn_interaction: Interaction) -> None:
                embed: Embed = _btn_interaction.message.embeds[0].set_image(url=await get_cat())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label="next")

            view: ui.View = ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title="A complete catalogue")
            ui_embed.set_image(url=await get_cat())

            await interaction.response.send_message(embed=ui_embed, view=view)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Sends a meme.")
    async def meme(self: "APICog", interaction: Interaction) -> None:
        async with interaction.channel.typing():

            async def get_meme():
                req = await self.cs.get("https://meme-api.herokuapp.com/gimme")
                data = await req.json()
                del req

                return data["url"]

            async def btn_interaction(_btn_interaction: Interaction) -> None:
                embed: Embed = _btn_interaction.message.embeds[0].set_image(url=await get_meme())
                await _btn_interaction.response.edit_message(embed=embed)

            next_btn: ui.Button = ui.Button(label="next")

            view: ui.View = ui.View()
            next_btn.callback = btn_interaction

            view.add_item(next_btn)

            ui_embed: Embed = Embed(title="A meme")
            ui_embed.set_image(url=await get_meme())

        await interaction.response.send_message(embed=ui_embed, view=view)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Sends a random fact about a cat.")
    async def catfact(self: "APICog", interaction: Interaction) -> None:
        async with interaction.channel.typing():
            req = await self.cs.get("https://catfact.ninja/fact")
            res = await req.json()
            em: Embed = Embed(
                title="A cat fact",
                description="learn more about cats here: https://www.catster.com/",
            )
            em.add_field(name="Did you know...", value=res["fact"])

        del req, res
        await interaction.response.send_message(embed=em)

    @cogs._helpCommandSetup.record()
    @app_commands.command(description="Sends a random fact about a dog.")
    async def dogfact(self, interaction: Interaction) -> None:
        async with interaction.channel.typing():
            req = await self.cs.get("https://dog-api.kinduff.com/api/facts")
            res = await req.json()

            em: Embed = Embed(
                title="A dog fact",
                description="learn more about cats here: https://dog-api.kinduff.com/",
            )
            em.add_field(name="Did you know...", value=res["facts"][0])

        del req, res
        await interaction.response.send_message(embed=em)

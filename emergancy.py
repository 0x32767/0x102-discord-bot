import nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("The bot is now activated")

testingserverid = 

@client.slash_command(name = "hello",description= "inceput",guild_ids=[testingserverid])
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message("hello")

client.run("")

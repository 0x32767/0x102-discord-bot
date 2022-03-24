from discord.ext import commands
import discord


intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix='~',
    intents=intents,
    application_id=866344879070904380
)

TEST_GUILD = discord.Object(938541999961833574)


@bot.event
async def on_ready():
    print('online')


@bot.event
async def setup_hook():
    await bot.load_extension('cogs.cog')
    await bot.tree.sync(guild=TEST_GUILD)


bot.run('ODY2MzQ0ODc5MDcwOTA0Mzgw.YPRMiw.JjZljreMV4c6LZFqOPGhoThysMY')

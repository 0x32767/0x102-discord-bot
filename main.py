from discord.ext import commands
from os import listdir
import aiosqlite
import discord
from rich.progress import track
from rich.console import Console
from _tokens import TOKEN


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(
    command_prefix='~',
    intents=intents,
    application_id=937461852282167337
)

console = Console()
TEST_GUILD = discord.Object(938541999961833574)


@bot.event
async def on_ready():
    console.clear()

    async with aiosqlite.connect('discordbotdb.db') as database:
        async with database.cursor() as cur:
            for server in bot.guilds:
                """
                 | Adds individual users to the `discordbotdb.db`
                 | database. This database is used to keep track
                 | of all the users attributes, e.g levels.
                """
                for user in server.members:
                    # ! if the user does not exist in the database, add them
                    await cur.execute(f"select * from levels where guild_id = {user.id} and user_id = {server.id}")

                    if not await cur.fetchall():
                        await cur.execute(f'INSERT INTO levels VALUES({server.id}, {user.id}, 0, 0)')

                    # ! if the user does exist in the database, we add them to the database
                    # ! the database is setup to have a default `false` value for the `whitelisted` column
                    await cur.execute(f'select * from whitelist where guild_id = {server.id} and user_id = {user.id}')

                    if not await cur.fetchall():
                        await cur.execute(f'INSERT INTO whitelist VALUES({server.id}, {user.id}, false)')

        await database.commit()

    async with aiosqlite.connect('stonks.db') as database:
        async with database.cursor() as cur:
            await cur.execute("SELECT guild_id FROM server_stonks")
            data = await cur.fetchall()

            # ! by default the `data` variable is a list of tuples
            servers = [x[0] for x in data]
            for server in bot.guilds:
                """
                 | adds the guild to the `stonks.db` database,
                 | if it doesn't exist already. This database
                 | is used to keep track of the value o0f the
                 | currancy that has been assighned to the
                 | server.
                """
                if server.id not in servers:
                    await cur.execute(f'INSERT INTO server_stonks VALUES({server.id}, "${server.name}$", 1)')

        await database.commit()

    num_cogs = 0
    idl_cogs = 0

    for cog in track(
        listdir('cogs'),
        console=console,
        description="[bald][bright_red]Loading cogs...[/bright_red][/bald]",
        total=len(listdir('cogs'))
    ):
        if cog.endswith('.py') and not cog.startswith('_'):
            try:
                await bot.load_extension(f"cogs.{cog[:-3]}")
                console.print(
                    f"  [green]Successfully loaded: [/green][bright_yellow][underline]{cog}[/underline][/bright_yellow]"
                )
                num_cogs += 1

            except Exception as e:
                console.print(f'[red]Failed loading  cog: [/red][orange_red1]{cog}[/orange_red1] [{e}]')

            finally:
                idl_cogs += 1

    console.print(f'\nSuccessfully loaded [bald][dark_orange3][{num_cogs}/{idl_cogs}][/dark_orange3][bals] cogs')

    await bot.tree.sync(guild=TEST_GUILD)

    console.print(f'[green]Logged in as: [/green][bright_yellow][underline]{bot.user.name}[/underline][/bright_yellow]')


bot.run(TOKEN)

from discord.ext import commands


recorded_commands = set([])


def record() -> callable:
    def wrapper(func: commands.Command) -> commands.Command:
        recorded_commands.add(func)
        return func

    return wrapper

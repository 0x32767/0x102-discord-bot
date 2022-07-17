from discord.ext import commands


recorded_commands: list[commands.Command] = []


def record(usage: str="/") -> callable:
    def wrapper(func: commands.Command) -> commands.Command:
        if usage == "/":
            recorded_commands.append({"f": func, "u": f"/{func.name}"})

        else:
            recorded_commands.append({"f": func, "u": usage})

        return func

    return wrapper

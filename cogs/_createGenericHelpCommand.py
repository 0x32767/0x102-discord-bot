from discord.ext import commands


def createFile(filename: str, commands: list) -> None:
    with open(filename, "w") as f:
        f.write(createDocs(commands))


def createDocs(commands: list[commands.Command]) -> str:
    return "".join(
        f"""## /{c["f"].name}\n\n> Usage:\n\n`{c["u"]}`\n\n{c["f"].description}\n"""
        for c in commands
    )

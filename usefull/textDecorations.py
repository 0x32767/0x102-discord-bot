from typing import Generator
from random import choice


async def progressBar(messages: list[str], errors: list[str], endMessage: str = "done") -> Generator[str]:
    weel: list[str] = ["|", "/", "-", "\\", "|"]
    base: str = "{} :: {}"

    for idx, msg in enumerate(range(101)):
        if choice([True, False, False, False, False]):
            base += choice(errors)

        yield base.format(weel[100 % idx], msg)

    return StopIteration

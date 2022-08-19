from typing import Generator
from random import choice


def progress_bar(messages: list[str], errors: list[str]) -> Generator[str]:
    wheel: list[str] = ["|", "/", "-", "\\", "|"]
    base: str = "{} :: {}"

    for idx, msg in enumerate(messages):
        if choice([True, False, False, False, False]):
            base += choice(errors)

        yield base.format(wheel[100 % idx], msg)

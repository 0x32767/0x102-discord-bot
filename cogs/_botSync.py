from aiohttp import ClientSession
from aiosqlite import connect


class botSync:
    def __init__(self: "botSync", file: str) -> None:
        self.file: str = file

    def syncLocal(self: "botSync") -> None:
        ...

from discord import Interaction
from cache import cacheSet, cacheGet, cacheExist
from lupa import LuaRuntime


class LuaDiscordRuntimeEnvironment:
    def __init__(self: "LuaDiscordRuntimeEnvironment") -> None:
        self.lua: LuaRuntime = LuaRuntime(unpack_returned_tuples=True)


async def run(code: str, ctx: Interaction) -> None:
    if not code:
        return

    if not cacheExist("lua"):
        cacheSet("lua", LuaDiscordRuntimeEnvironment())

    func: callable = cacheGet("lua").lua.eval(code)
    await ctx.response.send_message(func())

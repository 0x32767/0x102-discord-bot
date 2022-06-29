from lupa import LuaRuntime
from cogs._luaCtx import luaCtx
from discord import (
    Interaction
)


class LuaDiscordRuntimeEnvironment:
    def __init__(self: "LuaDiscordRuntimeEnvironment") -> None:
        self.lua: LuaRuntime = LuaRuntime(unpack_returned_tuples=True)

    def invoke(self: "LuaDiscordRuntimeEnvironment", ctx: Interaction, code: str) -> tuple[callable, any]:
        function_: function = self.lua.run(code)
        return (function_, luaCtx(ctx))

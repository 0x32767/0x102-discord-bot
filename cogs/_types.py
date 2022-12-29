from typing import NewType, Union, LiteralString, Tuple, Literal, Any
from enum import IntEnum, auto

# shards are for features
class _Shard(IntEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        """
        :name str
        """
        return name.lower()

    ACHIVEMENTS = auto()
    EASTER_EGGS = auto()
    LEVELING = auto()
    ITEMS = auto()


shard = NewType(
    "shard",
    Union[
        Literal("achivements"),
        Literal("easter-eggs"),
        Literal("leveling"),
        Literal("items"),
    ],
)

shards = NewType("shards", Tuple[shard])


# snowflakes are for items
snowflake = NewType(
    "shard",
    Union[
        LiteralString("achivements"),
        LiteralString("easter-eggs"),
        LiteralString("leveling"),
        LiteralString("items"),
    ],
)

snowflakes = NewType("snowflakes", Tuple[snowflake])

# general

guild_id = NewType("guild_id", int)
user_id = NewType("user_id", int)

# statuses

# it worked well
success = NewType("success", 0)

# invalid input
invalid = NewType("invalid", 1)

# function error
error = NewType("error", 2)

# a http like status which is eather a success, invalid or error
status = NewType("status", Union[success, invalid, error])

result = NewType("result", Tuple[status, LiteralString])

from typing import NewType, Union, Tuple, Any
from enum import StrEnum, auto


# shards are for features
class Shard(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        """
        :name str
        """
        return name.lower()

    ACHIEVEMENTS = auto()
    EASTER_EGGS = auto()
    LEVELING = auto()
    ITEMS = auto()


shard = NewType(
    "shard",
    Union[
        Shard.ACHIEVEMENTS,
        Shard.EASTER_EGGS,
        Shard.LEVELING,
        Shard.ITEMS,
    ],
)

shards = NewType("shards", Tuple[shard])


# snowflakes are for items


class Snowflake(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        """
        :name str
        """
        return name.lower()

    RARITY = auto()
    RANK = auto()
    NAME = auto()
    IMG = auto()
    ID = auto()


snowflake = NewType(
    "shard",
    Union[
        Snowflake.RARITY,
        Snowflake.NAME,
        Snowflake.RANK,
        Snowflake.ID,
    ],
)

snowflakes = NewType("snowflakes", Tuple[snowflake])


# general

guild_id = NewType("guild_id", int)
user_id = NewType("user_id", int)

# statuses

# it worked well
success = 0

# invalid input
invalid = 1

# function error
error = 2

# a http like status which is either a success, invalid or error
status = NewType("status", Union[success, invalid, error])

result = NewType("result", Tuple[status, str])

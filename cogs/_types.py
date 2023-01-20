from typing import NewType, Union, Tuple
from enum import StrEnum, auto


# shards are for features
class Shard(StrEnum):
    ACHIEVEMENTS = auto()
    EASTER_EGGS = auto()
    LEVELING = auto()
    ITEMS = auto()


t_shard = NewType(
    "t_shard",
    Union[
        Shard.ACHIEVEMENTS,
        Shard.EASTER_EGGS,
        Shard.LEVELING,
        Shard.ITEMS,
    ],
)

t_shards = NewType("t_shards", Tuple[t_shard])


# snowflakes are for items


class Snowflake(StrEnum):
    RARITY = auto()
    RANK = auto()
    NAME = auto()
    IMG = auto()
    ID = auto()


t_snowflake = NewType(
    "shard",
    Union[
        Snowflake.RARITY,
        Snowflake.NAME,
        Snowflake.RANK,
        Snowflake.ID,
    ],
)

t_snowflakes = NewType("t_snowflakes", Tuple[t_snowflake])


# reqards


class RewardShard(StrEnum):
    RAND_COINS_D = auto()  # DIRT
    RAND_COINS_L = auto()  # LOW
    RAND_COINS_O = auto()  # OK ish
    RAND_COINS_M = auto()  # MEDIUM
    RAND_COINS_H = auto()  # HIGH
    RAND_COINS_B = auto()  # BEST

    RAND_ITEMS_D = auto()  # DIRT
    RAND_ITEMS_L = auto()  # LOW
    RAND_ITEMS_O = auto()  # OK ish
    RAND_ITEMS_M = auto()  # MEDIUM
    RAND_ITEMS_H = auto()  # HIGH
    RAND_ITEMS_B = auto()  # BEST


t_reward = NewType(
    "t_reward",
    Union[
        RewardShard.RAND_COINS_D,
        RewardShard.RAND_COINS_L,
        RewardShard.RAND_COINS_O,
        RewardShard.RAND_COINS_M,
        RewardShard.RAND_COINS_H,
        RewardShard.RAND_COINS_B,
        RewardShard.RAND_ITEMS_D,
        RewardShard.RAND_ITEMS_L,
        RewardShard.RAND_ITEMS_O,
        RewardShard.RAND_ITEMS_M,
        RewardShard.RAND_ITEMS_H,
        RewardShard.RAND_ITEMS_B,
    ],
)

t_rewards = NewType("rewards_t", Tuple[t_reward])

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
t_status = NewType("t_status", Union[success, invalid, error])

t_result = NewType("result", Tuple[t_status, str])

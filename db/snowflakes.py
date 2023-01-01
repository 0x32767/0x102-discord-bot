from enum import StrEnum, auto
from typing import Any


class ItemSnowflakes(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        # This function just returns the lower ed name of the name of the enum
        # If this enum has a property called: "ABC" and auto is the value that is set to it,
        # AKA:
        # ... ABC = auto()
        # Then the function is called and auto would return "abc"
        return name.lower()

    RARITY = auto()
    NAME = auto()
    IMG = auto()
    ID = auto()

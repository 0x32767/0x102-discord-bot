from typing import Generic, TypeVar, Required, Optional, overload
from ctypes import CDLL

T = TypeVar("T", str, int)


class Array(Generic[T]):
    __slots__ = "__init__", "peek"

    def __init__(self) -> None:
        self.lib = CDLL(r"C:\Users\19MansH\programing\discord-bot\rust\target\release\rust_lib.dll")
        self.arr = self.lib.array_init((1 if isinstance(T, int) else 2).to_bytes(4, byteorder="little"))

    def peek(self) -> T:
        return self.arr.peek()

    # where we want to mutate the array
    @overload
    def pop(self, amount: Optional[int] = 1) -> T:
        if not isinstance(amount, int):
            raise TypeError(f"Exprected int for amount of times")

        self.arr.pop((amount).to_bytes(4, byteorder="little"))

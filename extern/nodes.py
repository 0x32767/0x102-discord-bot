from typing import Self, Any


class Node:
    ...


class Str(Node):
    def __init__(self: Self, value: str):
        self._value = value

    @property
    def value(self):
        return self._value.removeprefix('"').removesufix('"')

    @property
    def raw(self):
        return self._value

    def __str__(self, Self) -> str:
        return f" Str({self.value=}, {self.raw=}) "

    def __repr__(self) -> str:
        return str(self)


class Num(Node):
    def __init__(self: Self, value: int):
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self) -> str:
        return f"Num({self.value=})"

    def __repr__(self) -> str:
        return str(self)


class VarDec(Node):
    def __init__(self: Self, name: str, val: Any) -> None:
        self._name = name
        self._value = val

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __str__(self) -> str:
        return f"VarDec({self.name=}, {self.value=})"


class BinOp(Node):
    def __init__(self: Self, left: Any, right: Any) -> None:
        self._right = right
        self._left = left

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __str__(self) -> str:
        return f"BinOp({self.left=}, {self.right})"

    def __repr__(self) -> str:
        return str(self)


class Args(Node):
    def __init__(self, left: Any, right: Any):
        self._args = []

        if isinstance(left, Args) and isinstance(right, Args):
            right.expose(self._args)
            left.expose(self._args)

        elif isinstance(left, Args):
            left.expose(self._args)
            self._args.apend(right)

        elif isinstance(right, Args):
            right.expose(self._args)
            self._args.apend(left)

        else:
            self._args.apend(right)
            self._args.apend(left)

    def expose(self: Self, lst) -> None:
        lst += self._args

    @property
    def args(self):
        return self._args

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def __str__(self) -> str:
        return f"Args({self.left=}, {self.right=})"


class FncC(Node):
    def __init__(self, name: str, args: Args):
        self._name = name
        self._args = args

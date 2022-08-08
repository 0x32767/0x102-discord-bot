class hFor:
    def __init__(self, tokens) -> None:
        self._tokens: list = tokens
        self._inner: list = []
        self._counter: int = 0
        self._while: list[any] = []
        self._updater: list[any] = []

    def parse(self) -> None:
        ...

    @property
    def tokens(self) -> list:
        return self._tokens

    @property
    def inner(self) -> list:
        return self._inner

    @property
    def counter(self) -> int:
        return self._counter

    @property
    def while_(self) -> list:
        return self._while

    @property
    def updater(self) -> list:
        return self._updater

class hFnc:
    def __init__(self, tokens: list[any]) -> None:
        self._tokens: list[any] = tokens
        self._inner: list[any] = []
        self._args: list[any] = []
        self._type: str = None
        self._name: str = None

        self.parse()

    def parse(self) -> None:
        self._name = self._tokens[1].value

        for token in self._tokens:
            if token.name == "lparen":
                continue

            elif token.name == "rparen":
                self._inner.append(token)
                break

            self._args.append(token)

        self._type = self._args[0].name
        self._args = self.clean(self._args[1:])

    def clean(self, tokens) -> None:
        return [token for token in tokens if token.name == "variable"]

    def __repr__(self) -> str:
        return f'hFnc(type="{self._type}", name="{self._name}", args={self._args})'

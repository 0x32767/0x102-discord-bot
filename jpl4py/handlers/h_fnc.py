class hFnc:
    def __init__(self, tokens: list[any]) -> None:
        self._tokens: list[any] = tokens
        self._inner: list[any] = []
        self._args: list[any] = []
        self._type: str = None
        self._name: str = None

        self.parse()

    def parse(self) -> None:
        self._type = self._tokens[0].name

        for token in self._tokens:
            if token.name == "lparen":
                continue

            elif token.name == "rparen":
                self._inner.append(token)
                break

            self._args.append(token)
        
        self._name = self._args[0].name
        self._args = self._args[1:]

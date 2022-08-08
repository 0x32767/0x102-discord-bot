from handlers.h_for import hFor


class phpParser:
    def __init__(self, tokens) -> None:
        self.tokens: list = tokens

    def parse(self) -> None:
        for token in self.tokens:
            match token.name:
                case "for":
                    ...

class hElif:
    def __init__(self, tokens: list[any]) -> None:
        self.tokens: list = tokens
        self.comparisons: list = []
        self.condition = None
        self.inner: list = []

        self.alway_true: bool = False
        # always true is for if someone writes:
        # if (1==1) {
        #     print("true")
        # }
        self.parse()

    def parse(self) -> None:
        conditions: list = []
        nest = 0

        for token in self.tokens:
            if token.type == "lparen":
                conditions.append(token)
                nest += 1

            elif token.type == "rparen":
                nest -= 1

                if nest == 0:
                    conditions.append(token)
                    self.conditions = conditions

                elif nest == 1 and token.raw in ["==", "!=", ">", "<", ">=", "<="]:
                    self.comparison = token

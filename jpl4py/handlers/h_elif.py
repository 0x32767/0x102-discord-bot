class hElif:
    def __init__(self, tokens: list[any]) -> None:
        self.tokens: list = tokens
        self.conditions: list = []
        self.inner: list = []

        self.alway_true: bool = False
        # always true is for if someone writes:
        # if (1==1) {
        #     print("true")
        # }

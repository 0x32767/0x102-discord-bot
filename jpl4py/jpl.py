from sly import Lexer, Parser
import json


def _():
    ...


class jplLexer(Lexer):
    tokens = {
        "NAME",
        "NUMBER",
        "STRING",
        "IF",
        "ELSE",
        "FOR",
        "JFN",
        "EQEQ",
        "NE",
        "LE",
        "GE",
        "GE",
        "PP",
        "EQ",
        "NEQ",
        "VAR",
    }
    ignore = "\t "

    literals = {
        "=",
        "+",
        "-",
        "/",
        "*",
        "(",
        ")",
        ",",
        ";",
        "{",
        "}",
        "[",
        "]",
        ">",
        "<",
    }

    # Define tokens
    IF = r"if"
    ELSE = r"else"
    FOR = r"for"
    JFN = r"jfn"
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    VAR = r"\$[a-zA-Z_][a-zA-Z0-9_]*"
    STRING = r"\".*?\""

    EQEQ = r"=="
    LE = r"\<\="
    GE = r"\>\="
    PP = r"\+\+"

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r"#.*")
    def COMMENT(self, t):
        pass

    @_(r"\n+")
    def newline(self, t):
        self.lineno = t.value.count("\n")


class jplParser(Parser):
    tokens = jplLexer.tokens

    def __init__(self):
        self.env = {}

    @_("NAME")
    def expr(self, p):
        return {"type": "name", "name": p.NAME}

    @_("VAR")
    def expr(self, p):
        return {"type": "var", "name": p.VAR}

    @_("NUMBER")
    def expr(self, p):
        return {"type": "num", "value": p.NUMBER}

    @_("STRING")
    def expr(self, p):
        return {"type": "str", "value": p.STRING}

    @_("expr EQEQ expr")
    def expr(self, p):
        return {"type": "==", "1": p.expr0, "2": p.expr1}

    @_("expr GE expr")
    def expr(self, p):
        return {"type": "GEEQ", "1": p.expr0, "2": p.expr1}

    @_("expr LE expr")
    def expr(self, p):
        return {"type": "LTEQ", "1": p.expr0, "2": p.expr1}

    @_('expr ">" expr')
    def expr(self, p):
        return {"type": "GT", "1": p.expr0, "2": p.expr1}

    @_('expr "<" expr')
    def expr(self, p):
        return {"type": "LT", "1": p.expr0, "2": p.expr1}

    @_('expr "+" expr')
    def expr(self, p):
        return {"type": "add", "1": p.expr0, "2": p.expr1}

    @_('expr "-" expr')
    def expr(self, p):
        return {"type": "sub", "1": p.expr0, "2": p.expr1}

    @_('expr "*" expr')
    def expr(self, p):
        return {"type": "mul", "1": p.expr0, "2": p.expr1}

    @_('expr "/" expr')
    def expr(self, p):
        return {"type": "div", "1": p.expr0, "2": p.expr1}

    @_('expr "&" expr')
    def expr(self, p):
        return {"type": "and", "1": p.expr0, "2": p.expr1}

    @_('expr "|" expr')
    def expr(self, p):
        return {"type": "or", "1": p.expr0, "2": p.expr1}

    @_("expr PP")
    def expr(self, p):
        return {"type": "inc", "tar": p.expr}

    @_('"(" expr ")"')
    def expr(self, p):
        return {"type": "bracket", "tar": p.expr}

    @_('expr "+" "(" expr ")"')
    def expr(self, p):
        return {"type": "add", "1": p.expr0, "2": p.expr1}

    @_('expr "-" "(" expr ")"')
    def expr(self, p):
        return {"type": "sub", "1": p.expr0, "2": p.expr1}

    @_('expr "*" "(" expr ")"')
    def expr(self, p):
        return {"type": "mul", "1": p.expr0, "2": p.expr1}

    @_('expr "/" "(" expr ")"')
    def expr(self, p):
        return {"type": "div", "1": p.expr0, "2": p.expr1}

    @_(' NAME "(" expr ")"')
    def expr(self, p):
        return {"type": "call", "fnc": p.NAME, "params": p.expr}

    @_('NAME "(" ")"')
    def expr(self, p):
        return {"type": "call", "fnc": p.NAME, "params": []}

    @_('IF "(" expr ")" "{" expr "}" ELSE "{" expr "}" ')
    def expr(self, p):
        return {"type": "if", "if": p.expr0, "then": p.expr1, "else": p.expr2}

    @_('FOR "(" expr ";" expr ";" expr ")" "{" expr "}"')
    def expr(self, p):
        return {
            "type": "for",
            "cou": p.expr0,
            "con": p.expr1,
            "up": p.expr2,
            "inner": p.expr3,
        }

    @_('JFN NAME "(" expr ")" "{" expr "}"')
    def expr(self, p):
        return {"jfn", p.expr0, p.expr1}

    @_('JFN NAME "(" ")" "{" expr "}"')
    def expr(self, p):
        return {"type": "jfn", "name": p.NAME, "args": {}, "inner": p.expr}

    @_('VAR "=" expr')
    def expr(self, p):
        return {"type": "vardec", "tar": p.VAR, "eq": p.expr}

    @_('expr "," expr')
    def expr(self, p):
        return [p.expr0, p.expr1]

    @_('VAR "," VAR')
    def expr(self, p):
        return [p.VAR0, p.VAR1]


if __name__ == "__main__":
    lexer = jplLexer()
    parser = jplParser()

    while True:
        try:
            text = input("jpl > ")
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))

            if tree["fnc"] == "run":
                print(tree["inner"])
                continue

            with open("out.json", "w") as f:
                json.dump(tree, f, indent=4)

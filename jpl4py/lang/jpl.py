from errors.lex_errors.iligal_character import IllegalCharacterError
from sly import Lexer, Parser
from pprint import pprint


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
        "CFN",
        "CSTR",
        "EQEQ",
        "LE",
        "EQ",
        "GE",
        "GE",
        "PP",
        "NEQ",
    }
    ignore = "\t "

    literals = {
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
    CFN = r"cfn"
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    STRING = r"\".*?\""
    CSTR = r"\`.*?\`"

    EQEQ = r"=="
    LE = r"\<\="
    GE = r"\>\="
    PP = r"\+\+"
    EQ = r"="

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r"#.*", r"\\\*.*?\\\*", r"\\\*.*")
    def COMMENT(self, t):
        pass

    @_(r"\n+")
    def newline(self, t):
        self.lineno = t.value.count("\n")

    def error(self, t):
        raise IllegalCharacterError(self.lineno, [t.value])


class jplParser(Parser):
    tokens = jplLexer.tokens

    def __init__(self):
        self.env = {}

    @_("NAME")
    def expr(self, p):
        return ("name", p.NAME)

    @_("NUMBER")
    def expr(self, p):
        return p.NUMBER

    @_("STRING")
    def expr(self, p):
        return p.STRING

    @_(
        "expr EQEQ expr",
        "expr LE expr",
        "expr GE expr",
        "expr NEQ expr",
        "expr '+' expr",
        "expr '-' expr",
        "expr '*' expr",
        "expr '/' expr",
        "expr '>' expr",
        "expr '<' expr",
    )
    def expr(self, p):
        return [p[1], p.expr0, p.expr1]

    @_(
        'expr "&" expr',
        'expr "|" expr',
    )
    def expr(self, p):
        return [p[1], p.expr0, p.expr1]

    @_("expr PP")
    def expr(self, p):
        return ["inc", p.expr]

    @_('"(" expr ")"')
    def expr(self, p):
        return ["bracket", p.expr]

    @_(' NAME "(" expr ")"', 'NAME "(" ")"')
    def expr(self, p):
        return ["call", p.NAME, p.expr or []]

    @_(
        'IF "(" expr ")" "{" expr "}" ELSE "{" expr "}" ',
        'IF "(" expr ")" "{" expr "}"',
    )
    def expr(self, p):
        return ["if", p.expr0, p.expr1, p.expr2 or []]

    @_('FOR "(" var_dec ";" expr ";" expr ")" "{" expr "}"')
    def expr(self, p):
        return ["for", p.var_dec, p.expr0, p.expr1, p.expr2]

    @_(
        'JFN NAME "(" names ")" "{" expr "}"',
        'JFN NAME "(" ")" "{" expr "}"',
    )
    def expr(self, p):
        try:
            return ["jfn", p.expr0, p.expr1]

        except AttributeError:
            return ["jfn", p.NAME, [], p.expr]

    @_(
        'CFN NAME "(" names ")" "-" ">" NAME "{" CSTR "}"',
        'CFN NAME "(" ")" "-" ">" NAME "{" CSTR "}"',
    )
    def expr(self, p):
        try:
            return ["cfn", p.NAME0, p.names, p.NAME1, p.CSTR]

        except AttributeError:
            return ["cfn", p.NAME0, [], p.NAME1, p.CSTR]

    @_("NAME EQ expr")
    def var_dec(self, p):
        return ["vardec", p.NAME, p.expr]

    @_('expr "," expr')
    def expr(self, p):
        return [p.expr0, p.expr1]

    @_("NAME , NAME")
    def names(self, p):
        return [p.NAME0, p.NAME1]


if __name__ == "__main__":
    lexer = jplLexer()
    parser = jplParser()

    while True:
        tokens = lexer.tokenize(input("> "))
        for t in tokens:
            print(t)

        pprint(parser.parse(tokens))

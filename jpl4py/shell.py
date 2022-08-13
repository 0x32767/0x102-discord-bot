from token_cls import jplToken
from parser import jplParser
from lexer import jplLexer


if __name__ == "__main__":
    parser: jplParser = jplParser()
    lexer: jplLexer = jplLexer()

    while True:
        tokens = lexer.tokenize(input("jpl >>> "))
        print(parser.parse(tokens))

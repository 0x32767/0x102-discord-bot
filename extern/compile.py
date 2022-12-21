from pprint import pprint
from astt import mk_ast


ast = mk_ast("""
extern "abc.py" [
	"print",
	"print"
];
fnc abc()[
	print("Hello");
	print("World");
];
""")

pprint(ast)

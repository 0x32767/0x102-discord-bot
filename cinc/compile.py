import argparse


from pycparser import parse_file
from setup import *

ast = parse_file("test.c")

for fn in ast.ext:
    if fn.decl.name == "_start":
        fn2bc(fn.body)

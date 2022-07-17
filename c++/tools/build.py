from sys import argv
from os import system


def build(name):
    system(f"g++ -c -fPIC {name}.cpp -o bin\\{name}.o")
    system(f"g++ -shared -Wl,-soname,builds\\{name}.so -o builds\\{name}.so bin\\{name}.o")


if __name__ == "__main__":
    build(argv[1])

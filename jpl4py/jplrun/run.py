from sys import argv
import json


env: dict = {}


def invokeFnc(name: str, tree: dict):
    for fnc in tree:
        if fnc["name"] == "main" and fnc["type"] == "jfn":
            body: dict = fnc["inner"]

    for expr in body:
        ...


def handleExpr(expr: dict):
    match expr["type"]:
        case "jfn":
            "error"

        case "var":
            ...


def main():
    with open(f"{argv[1]}.out.json", "r") as f:
        tree = json.load(f)

    invokeFnc("main", tree)


if __name__ == "__main__":
    main()

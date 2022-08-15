from sys import argv
import json


with open(f"{argv[1]}.out.json", "r") as f:
    tree = json.load(f)


def invokeFnc(name: str):
    for fnc in tree:
        if fnc["name"] == "main" and fnc["type"] == "jfn":
            body: dict = fnc["inner"]

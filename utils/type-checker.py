from os import listdir
from ast import *
import re


class Visitor(NodeVisitor):
    def __init__(self: "Visitor") -> None:
        self.errors: list[str] = []

    def visit_AnnAssign(self: "Visitor", node: AnnAssign):
        self.generic_visit(node)

    def visit_FunctionDef(self: "Visitor", node: FunctionDef):
        if edits := [arg.arg for arg in node.args.args if not arg.annotation]:
            self.errors.append(f"{str(node.lineno).zfill(3)} :: need annotations :: {', '.join(edits)}")

        self.generic_visit(node)


visitor = Visitor()


def analyse(path: str, vis: Visitor):
    for file in listdir(path):
        if file in [".git", "__pycache__", ".idea", ".vscode", "LICENSE", "license", "node_modules"]:
            continue

        elif "." not in file:
            analyse(f"{path}\\{file}", vis=vis)

        elif file.endswith(".py"):

            try:
                vis.visit(parse(open(f"{path}\\{file}").read()))

                if vis.errors:
                    print(f"checking {path}\\{file} ...")
                    print(f"\n".join(vis.errors))

            except UnicodeDecodeError:
                print(f"{path}\\{file}\nFailed, unicode error")

            vis.errors = []


analyse("D:\\programing\\0x102-discord-bot", vis=visitor)

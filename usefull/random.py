from random import shuffle


def action(fnc: list[callable]) -> None:
    shuffle(fnc)
    fnc[0]()

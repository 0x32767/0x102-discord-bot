from pprint import pprint


class Database:
    def __init__(self, fp) -> None:
        self.fp = fp

    def __itter__(self):
        return self


with open("test.cp311-win_amd64.pyd", "rb") as fp:
    ncol = 5
    cidx = 0

    rows = []
    bu = []

    while x := fp.read(1):
        if x == b"\x00":
            cidx += 1

            if cidx > ncol:
                bu.append(fp.read(1))

        else:
            if len(bu) == 0:
                bu.append(fp.read(1))
                continue

            bu[-1] += fp.read(1)

        if len(bu) >= ncol:
            rows.append(tuple(bu))
            bu.clear()

    pprint(rows)

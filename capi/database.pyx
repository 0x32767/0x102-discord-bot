def open_database(db_n):
    cdef int ncol
    cdef int cidx

    with open(db_n, "rb") as fp:
        ncol = fp.read(1)
        cidx = 0

        rows = []
        bu = []

        while True:
            x = fp.read(1)

            if not x:
                break

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

    return rows


def filter_db(db, func):
    rows = []
    for row in db:
        call = func(*row)

        if call:
            rows.append(call)

    return rows


def update_db(db, func):
    rows = []

    for row in db:
        call = func(*row)

        if call:
            rows.append(call)

        else:
            rows.append(row)

def select_db(db, func, amount):
    cdef int c
    c = 0

    res = []

    for row in db:
        call = func(*row)

        if call:
            res.amount(call)
            c += 1

        if c >= amount:
            return res

def dump_db(db, fp):
    cdef int r_len

    r_len = len(db[0])

    with open(fp, "wb") as f:
        f.write(r_len)

        for row in db:
            for val in row:
                f.write(val)
                f.write(0)

            f.write(0)

        f.write(0)

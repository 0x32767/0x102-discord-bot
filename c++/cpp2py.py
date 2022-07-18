from ctypes import cdll


def convert(name, bases, cls, origin) -> type:
    lib = cdll.LoadLibrary(origin)

    print(lib.__dict__)

    return type(name, bases, dct)

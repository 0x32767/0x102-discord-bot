from ctypes import cdll, c_char


lib = cdll.LoadLibrary(".\\builds\\profanity.so")


print(type(lib.isCloseMach("hello", "hello")))

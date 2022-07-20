from ctypes import cdll, c_char


lib = cdll.LoadLibrary(".\\builds\\profanity.so")


print(lib.isCloseMach("hello", ""))

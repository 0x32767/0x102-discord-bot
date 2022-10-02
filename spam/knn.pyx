import random


cdef int hypotinuse(int x1, int y1, int x2, y2) -> int:
    return ((x1-x2)**2 + (y1-y2) ** 2) ** .5

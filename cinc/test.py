from dis import dis

def helloWorld():
    a = 0
    b = 1
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    printf("Hello World!")
    return a + b - c / d * e % f


dis(helloWorld)

import dis


def fact(n):
    print("hello world")
    return


for ins in list(dis.Bytecode(fact)):
    print(ins)

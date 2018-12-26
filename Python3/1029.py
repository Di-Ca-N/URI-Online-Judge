c = 0


def fib(a):
    global c
    c += 1
    if a != 1 and a != 0:
        return fib(a-1) + fib(a-2)
    else:
        return a


n = int(input())
for i in range(n):
    b = int(input())
    m, n = 0, 1
    for j in range(b):
        m, n = n, m+n


    print("fib({}) = {} calls = {}".format(b,c-1,k))
    c = 0
#TODO

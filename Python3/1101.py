a, b = map(int,input().split())

while a > 0 and b > 0:
    if a > b:
        a, b = b, a

    seq = ' '.join(str(c) for c in range(a, b+1))
    print("{} Sum={}".format(seq, sum(range(a,b+1))))
    a, b = map(int, input().split())

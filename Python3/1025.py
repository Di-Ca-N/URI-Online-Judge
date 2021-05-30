import bisect

n, q = [int(x) for x in input().split()]
cont = 1

while (n, q) != (0, 0):
    marbles = sorted(int(input()) for _ in range(n))

    print("CASE# {}:".format(cont))
    for j in range(q):
        inp = int(input())
        idx = bisect.bisect_left(marbles, inp)
        if idx < n and marbles[idx] == inp:
            print("{} found at {}".format(inp, idx + 1))
        else:
            print("{} not found".format(inp))
    cont += 1
    n, q = [int(x) for x in input().split()]


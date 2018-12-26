n = int(input())

for i in range(1, n+1):
    a, b, c = i, i**2, i**3
    print("{} {} {}".format(a, b, c))
    print("{} {} {}".format(a, b+1, c+1))

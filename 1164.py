n = int(input())
for teste in range(n):
    divs = []
    a = int(input())

    for i in range(1, a):
        if a % i == 0:
            divs.append(i)

    if sum(divs) == a:
        print("{} eh perfeito".format(a))
    else:
        print("{} nao eh perfeito".format(a))

while True:
    valores = input().split()

    n = int(valores[0])
    d = a = int(valores[1])
    e = b = int(valores[2])

    if n == 0 and a == 0 and b == 0:
        break
    

    while e != 0:
        d, e = e, d % e

    c = (a * b) // d

    a_l = len(range(a, n + 1, a))
    b_l = len(range(b, n + 1, b))
    c_l = len(range(c, n + 1, c))

    print(a_l + b_l - c_l)

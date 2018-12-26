try:
    while True:
        is_valido = False
        numero = int(input())
        if numero >= 0:
            limite = int((numero/2)**0.5)+1
            for x in range(limite):
                y = abs(numero-x**2)**0.5
                if int(y) == y:
                    is_valido = True

        if is_valido:
            print("YES")
        else:
            print("NO")
except EOFError:
    pass

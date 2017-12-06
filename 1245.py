try:
    while True:
        boots = []
        cont = 0
        a = int(input())
        for i in range(a):
            j = tuple(input().split())
            teste = True
            for k in boots:
                if (k[0] == j[0]) and (k[1] != j[1]):
                    boots.remove(k)
                    cont += 1
                    teste = False
            if teste:
                boots.append(j)
        print(cont)

except EOFError:
    pass

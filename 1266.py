a = input()

while a != "0":
    b = input().split()
    if "1" not in b:
        cont = 1
    else:
        cont = 0
        primeiro = b.index("1")
        b = b[primeiro:] + b[:primeiro]
    postes_totais = 0

    for i in b:
        if i == "0":
            cont += 1
        elif cont != "0":
            postes = (cont-1)/2 if (cont%2 != 0) else cont/2
            cont = 0
            postes_totais += postes
    postes_totais += (cont-1)/2 if (cont%2 != 0) else cont/2
    print("%d"%postes_totais)
    a = input()
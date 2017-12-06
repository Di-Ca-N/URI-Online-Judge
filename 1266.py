a = input()
cont = 0
b = input().split()
primeiro = b.index("1")
b = b[primeiro:]+b[:primeiro]
print(b)
postes_totais = 0

for index, value in enumerate(b):
    if b[index] == "0":
        cont += 1
    elif cont != 0:
        postes = (cont-1)/2 if (cont%2 != 0) else cont/2
        cont = 0
        postes_totais += postes
dsadsa
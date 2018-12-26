linha = int(input())
op = input()
matriz = []

for i in range(12):
    k = []
    for l in range(12):
        k.append(float(input()))
    matriz.append(k)

if op == "S":
    valor = sum(matriz[linha])

else:
    valor = sum(matriz[linha])/12

print("{:.1f}".format(valor))

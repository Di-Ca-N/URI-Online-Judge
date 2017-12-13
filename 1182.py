coluna = int(input())
op = input()
matriz = []

for i in range(12):
    k = []
    for l in range(12):
        k.append(float(input()))
    matriz.append(k)

soma = sum(matriz[j][coluna] for j in range(12))
if op == "S":
    valor = soma
else:
    valor = soma / 12

print("{:.1f}".format(valor))

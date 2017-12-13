valores = list(map(int, input().split()))

a = valores[0]
cont = 1
b = 0
while b <= 0:
    b = valores[cont]
    cont += 1

soma = 0

for i in range(b):
    soma += a + i

print(soma)

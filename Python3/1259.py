n = int(input())

pares = []
impares = []

for i in range(n):
	v = int(input())

	if v % 2 == 0:
		pares.append(v)
	else:
		impares.append(v)


for value in sorted(pares):
	print(value)

for value in sorted(impares, reverse=True):
	print(value)

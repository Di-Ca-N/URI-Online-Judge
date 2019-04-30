m, n = map(int, input().split())

dicionario = {}

for i in range(m):
	cargo, valor = input().split()
	dicionario[cargo] = int(valor)

for i in range(n):
	a = input().split()
	total = 0

	while a != ["."]:
		for word in a:
			if word in dicionario:
				total += dicionario[word]
		a = input().split()

	print(total)

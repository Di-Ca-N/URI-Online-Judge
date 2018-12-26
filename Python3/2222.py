q = int(input())

for k in range(q):

	n = int(input())
	conjuntos = []

	for i in range(n):
		conjuntos.append(set(input().split()[1:]))

	m = int(input())

	for j in range(m):
		a, b, c = map(int, input().split())
		conj1 = conjuntos[b - 1]
		conj2 = conjuntos[c - 1]

		if a == 1:
			print(len(conj1.intersection(conj2)))
		else:
			print(len(conj1.union(conj2)))

n = int(input())

while n != 0:
	matriz = []
	k = list(range(1,n+1))
	matriz.append(k)
	linha = k.copy()
	for i in range(1, n):
		teste = linha.copy()
		linha = []
		for j in range(n):
			if j >= i:
				linha.append(teste[j]-1)
			else:
				linha.append(teste[j]+1)
		matriz.append(linha)
	saida = ' '.join(['%3d']*n)
	for m in matriz:
		g = tuple(n for n in m)
		print(saida%g)
	print('')
	n = int(input())
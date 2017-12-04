l, c = map(int,input().split())
matriz = []
valor = None

for i in range(l):
	matriz.append(input().split())

for linha in range(l):
	for coluna in range(c):
		if matriz[linha][coluna] == "42":
			valor = (linha,coluna)

		if valor:
			k,j = valor
			localizado = True
			considerados = ((k-1, j-1), (k-1, j), (k-1, j+1),
							(k,   j-1),           (k,   j+1),
							(k+1, j-1), (k+1, j), (k+1, j+1))

			for casa in considerados:
				x, y = casa
				try:
					if x < 0:
						x = None
					if matriz[x][y] != "7":
						localizado = False
				except:
					pass
			valor = None
			if localizado == True:
				print(x,y)
				exit()
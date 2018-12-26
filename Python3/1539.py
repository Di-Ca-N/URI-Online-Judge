n = int(input())

while n != 0:
	antenas = []
	distancia = [[1001]*n]*n


	for i in range(n):
		x, y, r = map(int, input().split())
		antenas.append([x, y, r])

	for k in range(n):
		for j in range(n):
			d = int(((antenas[k][0] - antenas[j][0]) ** 2 + (antenas[k][1] - antenas[j][1]) ** 2) ** 0.5)
			distancia[k][j] = d
			print(k, j, d)
			print(distancia)
			#if d <= antenas[i][2] else distancia[i][j]

	print(distancia)
	# for k in range(n):
	# 	for i in range(n):
	# 		for j in range(n):
	# 			distancia = ((antenas[i][0] - antenas[j][0]) ** 2 + (antenas[j][1] - antenas[i][1]) ** 2) ** 0.5
				

	# print(matriz)

	# c = int(input())
	# for i in range(c):
	# 	a1, a2 = map(int, input().split())
	# 	out = matriz[a1-1][a2-1] if matriz[a1-1][a2-1] else -1
	# 	print(out)
	# n = int(input())
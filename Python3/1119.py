n, k, m = map(int, input().split())

while [n, k, m] != [0, 0, 0]:
	participantes = list(str(p).rjust(3) for p in range(1, n + 1))
	removidos = [False] * n
	removidos_ordem = []

	i1 = -1
	i2 = n

	while not all(removidos):
		count1 = 0
		while count1 != k:
			i1 = (i1 + 1) % n
			if not removidos[i1]:
				count1 += 1
			
			#print("posicao atual", removidos[i1], "i1 eh", i1)

		count2 = 0
		while count2 != m:
			i2 = (i2 - 1) % n
			if not removidos[i2]:
				count2 += 1
			#print("posicao atual", removidos[i2], "i2 eh", i2)
		
		removidos[i1] = True
		removidos[i2] = True
		
		if i1 == i2:
			removidos_ordem.append(participantes[i1])

		else:
			removidos_ordem.append(participantes[i1])
			removidos_ordem.append(participantes[i2])

		removidos_ordem.append(",")

		#input(str(removidos) + " " + str(removidos_ordem))

	print("".join(removidos_ordem[:-1]))
	n, k, m = map(int, input().split())

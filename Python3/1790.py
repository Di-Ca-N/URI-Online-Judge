c, p = map(int, input().split())

vizinhos = {cidade: [] for cidade in range(c)}
processado = [False] * c

def verifica_ciclo(vertice_base, vertice_procurado):
	global vizinhos

	for j in vizinhos[vertice_base]:
		processado[j] = True
		print(vertice_base)
		if vertice_procurado in vizinhos[j] and j not in vizinhos[vertice_procurado]:
			return True
		else:
			verifica_ciclo(j, vertice_procurado)

	return False


for i in range(p):
	x, y = map(int, input().split())
	vizinhos[x - 1].append(y - 1)
	vizinhos[y - 1].append(x - 1)

print(vizinhos)
cont = 0

for vertice in vizinhos:
	ciclo = False
	if not processado[vertice]:
		ciclo = verifica_ciclo(vertice, vertice)

	if not ciclo:
		cont += 1


print(cont)

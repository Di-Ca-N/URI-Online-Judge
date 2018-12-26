ca, na = map(int, input().split())
fila = []
caixas = []
lim = 0
tempo = 0

for cliente in range(na):
	chegada, tempo_atendimento = map(int, input().split())
	fila.append([chegada, tempo_atendimento])

while fila:
	try:
		while (tempo >= fila[0][0]) and (len(caixas) < ca):
			pessoa = fila[0]
			caixas.append(pessoa[1])

			if tempo - pessoa[0] > 20:
				lim += 1

			fila.pop(0)

		for k in range(len(caixas)):
			caixas[k] -= 1

		while 0 in caixas:
			caixas.remove(0)


		tempo += 1

	except:
		pass

print(lim)

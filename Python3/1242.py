try:
	while True:
		bases = input()

		pilha = []
		ligacoes = 0
		for base in bases:
			if pilha and ((base == "C" and pilha[-1] == "F") or
			   (base == "F" and pilha[-1] == "C") or
			   (base == "B" and pilha[-1] == "S") or
			   (base == "S" and pilha[-1] == "B")):

				pilha.pop()
				ligacoes += 1

			else:
				pilha.append(base)

		print(ligacoes)

except EOFError:
	pass
	
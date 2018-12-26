n = int(input())

while n != 0:
	pilha = [str(k) for k in range(1, n+1)]
	discarded = []

	while len(pilha) > 1:
		discarded.append(pilha.pop(0))
		pilha.append(pilha.pop(0))

	print("Discarded cards: {}".format(", ".join(discarded)))
	print("Remaining card: {}".format(pilha[0]))


	n = int(input())
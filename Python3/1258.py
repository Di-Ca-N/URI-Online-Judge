n = int(input())
espaco = False

while n != 0:
	camisetas = []

	if espaco:
		print()

	for i in range(n):
		nome = input()
		cor, tamanho = input().split()
		
		camisetas.append((cor, tamanho, nome))

	sort1 = sorted(camisetas, key=lambda x: x[2])
	sort2 = sorted(sort1, key=lambda x: x[1], reverse=True)
	sort3 = sorted(sort2, key=lambda x: x[0])

	for camiseta in sort3:
		print(" ".join(camiseta))

	espaco = True
	n = int(input())

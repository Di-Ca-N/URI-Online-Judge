n, q = map(int, input().split())
cont = 1

while (n, q) != (0, 0):

	marbles = []
	for i in range(n):
		marbles.append(int(input()))

	marbles.sort()
	print("CASE# {}:".format(cont))
	for j in range(q):
		inp = int(input())
		if inp in marbles:
			print("{} found at {}".format(inp, marbles.index(inp) + 1))
		else:
			print("{} not found".format(inp))

	cont += 1
	n, q = map(int, input().split())

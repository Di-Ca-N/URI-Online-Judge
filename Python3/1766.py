
n = int(input())

for k in range(n):
	a, b = map(int, input().split())
	estabulo = []
	for j in range(a):
		n, p, i, a = input().split()
		estabulo.append((n, int(p), int(i), float(a)))

	estabulo = sorted(estabulo, key=lambda x: x[0])
	estabulo = sorted(estabulo, key=lambda x: x[3])
	estabulo = sorted(estabulo, key=lambda x: x[2])
	estabulo = sorted(estabulo, key=lambda x: x[1], reverse=True)

	print("CENARIO {%d}"%(k+1))
	for rena in range(b):
		print("{} - {}".format(rena+1, estabulo[rena][0]))

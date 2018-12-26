try:
	cont = 0

	while True:
		a = input()
		charset = set(a)
		chartab = {}
		
		if cont != 0:
			print()

		for char in charset:
			chartab[ord(char)] = a.count(char)

		b = sorted(chartab, reverse=True)
		b = sorted(b, key=lambda x: chartab[x])

		for i in b:
			print("{} {}".format(i, chartab[i]))

		cont += 1

except EOFError:
	pass
	
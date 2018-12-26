try:
	while True:
		ps = input()
		n = int(input())

		ciclos = 0

		reserva = 0
		for l in ps:
			if l == "R":
				reserva += 1

			if reserva == n:
				ciclos += 1
				reserva = 0

			if l == "W":
				ciclos += 1
				if reserva:
					ciclos += 1
					reserva = 0

		if reserva:
			ciclos += 1

		print(ciclos)

except EOFError:
	pass
	
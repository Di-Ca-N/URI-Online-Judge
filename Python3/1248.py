n = int(input())

for i in range(n):
	dieta = list(input())
	cafe = list(input())
	almoco = list(input())

	todos = cafe + almoco

	cheat = False
	for comido in todos:
		if comido in dieta:
			dieta.remove(comido)
		else:
			cheat = True

	if not cheat:
		print("".join(sorted(dieta)))
	else:
		print("CHEATER")

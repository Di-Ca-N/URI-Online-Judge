a = input().split("/")

notas = {"W": 1, "H": 1/2, "Q": 1/4, "E": 1/8, "S": 1/16, "T":1/32, "X": 1/64}

while a != ["*"]:
	corrects = 0
	for compass in a:
		time = 0
		for note in compass:
			time += notas[note]

		if time == 1:
			corrects += 1

	print(corrects)
	a = input().split("/")

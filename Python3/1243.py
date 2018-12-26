try:
	out = []
	while True:
		entry = input().split()
		words = 0
		length = 0
		
		for symbol in entry:
			if symbol[-1] == ".":
				symbol = symbol[:-1]

			if symbol.isalpha():
				words += 1
				length += len(symbol)

		if words == 0:
			med = 0

		else:
			med = length // words

		if med <= 3:
			dif = '250'

		elif med < 6:
			dif = '500'

		else:
			dif = '1000'
		
		print(dif)

except EOFError:
	pass

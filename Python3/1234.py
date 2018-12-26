
try:
	while True:
		text = input()
		out = ""
		cont = 0
		for char in text:
			if char.isalpha():
				if cont % 2 == 0:
					out += char.upper()
				else:
					out += char.lower()

				cont += 1

			else:
				out += char

		print(out)
except EOFError:
	pass
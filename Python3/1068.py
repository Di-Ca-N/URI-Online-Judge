try:
	while True:
		expr = input()
		pilha = []
		r = "correct"
		try:
			for char in expr:
				if char == "(":
					pilha.append(1)
				if char == ")":
					pilha.remove(1)
		except ValueError:
			r = "incorrect"

		finally:
			if len(pilha) > 0:
				r = "incorrect"
			print(r)

except EOFError:
	pass
try:
	while True:
		entry = input()
		pilha = [""]
		out = ""

		for caractere in entry:
			if caractere == "_":
				if pilha[-1] != "_":
					out += "<i>"
					pilha.append("_")
				else:
					out += "</i>"
					pilha.pop()

			elif caractere == "*":
				if pilha[-1] != "*":
					out += "<b>"
					pilha.append("*")
				else:
					out += "</b>"
					pilha.pop()
			else:
				out += caractere

		print(out)

except EOFError:
	pass
	
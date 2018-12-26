try:
	while True:
		a, b, c = map(int, input().split())
		text = input().split()
		linhas = 1
		chars = len(text[0])
		text.pop(0)
		while text:
			if chars + 1 + len(text[0]) <= c:
				chars += 1 + len(text[0])

			else:
				linhas += 1
				chars = len(text[0])
			#print(text[0], len(text[0]), chars, linhas)
			text.pop(0)

		pags = linhas // b
		#print(linhas)
		#print(pags)
		if linhas % b != 0:
			pags += 1
		print(pags)

except EOFError:
	pass
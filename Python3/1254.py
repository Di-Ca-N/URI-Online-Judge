try:
	k = []
	while True:
		tag_cod = input().lower()
		cod = input()
		text = input()

		dentro = False
		
		out = ""
		tag = ""
		for char in text:
			if char == "<":
				dentro = True
				out += "<"

			elif char == ">":
				dentro = False
				fila = []
				for c in tag:
					fila.append(c)
					if len(fila) >= len(tag_cod):
						if "".join(fila[-len(tag_cod):]).lower() == tag_cod:
							out += "".join(fila[:-len(tag_cod)]) + cod
							fila = []

				out += "".join(fila)

				out += ">"
				tag = ""

			else:
				if dentro:
					tag += char
				else:
					out += char 

		k.append(out)

except EOFError:
	print("\n".join(k))

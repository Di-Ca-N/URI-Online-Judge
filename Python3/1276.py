try:
	alp = 'abcdefghijklmnopqrstuvwxyz'
	while True:
		a = set(input())

		a = sorted([k for k in a if k.isalpha()])
		out = []
		try:
			ls = a[0]
			pi = pf =  alp.find(a[0])

			a.pop(0)

			for letter in a:
				if alp.find(letter) == pf + 1:
					pf = alp.find(letter)
				else:
					out.append("{}:{}".format(alp[pi], alp[pf]))
					pi = pf = alp.find(letter)

			out.append("{}:{}".format(alp[pi], alp[pf]))
			print(", ".join(out))
		
		except IndexError:
			print()
except EOFError:
	pass
	
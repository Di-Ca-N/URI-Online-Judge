try:
	while True:
		entry = input().lower().split()
		als = 0
		last_init = ""
		c = False
		for word in entry:
			init = word[0]

			if last_init == init:
				c = True

			else:
				if c:
					als += 1
				c = False

			last_init = init

		if c:
			als += 1

		print(als)

except EOFError:
	pass

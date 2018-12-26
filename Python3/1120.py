a, b = input().split()

while (a, b) != ("0", "0"):
	c = b.replace(a, '')
	if c == '':
		print(0)
	else:
		print(int(c))
	a, b = input().split()

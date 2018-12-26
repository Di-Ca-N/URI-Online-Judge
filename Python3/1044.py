a,b = input().split()

if (int(a) % int(b) == 0) or (int(b) % int(a) == 0):
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")
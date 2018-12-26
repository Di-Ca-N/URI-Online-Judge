n = int(input())

for i in range(n):
	alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	out = ""

	entry = input()
	des = int(input())

	for char in entry:
		if char in alp:
			out += alp[(alp.find(char) - des) % 26]
		else:
			out += char

	print(out)

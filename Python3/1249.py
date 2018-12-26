mins = 'abcdefghijklmnopqrstuvwxyz' 
mais = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
	while True:
		entry = input()
		out = ""
		for char in entry:
			if char in mins:
				index = (mins.find(char) + 13) % 26
				out += mins[index]
			elif char in mais:
				index = (mais.find(char) + 13) % 26
				out += mais[index]
			else:
				out += char

		print(out)

except EOFError:
	pass

n = int(input())

for i in range(n):
	diamonds = 0
	mine = input()
	mine = mine.replace(".", "")
	while "<>" in mine:
		diamond = mine.find("<>")
		mine = mine[0:diamond] + mine[diamond+2:]
		diamonds += 1
	print(diamonds)
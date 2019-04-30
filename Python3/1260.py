#out = open("out.txt", 'w')

try:
	test_cases = int(input())
	blank = input()
	space = False

	for i in range(test_cases):
		forest = {}
		total = 0
		tree = " "
		while tree:
			tree = input()
			if tree:
				if tree in forest:
					forest[tree] += 1
				else:
					forest[tree] = 1
				total += 1

		if space:
			#out.write("\n")
			print()

		for key in sorted(forest.keys()):
			#out.write("{} {:.4f}\n".format(key, forest[key] / total * 100))
			print("{} {:.4f}".format(key, forest[key] / total * 100))

		space = True

except EOFError:
	pass
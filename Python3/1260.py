file = open("out.txt", "w")

try:
	t = int(input())
	for i in range(t):
		forest = {}
		cont = 0
		tree = input()

		while tree != "":
			if tree in forest:
				forest[tree] += 1
			else:
				forest[tree] = 1
			cont += 1
			tree = input()

		keys = list(forest.keys())
		keys.sort()

		for key in keys:
			file.write("{} {:.4f}\n".format(key, forest[key] / cont * 100))

		if i != t-1:
			file.write("\n")
except EOFError:
	pass
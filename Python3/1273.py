a = int(input())
f = True
while a != 0:
	longest_len = 0
	words = []

	for i in range(a):
		word = input()

		if len(word) > longest_len:
			longest_len = len(word)

		words.append(word)
	
	if not f:
		print()

	f = False

	for word in words:
		print("%{}s".format(longest_len)%word)

	a = int(input())

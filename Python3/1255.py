n = int(input())

for i in range(n):
	line = input().lower()
	dic = {}

	for letter in line:
		if letter.isalpha():
			if letter not in dic:
				dic[letter] = 0

			dic[letter] += 1

	mf = max(dic.values())

	ls = [l for l in dic if (dic[l] == mf)]

	print("".join(sorted(ls)))

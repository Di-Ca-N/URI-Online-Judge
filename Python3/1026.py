try:
	while True:
		a, b = map(int, input().split())
		a_bin = bin(a)[2:]
		b_bin = bin(b)[2:]

		digits = max(len(a_bin), len(b_bin))
		a_bin = a_bin.zfill(digits)
		b_bin = b_bin.zfill(digits)

		result = ""
		for i in range(digits-1, -1, -1):
			partial = int(a_bin[i]) + int(b_bin[i])
			if partial == 1:
				result += '1'
			else:
				result += '0'

		result_dec = 0
		pot = 0
		for j in range(len(result) - 1, -1, -1):
			result_dec += int(result[j])*2**pot
			pot += 1

		print(result_dec)

except EOFError:
	pass
	
# TODO: terminar

def merge_sort_and_count(array):
	if len(array) == 1:
		return 0

	ar1 = merge_sort_and_count(array[:len(array)//2])
	ar2 = merge_sort_and_count(array[len(array)//2:])

	inversoes = ar1 + ar2

	while ar2:
		while ar1 and ar1[0] <= ar2[0]:
			ar1.pop(0)

		ar2.pop(0)
		inversoes += len(ar1)

	return inversoes


seq = [int(x)-1 for x in input().split()[1:]]

while seq != []:
	inversions = merge_sort_and_count(seq)
	print(inversions)
	if inversions % 2 == 1:
		print("Marcelo")
	else:
		print("Carlos")

	seq = [int(x)-1 for x in input().split()[1:]]
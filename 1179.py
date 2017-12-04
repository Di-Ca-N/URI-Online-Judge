par = []
impar = []

for i in range(15):
	a = int(input())
	if a % 2 == 0:
		par.append(a)
	else:
		impar.append(a)

	if len(par) == 5:
		for k in range(5):
			print("par[{}] = {}".format(k,par[k]))
		par = []

	if len(impar) == 5:
		for k in range(5):
			print("impar[{}] = {}".format(k,impar[k]))
		impar = []

for g in range(len(impar)):
	print("impar[{}] = {}".format(g,impar[g]))

for h in range(len(par)):
	print("par[{}] = {}".format(h,par[h]))
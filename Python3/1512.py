while True:
	valores = input().split()
	saida = []
	n = int(valores[0])
	d = a = int(valores[1])
	e = b = int(valores[2])

	if n == 0 and a == 0 and b == 0:
		break
	
	try:
		while True:
			d, e = e, d%e

	except ZeroDivisionError:
		c = (a*b)//d

	a_l = len(range(1,n+1,a))
	b_l = len(range(1,n+1,b))
	c_l = len(range(1,n+1,c))

	print(a_l+b_l-c_l)
a, b, c = map(float,input().split(	))

if (a >= (b+c)) or (b >= (a+c)) or (c >= (a+b)):
	area = (a+b)*c/2
	print("Area = {:.1f}".format(area))
else:
	perimetro = a+b+c
	print("Perimetro = {:.1f}".format(perimetro))

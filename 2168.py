n = int(input())
matriz = []
for i in range(n+1):
	matriz.append(input().split())

for j in range(n):
	resultado = ""
	for k in range(n):
		quadra = [matriz[j][k], matriz[j][k+1], matriz[j+1][k], matriz[j+1][k+1]]
		if quadra.count('1') > 1:
			resultado += "S"
		else:
			resultado += "U"
	print(resultado)
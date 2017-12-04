pesos = [2, 3, 4, 1]
notas = list(map(float,input().split()))
z = zip(pesos, notas)
total = 0
for k,j in z:
	total += k*j
media = total/10

print("Media: {:.1f}".format(media))
if 5 <= media < 7:
	print("Aluno em exame.")
	exame = float(input())
	print("Nota do exame: {:.1f}".format(exame))
	media = (media+exame)/2
	if media >= 5:
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final: {:.1f}".format(media))
elif media >= 7:
	print("Aluno aprovado.")
else:
	print("Aluno reprovado.")


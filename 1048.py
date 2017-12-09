salario = float(input())
if salario <= 400:
    percentual = 15

elif 400 < salario <= 800:
    percentual = 12

elif 800 < salario <= 1200:
    percentual = 10

elif 1200 < salario <= 2000:
    percentual = 7

else:
    percentual = 4

reajuste = salario * (percentual / 100)
salario_novo = salario + reajuste

print("""Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: {} %""".format(salario_novo, reajuste, percentual))

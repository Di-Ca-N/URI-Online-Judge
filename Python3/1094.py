n = int(input())
cobaias = {"C": 0, "R": 0, "S": 0}
for i in range(n):
    valores = input().split()
    a = int(valores[0])
    b = valores[1]
    cobaias[b] += a

total = sum(cobaias.values())
coelhos = cobaias["C"]
ratos = cobaias["R"]
sapos = cobaias["S"]

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(coelhos))
print("Total de ratos: {}".format(ratos))
print("Total de sapos: {}".format(sapos))
print("Percentual de coelhos: {:.2f} %".format(coelhos/total*100))
print("Percentual de ratos: {:.2f} %".format(ratos/total*100))
print("Percentual de sapos: {:.2f} %".format(sapos/total*100))

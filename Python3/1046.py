a,b = input().split()
dif = int(b) - int(a)

if dif <= 0:
	dif += 24

print("O JOGO DUROU {} HORA(S)".format(dif))
h1, m1, h2, m2 = map(int, input().split())
minutos = m2 - m1
horas = h2 - h1

if horas <= 0:
    horas += 24
if minutos < 0:
    horas -= 1
    minutos = 60 + minutos

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))

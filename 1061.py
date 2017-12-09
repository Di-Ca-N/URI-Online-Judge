dia_1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(":"))

dia_2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(":"))

segs = s2 - s1
mins = m2 - m1
horas = h2 - h1
dias = dia_2 - dia_1

if segs < 0:
    segs = 60 + segs
    mins -= 1

if mins < 0:
    mins = 60 + mins
    horas -= 1

if horas < 0:
    horas = 24 + horas
    dias -= 1

if dias < 0:
    dias = 0

print("""{} dia(s)
{} hora(s)
{} minuto(s)
{} segundo(s)""".format(dias, horas, mins, segs))

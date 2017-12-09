media, cont = 0, 0
for i in range(6):
    a = float(input())
    if a > 0:
        media += a
        cont += 1

print("{} valores positivos".format(cont))
print("{:.1f}".format(media / cont))

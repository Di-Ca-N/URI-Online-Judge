cont = 0

for i in range(5):
    a = int(input())
    if a % 2 == 0:
        cont += 1
print("{} valores pares".format(cont))

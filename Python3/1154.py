idades = []
a = int(input())

while a >= 0:
    idades.append(a)
    a = int(input())

print("{:.2f}".format(sum(idades)/len(idades)))

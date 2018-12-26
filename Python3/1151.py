a = int(input())
x, y = 0, 1
valores = []
for i in range(a):
    valores.append(str(x))
    x, y = y, x+y

print(' '.join(valores))

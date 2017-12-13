a, b = map(int, input().split())

valores = range(1, b + 1)

for i in range(b//a):
    print("{}".format(' '.join(str(valor) for valor in valores[i*a:(i+1)*a])))
if b % a:
    print(' '.join(str(k) for k in valores[(i+1)*a:]))
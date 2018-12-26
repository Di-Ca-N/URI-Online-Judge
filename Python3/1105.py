m, n = map(int, input().split())

bancos = list(map(int, input().split()))

o = "S"
for i in range(n):
	d, c, v = map(int, input().split())
	bancos[d-1] -= v
	bancos[c-1] += v

o = "N" for banco in bancos if (banco < 0)

print(o)

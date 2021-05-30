n = int(input())
total = 0
for i in range(n):
    t, v = [int(x) for x in input().split()]
    total += t * v

print(total)
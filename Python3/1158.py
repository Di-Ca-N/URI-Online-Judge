n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a % 2 == 0:
        a += 1
    print(sum(range(a, a+2*b, 2)))

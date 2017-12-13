a = int(input())

for i in range(a):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    if x % 2 == 1:
        x += 2
    else:
        x += 1
    print(sum(range(x,y,2)))
